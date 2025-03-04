import sqlite3
from pprint import pprint

CONNECTION = sqlite3.connect("til.db")
def select(conn):
    return [
        {
            "id" : row[0],
            "date" : row[1],
            "desc" : row[2],
            "subject" : row[3]
        }
        for row in conn.cursor().execute("SELECT * FROM til;")
    ]
pprint(select(CONNECTION))
'''
#server sollte so funktionieren!!!

def handle():
    if request.method == "GET":
        # SELECT * FROM
    elif request.method == "PUT":
        # INSERT INTO
    elif request.method == "POST":
        # UPDATE .... SER
    elif request.method == "DELETE":
        # DELETE FROM
while True:
    request = conn.recive()
    response = handle(request)
    conn.send(response)
'''
CONNECTION.close()