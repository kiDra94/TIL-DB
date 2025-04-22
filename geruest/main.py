from bulmeapi import App
import json
import sqlite3

app = App()

#http://localhost:8080/tils
@app.route("/tils")
def tils(conn):
    q = """SELECT ts.id, ts.date, ts.desc, s.name subject
    FROM tils ts
    LEFT JOIN  subjects s ON ts.subject_id = s.id
    """
    cursor = conn.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
    return json.dumps(rows)


# tils = app.route("/tils")(tils) der aufgeschriebener decorator

with sqlite3.connect("tils.db") as conn:
    app.run(conn)