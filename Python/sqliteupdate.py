import sqlite3

with sqlite3.connect('db.sqlite3') as conn:
    command = "UPDATE Movie set star = 'srk' where name = 'lion'"
    conn.execute(command)
    conn.commit()