from flask import current_app
import sqlite3
import os

DB_PATH = "api/data/ingredients.db"

def get_conn():
    conn = sqlite3.connect(os.getenv("DB_PATH"))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
    """)

    conn.commit()

    num_ingredients = cursor.execute("SELECT COUNT(*) FROM ingredients").fetchone()[0]
    if num_ingredients == 0:
        cursor.executemany("INSERT INTO ingredients (name, price) VALUES (?, ?)", [
            ("Pimiento verde", 0.25),
            ("Pimiento rojo", 0.25),
            ("Cebolla", 0.35)
        ])
        conn.commit()

    conn.close()