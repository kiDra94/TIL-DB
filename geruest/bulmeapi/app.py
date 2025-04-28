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

    def run(self, conn):
        data = conn.recv(1024).decode()
        # do smth with data
        conn.close()