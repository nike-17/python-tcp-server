import socket
import thread

def handle(client_socket, address):
	while 1:
		data = client_socket.recv(512)
		client_socket.send(data)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(),6666))
server.listen(2)

while 1:
	client_socket, address = server.accept()
	thread.start_new_thread(handle, (client_socket, address))

