import socket

class HttpServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def __enter__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Server läuft auf {self.host}:{self.port}")
        return self

    def __exit__(self):
        self.close()
        print("Server gestoppt")

    def close(self):
        if self.socket:
            self.socket.close()

    def accept(self):
        conn, _ = self.socket.accept()
        return conn
    
    def receive(self, conn):
        return conn.recv(1024).decode()
    
    def handle_request(self, request):
        lines = request.split("\r\n")
        method, path, _ = lines[0].split(" ") #z.B GET /til
        headers = {} # BSP fuer Header https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header
        for line in lines[1:]:
            if line.strip() == "":
                continue
            key, val =  line.split(": ", 1) # splitet nur nach dem ersten ': '
            headers.setdefault(key.strip(), val.strip()) 

        if method == "GET":
            return self.handle_get_request(self, path, headers, request)
        elif method == "put":
            return self.handle_get_request(self, path, headers, request)
        else:
            raise Exception("TO DO: impelement!")

        return method, path, headers

    # wichtig das der return gelich ausschaut, da dies in der handle_request
    # nicht funktionieren wuerden
    def handle_get_request(self, path, headers, request):
        return "GET", path, headers, None    
    
    def handle_put_request(self, path, headers, request):
        return "GET", path, headers, None 

    def handle_post_request(self, path, headers, request):
        return "POST", path, headers, None

    def handle_delete_request(self, path, headers, request):
        return "DELETE", path, headers, None

if __name__ == "__main__":
    server = HttpServer("localhost", 8080)

    print(server.host)
    exit()

    HOST = "localhost"
    PORT = 8080

    response = "HTTP/1.1 200 OK\r\n"
    response += "Content-Type: text/json\r\n"
    response += "Connection: close\r\n\r\n"
    response += "{'vorname': 'Hansi', 'nachname': 'Huber'}"

    def handle_request(request):
        lines = request.split("\r\n")
        method, path, _ = lines[0].split(" ")
        if method == "GET" and path == "til":
            # SELECT * FROM til
            pass

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Server is listening to {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            print(f"Client {addr} is requesting something.")

        with conn:
                handle_request(conn.recv(1024))
                conn.sendall(response.encode())