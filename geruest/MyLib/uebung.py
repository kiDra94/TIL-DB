#Uebung: 

#Erstelle ein Modul "MyLib" mit zewi funktionen "Hallo()" und "Welt()"
#erstelle ein main-Datei und importiere Hallo, um es dann in der Main ausfuehren zu koennen.
#Welt darf nicht importierbar sein, es wird aber von Hallo verwendet

def world():
        return "World"

def hallo():
    return f"Hallo {world()}"