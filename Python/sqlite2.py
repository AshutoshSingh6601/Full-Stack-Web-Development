import sqlite3
with sqlite3.connect('db.sqlite3') as conn:
    command = "SELECT year,star,name FROM Movie where year = 2023 "
    fetch = conn.execute(command)
    for movies in fetch:
        print(movies)
    