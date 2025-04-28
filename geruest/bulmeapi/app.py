from .server import HttpServer
# App soll den HttpServer intern verwenden

class App:
    def __init__(self): # Konstruktor
        self.routes = {} # self.routes Datentyp -> Dict

    def route(self, path):
        def inner(func):
            self.routes[path] = func
            return func
        return inner

    def handle_request(self, request, server, conn):
        method, path, headers, body = server.handle_request(request) #kriegt nur die antwort von der Http aber macht es nicht sleber

    def run(self, conn, host="localhost", port="8080"):
        # der Clienet bekommt jetzt eine antwort
        with HttpServer(host, port) as server:
            while True:
                conn = server.accept()
                request = server.receive(conn)
                response = server.handle_request(request)
                conn.send(response.encode())
                conn.close()