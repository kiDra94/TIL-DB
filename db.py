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
CONNECTION.close()