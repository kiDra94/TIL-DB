import socket #socket ist eine combination aus IP und PORT

HOST = "localhost"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET - IPv4, SOCK_STREAM - TCP
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server is listening to {HOST}:{PORT}")

    conn, addr = server.accept() # server.accept wartet das der Client was sagt