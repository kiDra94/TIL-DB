def hallo():
    print("Hallo Welt")

def hello():
    print("Hello World")

def seas():
    print("Griaß di wöd")
    
def szia():
    print("Szia Vilag")

paths = {
    "de": hallo,
    "en": hello,
    "at": seas,
    "hu": szia
}

while True:
    path = input("Which greeting: ")
    paths[path]()