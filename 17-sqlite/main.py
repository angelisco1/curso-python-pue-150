import sqlite3

DB_PATH = "ingredients.db"

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
   	name TEXT NOT NULL,
	price REAL NOT NULL
);
""")

conn.commit()

def insert(ingrediente):
    cursor.execute("INSERT INTO ingredients (name, price) VALUES (?, ?)", (ingrediente["name"], ingrediente["price"]))
    conn.commit()

# insert({
#     "name": "Pimiento rojo",
#     "price": 0.20
# })

def get_all():
    cursor.execute("SELECT * FROM ingredients")
    rows = cursor.fetchall()
    for row in rows:
        print("---")
        print(f"id: {row["id"]}")
        print(f"name: {row["name"]}")
        print(f"price: {row["price"]}")

# get_all()

def get_by_id(id):
    cursor.execute("SELECT * FROM ingredients WHERE id = ?", (id,))
    row = cursor.fetchone()
    print(f"id: {row["id"]}")
    print(f"name: {row["name"]}")
    print(f"price: {row["price"]}")

get_by_id(2)

