def sag_immer_hallo(function):
    def bla():
        print("Hallo")
        function()
    return bla

@sag_immer_hallo
def welt():
    print("Welt")

@sag_immer_hallo
def vilage():
    print("Vilage")

def addieren(a, b):
    return a + b

def subtrahieren(a, b):
    return a - b

@hallo("/de")
def hallo():
    print("Hallo Welt")
@hallo("/en")
def hello():
    print("Hello World")
@hallo("/at")
def seas():
    print("Griaß di wöd")
@hallo("/hu")  
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