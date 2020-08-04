import socket
import time

HEADER = 2
PORT = 5049
IP = "192.168.0.94"
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg):
	message = msg.encode(FORMAT)
	msg_length = len(message).to_bytes(2, byteorder = "big")

	client.send(msg_length)
	client.send(message)

def disconnect():
	client.send(b"\xff\xff")

def main():
	client.connect((IP, PORT))
	try:
		while True:
			send(input())
	except KeyboardInterrupt:
		disconnect()
		print("disconnected from the server")

if __name__ == "__main__":
	main()
