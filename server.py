import socket
import threading

PORT = 5049
IP = socket.gethostbyname(socket.gethostname())
HEADER = 2
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def handle_client(conn, addr):
	print(f"{addr} connected")
	while True:
		header = conn.recv(HEADER)
		if header:
			if header == b"\xff\xff":
				print(f"{addr} disconnected")
				break
			msg_length = int.from_bytes(header[0:2], byteorder = "big")
			msg = conn.recv(msg_length).decode(FORMAT)
			print(f"<{addr}> {msg}")
	conn.close()

def main():
	print("[server is starting]")
	server.bind((IP, PORT))
	server.listen()
	while True:
		thread = threading.Thread(target = handle_client, args = server.accept())
		thread.start()

if __name__ == "__main__":
	main()
