import json
from pathlib import Path
import sqlite3
data = json.loads(Path("movies.json").read_text())
print(data )
with sqlite3.connect("db.sqlite3") as conn:
    command = "INSERT INTO Movie VALUES(?, ?, ?)"
    for movie in data:
        conn.execute(command,tuple(movie.values()))
        conn.commit()