import sqlite3

DB_PATH = "ingredients.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	name TEXT NOT NULL,
	price REAL NOT NULL
);
""")

conn.commit()

ingrediente = {
    "name": "Tomate",
    "price": 1.10
}
cursor.execute("INSERT INTO ingredients (name, price) VALUES (?, ?)", (ingrediente["name"], ingrediente["price"]))
conn.commit()

