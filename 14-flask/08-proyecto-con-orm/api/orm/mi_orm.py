# import sqlite3
from ..database import get_conn

# Ingredient.all()
# -> SELECT * FROM ingredients
#
# Persona.all()
# -> SELECT * FROM personas

# Ingredient.where(id=1, category="especia")
# -> SELECT * FROM ingredients WHERE id=1 AND categoria=especia

# tomate = Ingrediente("Tomate", 0.23)
# tomate.save()
# -> INSERT INTO ingredients (name, price) VALUES (?, ?)


# Ingredient.create_table()

class Field:
    def __init__(self, type_field, primary_key=False):
        self.name = None
        self.type_field = type_field
        self.primary_key = primary_key

        
class StringField(Field):
    def __init__(self, primary_key=False):
        super().__init__("TEXT", primary_key)

class IntField(Field):
    def __init__(self, primary_key=False):
        super().__init__("INTEGER", primary_key)

class FloatField(Field):
    def __init__(self, primary_key=False):
        super().__init__("REAL", primary_key)




class MetaModel(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return super().__new__(cls, name, bases, attrs)

        # fields = {
        #     "id": {
        #         pk: True,
        #         type_field: INTEGER,
        #     }
        # }
        fields = {}
        primary_key = False

        print(f"------- {name} ------")
        for key, value in list(attrs.items()):
            print(f"key: {key}, value: {value}")

            if isinstance(value, Field):
                value.name = key
                fields[key] = value
                if value.primary_key:
                    if primary_key:
                        raise Exception("Ya existe una primary key")
                    primary_key = True
                del attrs[key]

        attrs["fields"] = fields
        attrs["primary_key"] = primary_key
        attrs["table"] = name.lower() + "s"

        return super().__new__(cls, name, bases, attrs)


class Model(metaclass=MetaModel):
    def __init__(self, **kwargs):
        print(f"Fields: {self.fields}")
        print(f"Tabla: {self.table}")
        print(f"PK: {self.primary_key}")
        print(kwargs)
        for key in self.fields:
            setattr(self, key, kwargs.get(key))


    @classmethod
    def all(cls):
        entities = []
        sql = f"SELECT * FROM {cls.table}"
        cursor = cls.__execute_sql(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Row: {row}")
            entities.append(cls(**row))
        return entities

    def save(self):
        values = [getattr(self, key) for key in self.fields.keys()]
        placeholders = ", ".join(["?"] * len(values))
        sql = f"INSERT INTO {self.table} ({", ".join(self.fields)}) VALUES ({placeholders})"
        cursor = self.__execute_sql(sql, values)
        setattr(self, "id", cursor.lastrowid)
        return self

    @classmethod
    def create_table(cls):
        field_defs = []
        for name, field in cls.fields.items():
            column_def = f"{name} {field.type_field}"
            if field.primary_key:
                column_def += " PRIMARY KEY AUTOINCREMENT"
            else:
                column_def += " NOT NULL"
            field_defs.append(column_def)

        sql = f"CREATE TABLE IF NOT EXISTS {cls.table} ({", ".join(field_defs)})"
        cls.__execute_sql(sql)


    @classmethod
    def __execute_sql(cls, sql, params=None):
        # conn = sqlite3.connect("pruebas.db")
        # conn.row_factory = sqlite3.Row
        conn = get_conn()
        cursor = conn.cursor()

        print(f"SQL = {sql}")
        cursor.execute(sql, params or [])

        conn.commit()
        return cursor



if __name__ == "__main__":

    class Usuario(Model):
        id = IntField(primary_key=True)
        name = StringField()
        #
        # tabla = "usuarios"
        # campos = [id, name]
        # primary_key = True



    class Ingrediente(Model):
        id = IntField(primary_key=True)
        name = StringField()
        price = FloatField()
        categoria: str




    # Ingrediente.create_table()
    # Usuario.create_table()


    # angel = Usuario(id=1, name="Ángel")
    # charly = Usuario(name="Charly")
    # angel.save()
    # charly.save()

    # p_verde = Ingrediente(name="Pimiento verde", price="0.35")
    # p_rojo = Ingrediente(name="Pimiento rojo", price="0.25")
    # p_verde.save()
    # p_rojo.save()

    # print("****")
    # print("****")
    # print(Usuario.all())
    # print("****")
    # print("****")
    # print(Ingrediente.all())



