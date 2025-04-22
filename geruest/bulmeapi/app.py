from .server import HttpServer

class App:
    def __init__(self): # Konstruktor
        self.routes = {}

    def route(self, path):
        def inner(func):
            self.routes[path] = func
            return func
        return inner

    def run(self, conn):
        pass