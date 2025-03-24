import socket #socket ist eine combination aus IP und PORT

HOST = "localhost"
PORT = 8080

respons = "HTTP/1.1 200 OK\r\n" #\r - carriage retrn \n - new line pflicht lineending fuer HTPP
respons += "Content-Type: text/json\r\n" #nach text kommt das gewuenschte format [plain, html, json, ...]
respons += "Connection: close\r\n\r\n" 
#nach schliessen der connection, commt normal der body 
# der ist mit 2 \r\n gettrent
respons += "{'vorname': 'Hansi', 'nachname': 'Huber'}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET - IPv4, SOCK_STREAM - TCP
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server is listening to {HOST}:{PORT}")

    while True:
        conn, addr = server.accept() # server.accept wartet das der Client was sagt
        print(f"Client {addr} is requesting an object!")

        with conn:
            conn.sendall(respons.encode())
            request = conn.recv(1024) # anzahl von byte
            print(f"Was der Client eigentlch wollte: {request.decode()}")