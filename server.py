import socket #socket ist eine combination aus IP und PORT

HOST = "localhost"
PORT = 8080

socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET - IPv4, SOCK_STREAM - TCP
