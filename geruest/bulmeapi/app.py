from .server import HttpServer
# App soll den HttpServer intern verwenden

class App:
    def __init__(self): # Konstruktor
        # self.routes = {} # self.routes Datentyp -> Dict
        self.gets = {}
        self.post = {}

    def route(self, path, dict):
        def inner(func):
            dict[path] = func
            return func
        return inner
    
    #die funktion welche unter dem dekorator stehen, werden in die routen reingeschrieben
    def get(self, path):
        self.route(path,self.get)

    #die funktion welche unter dem dekorator stehen, werden in die routen reingeschrieben    
    def post(self, path):
        self.route(path,self.post)

    def handle_request(self, request, server, sqlconn):
        method, path, headers, body = server.parse_http(request) #kriegt nur die antwort von der Http aber macht es nicht sleber
        if path in self.routes:
            func = self.routes[path]
            result = func(sqlconn) # wird von der main.py returned da die function die def tils ist
            return self.create_respons(result)
        else:
            return self.create_respons("Not found", 404)

    def create_respons(self, content, statuscode=200):
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Content-Length": str(len(content))
        }

        response = f"HTTP/1.1 {statuscode} \r\n"
        for header, value in headers.items():
            response += f"{header}: {value}\r\n"
        response += "\r\n"
        response += content

        return response

    def run(self, host="localhost", port="8080"):
        # der Clienet bekommt jetzt eine antwort
        with HttpServer(host, port) as server:
            while True:
                conn = server.accept()
                request = server.receive(conn)
                response = self.handle_request(request, server, sqlconn)
                conn.send(response.encode())
                conn.close()