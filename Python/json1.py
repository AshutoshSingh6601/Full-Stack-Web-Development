import json
from pathlib import Path 
movies = [
    {"name": "pathan", "year":2023, "star":"skr"},
    {"name": "kgf", "year":2022, "star":"yash"}
]
data = json.dumps(movies)
Path("movies.json").write_text(data)