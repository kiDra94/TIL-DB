import socket #socket ist eine combination aus IP und PORT

class HttpServer:

    def __init__(self, host, port): #Konstruktor
        self.__host = host
        self.__port = port

HOST = "localhost"
PORT = 8080

server = HttpServer(HOST, PORT)

exit()

respons = "HTTP/1.1 200 OK\r\n" #\r - carriage retrn \n - new line pflicht lineending fuer HTPP
respons += "Content-Type: text/json\r\n" #nach text kommt das gewuenschte format [plain, html, json, ...]
respons += "Connection: close\r\n\r\n" 
#nach schliessen der connection, commt normal der body 
# der ist mit 2 \r\n gettrent
respons += "{'vorname': 'Hansi', 'nachname': 'Huber'}"

def handle_request(request):
    lines = request.split("\r\n") #['GET / HTTP/1.1', ..... , 'Priority: u=0, i']
    method, path, _ = lines[0].split(" ") #GET, /.... , nicht zugewiesen
    #GET-> Methode /-> pfad HTTP-> protokoll/1.1-> version
    if method == "GET" and path == "til":
        # SELECT * FROM til
        print("smthing so i do not have errors")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #AF_INET - IPv4, SOCK_STREAM - TCP
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Server is listening to {HOST}:{PORT}")

    while True:
        conn, addr = server.accept() # server.accept wartet das der Client was sagt
        print(f"Client {addr} is requesting an object!")

        with conn:
            handle_request(conn.recv(1024)) # anzahl von byte
            conn.sendall(respons.encode())
            print(f"Was der Client eigentlch wollte: {request.decode()}")