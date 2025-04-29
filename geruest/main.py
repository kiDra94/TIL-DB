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
    cursor = sqlconn.cursor()
    cursor.execute(q)
    rows = cursor.fetchall()
    return json.dumps(rows) # dumps -> dump string

@app.post("/tils")
def add_new_til(subject, date, descripton):
    sid = "SELECT id FROM subjects WHERE name = {subject}"
    if sid is None:
        sid = cursor.execute("INSERT INTO subjects VALUES(?) RETURNING id", (subject))
    stmt = "INSERT INTO tils (data, descriptions, subject_id) VALUES (?, ?, ?) RETURNING id"
    cursor.execute(stmt, (data, descriptions, sid)) # absicherung gegen SQl-Injections
    return tid

# tils = app.route("/tils")(tils) der aufgeschriebener decorator

with sqlite3.connect("tils.db") as sqlconn:
    app.run(sqlconn)