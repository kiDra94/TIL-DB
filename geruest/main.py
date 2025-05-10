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
def add_new_til(sqlconn, subject, date, descripton):
    """
    data koente so auscchauen
    data = {
        'date': '2025-01-01',
        'topic': 'Silvester!!!',
        'description': 'Nix gelernt. JedeJahr das gleiche!'
    }
    """
    sid_stmt = "SELECT id FROM subjects WHERE name = {:subject}"
    cursor = sqlconn.cursor() 
    sid = cursor.execuete(sid_stmt, (subject)).fetchone()

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
    return insterted_id

@app.put("/tils")
def update_til(sqlconn, subject, date, description, id):
    cursor = sqlconn.cursor()

    sid_stmt = "SELECT id FROM subjects WHERE name = {:subject}"
    cursor = sqlconn.cursor() 
    sid = cursor.execuete(sid_stmt, (subject)).fetchone()
    if sid is None:
        sid = cursor.execute("INSERT INTO subjects VALUES({:subject}) RETURNING id")
    
    check_id_stmt = "SELECT id FROM tils WHERE id = {:id}"
    cid = cursor.execuete(check_id_stmt, (id, ))
    if cid is None:
        sqlconn.close()
        return "ERROR unknown til"
    else:
        stmt = "UPDATE tils SET subject = {:subject}, date = {:date}, description = {:description} WHERE id = {:id}"
        curser.execuete(stmt, (id, subject, date, description))
        sqlconn.commit()

        get_new_til_stmt = """SELECT ts.id, ts.date, ts.desc, s.name subject
                            FROM tils ts
                            LEFT JOIN  subjects s ON ts.subject_id = s.id"""

        new_data = cursor.execute(get_new_til_stmt, (id, subject, date, description)).fetchone()
        sqlconn.close()

    return ("Updateted TIL", json.dumps(new_data))

@app.delete("/tils")
def delete_til(sqlconn, id):
    cursor = sqlconn.cursor()

    check_id_stmt = "SELECT id FROM tils WHERE id = {:id}"
    cid = cursor.execuete(check_id_stmt, (id, ))
    if cid is None:
        sqlconn.close()
        return "ERROR unknown til"
    else:
        get_data_befor_delete_stmt = """SELECT ts.id, ts.date, ts.desc, s.name subject
                                        FROM tils ts
                                        LEFT JOIN  subjects s ON ts.subject_id = s.id"""
        data_befor_delete = cursor.execuete(get_data_befor_delete_stmt, (id, subject, date, description)).fetchone

        stmt = "DELETE FROM tils where id = {:id}"
        cursor.execuete(stmt, (id,))
        sqlconn.commit()
        sqlconn.close()

    return ("DELETED data", json.dumps(data_befor_delete))
        

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