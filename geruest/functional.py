from functools import reduce

def addieren(a, b):
    return a + b

# Funktion einer anderen zuweisen
x = addieren
x(2, 3)

# Funktion als Parameter übergeben
reduce(addieren, [1, 2, 3, 4], 0)

# Funktion, die eine Funktion zurückgibt
def plusn(n):
    def addieren(a):
        return a + n
    return addieren

plus8 = plusn(8)
plus7 = plusn(7)

plus8(10)
plus7(10)

plusn(8)(10)


def log(function):
    def inner():
        print("Vorher")
        function()
        print("Nachher")
    return inner

def hallo():
    print("Hallo")

hallo = log(hallo)
hallo()

@log
def seas():
    print("Seas")