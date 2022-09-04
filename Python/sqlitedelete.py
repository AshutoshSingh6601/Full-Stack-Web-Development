import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    Command = "DELETE FROM movie where year=2022"
    conn.execute(Command)

    conn.commit()