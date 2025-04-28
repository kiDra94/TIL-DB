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

    def run(self, conn, host="localhost", port="8080"):
        with HttpServer(host, port) as server:
            while True:
                conn = server.accept()
                request = server.receive(conn)
                server.handle_request(request)
        data = conn.recv(1024).decode()
        # do smth with data
        conn.close()