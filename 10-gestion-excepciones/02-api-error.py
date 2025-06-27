class APIError(Exception):
    def __init__(self, status_code):
        mensaje = APIError.get_mensaje_del_codigo(status_code)
        super().__init__(f"[{status_code}] {mensaje}")
        self.codigo = status_code

    @staticmethod
    def get_mensaje_del_codigo(codigo):
        mensajes_por_codigo = {
            400: "los datos enviados no son correctos",
            401: "las credenciales no son válidas",
            404: "no hemos encontrado lo que buscas",
        }
        return mensajes_por_codigo[codigo] if codigo in mensajes_por_codigo else "ha ocurrido un error"


usuarios = [
    { "email": "angel@gmail.com", "password": "1234", "nombre": "Ángel" },
    { "email": "octavia@gmail.com", "password": "1234", "nombre": "Octavia" },
]

def get_usuario(credenciales):
    email, password = credenciales.values()

    if "@" not in email:
        # print("Error 400: los datos enviados no son correctos")
        raise APIError(400)

    usuario_buscado = None
    for usuario in usuarios:
        if usuario["email"] == email and usuario["password"] == password:
            usuario_buscado = usuario
            break

    if not usuario_buscado:
        raise APIError(404)
        # print("Error 404: no hemos encontrado el usuario")

    return usuario_buscado


credenciales = {
    "email": "angel@gmail.com",
    "password": "1234"
}

print(get_usuario(credenciales))

try:
    credenciales = {
        "email": "angelgmail.com",
        "password": "1234"
    }
    print(get_usuario(credenciales))
except APIError as e:
    print(e)

try:
    credenciales = {
        "email": "paco@gmail.com",
        "password": "1234"
    }
    print(get_usuario(credenciales))
except APIError as e:
    print(e)