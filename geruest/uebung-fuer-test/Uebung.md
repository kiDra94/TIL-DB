applicants
    id
    first
    state_id

states
    id
    name

## Aufgabe 1

Erstelle die DB (CREATE TABLE)

CREATE TABLE applicants{
    id INTEGER PRIMARY AUTOINCREMENT,
    state_id INTEGER NOT NULL
    first VARCHAR(40) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
}

CREATE TABLE states{
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(40) NOT NULL
}

## Aufgabe 2

Schriebe eine Abfrage, die eine Liste aller Bewerber
mit ihrem Bewerbungsstatus ausgibt

SELECT * FROM applicants as a
LEFT JOIN states as s ON  a.state_id = s.id;

## Aufgabe 3

Schriebe ein python-Programm, das eine Liste aller abgehlenten Bewerber
aus der Konsole ausgibt

import sqlite3

with sqlite3.connect(../applicants.db) as conn:
    stmt = """SELECT a.first, s.name FROM applicants as a
              LEFT JOIN states as s ON  a.state_id = s.id
              WHERE s.name LIKE {:statement}"""
    
    cursore = conn.cursor()
    result = cursore.execute(stmt, 'Abgehelent')
    for row in result.fetchall():
        print(row)

## Aufgabe 4

Schreibe eine Klasse, die den State von Bewerbern aktualiesiert

```
@sql.update({"state": "reject"})
def applicants():
    return (1, 7, 23, 76)
```

Class Sql:
    
    def update(self, data, conn):
        def decorator(func):
            cursor = conn.cursor()
            stmt = "UPDATE applicants SET state = {:new_state} WHERE id = {:id}"
            ids = func()
            for i in ids:
                curosor.execute(stmt, data[1], i)
                cursor.commit()
            return cursors.execute("SELECT * FROM applicants WHERE id IN {:ids}", ids).fetchall()
        return decorator

