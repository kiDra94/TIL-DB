from bulmeapi import App
import json
import sqlite3

app = App()

#http://localhost:8080/tils
@app.get("/tils")
def tils(sqlconn):
    q = """SELECT ts.id, ts.date, ts.desc, s.name subject
    FROM tils ts
    LEFT JOIN  subjects s ON ts.subject_id = s.id
    """
    cursor = sqlconn.cursor() #curser kann man sich als einen blinkende
    # der denn beginn von der zb Zeile in Tabelle markiert
    cursor.execute(q)
    rows = cursor.fetchall() # cursor arbeiete erst ab hier
    return json.dumps(rows) # dumps -> dump string

@app.post("/tils")
def add_new_til(subject, date, descripton):
    """
    data koente so auscchauen
    data = {
        'date': '2025-01-01',
        'topic': 'Silvester!!!',
        'description': 'Nix gelernt. JedeJahr das gleiche!'
    }
    """
    sid = "SELECT id FROM subjects WHERE name = {subject}"
    cursor = sqlconn.cursor() 

    # absicherung gegen SQl-Injections mit Platzhalter (Prepeared-stmt)
    if sid is None:
        sid = cursor.execute("INSERT INTO subjects VALUES(?) RETURNING id", (subject))
        #VALUES(?) auch ein platzhalter aber nicht schoen
    stmt = "INSERT INTO tils (date, descriptions, subject_id) VALUES (:date, :descriptions, :subject_id) RETURNING id" 
    # :data, :description, :subject_id sind patzhalter

    row = cursor.execute(stmt, (date, descriptions, sid)).fetchone()
    #fetchone da ein inster nur eine zeile ist
    insterted_id = row[0] if row else None # sollte einen id haben da -> RERTURNING id
    conn.commit() #
    return tid

# tils = app.route("/tils")(tils) der aufgeschriebener decorator

""" MINIMUM ZUM WISSEN
eine conncet funktion bekommt eine gultige DB datei
curser wird in der connection erzeugt
curser fuert abfrage aus
bekommt einen generator (ist iterierbar) zurueck

import sqlite3

with sqlite3.connect([pfad zuer datei]) as conn:
    cursor = conn.cursor()
    cursor.execuete('SELECET * FROM til')
    for row in cursor.fetchall():
        print(row)

man sollte das gleiche fuer delete update insert wissen
"""
with sqlite3.connect("tils.db") as sqlconn:
    app.run(sqlconn)

# so stellt man die verbindung mit der DB her 
# close passiert wenn die WITH [kontextmanager] fertig ist
"""
conn = sqlite3.connect('tils.db')
# TODO
conn.close()
#fast das gleiche wie unten, untere methode beforzugt
"""   