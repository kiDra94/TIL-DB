import socket #socket ist eine combination aus IP und PORT

HOST = "localhost"
PORT = 8080
endpoint = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET - IPv4, SOCK_STREAM - TCP
    server.bind((endpoint))
    server.listen(1)
    print(f"Server is listening to {HOST}:{PORT}")

    conn, addr = server.accept() # server.accept wartet das der Client was sagt
    print(f"Client {addr} is requesting an object!")

    with conn:
        conn.sendall("Was ist mit dir.")
        request = conn.recv(1024) # anzahl von byte
        print(f"Was der Client gigentich wollte: {request.decode()}")