from ..database import get_conn
from ..interfaces import IngredientRepository

DB_PATH = "api/data/ingredients.db"

class IngredientSQLiteRepository(IngredientRepository):


    def get_all(self):
        conn = get_conn()

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ingredients")
        rows = cursor.fetchall()

        conn.close()

        ingredients = []
        for row in rows:
            ingredients.append({
                "id": row["id"],
                "name": row["name"],
                "price": row["price"],
            })

        return ingredients


    def get_by_id(self, id):
        conn = get_conn()

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ingredients WHERE id=?", (id,))
        row = cursor.fetchone()

        conn.close()

        if not row:
            return None

        return {
            "id": row["id"],
            "name": row["name"],
            "price": row["price"],
        }


    def create(self, ingredient):
        conn = get_conn()

        cursor = conn.cursor()
        cursor.execute("INSERT INTO ingredients (name, price) VALUES (?, ?)", (
            # ingredient["name"],
            # ingredient["price"]
            ingredient.name,
            ingredient.price
        ))

        conn.commit()

        created_id = cursor.lastrowid
        ingredient.id = created_id

        conn.close()

        return ingredient


    def update(self, id, ingredient_data):
        conn = get_conn()

        cursor = conn.cursor()
        cursor.execute("UPDATE ingredients SET name=?, price=? WHERE id=?", (
            ingredient_data["name"],
            ingredient_data["price"],
            id,
        ))

        conn.commit()

        conn.close()

        if cursor.rowcount > 0:
            return {**ingredient_data, "id": id}
        return None


    def partial_update(self, id, ingredient_data):
        conn = get_conn()

        cursor = conn.cursor()

        values = []
        fields = []

        if "name" in ingredient_data:
            values.append(ingredient_data["name"])
            fields.append("name=?")

        if "price" in ingredient_data:
            values.append(ingredient_data["price"])
            fields.append("price=?")

        values.append(id)
        # ["name = ?", "price = ?"] -> "name = ?, price = ?"
        cursor.execute(f"UPDATE ingredients SET {", ".join(fields)} WHERE id=?", values)

        conn.commit()

        ingredient = None
        if cursor.rowcount > 0:
            cursor.execute("SELECT * FROM ingredients WHERE id=?", (id,))
            row = cursor.fetchone()
            ingredient = {
                "id": id,
                "name": row["name"],
                "price": row["price"],
            }

        conn.close()
        return ingredient



    def delete(self, id):
        conn = get_conn()

        cursor = conn.cursor()
        cursor.execute("DELETE FROM ingredients WHERE id=?", (id,))
        conn.commit()

        deleted = cursor.rowcount > 0
        conn.close()

        return deleted