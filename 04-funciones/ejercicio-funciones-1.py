# Ejericio 1:
# Crear una función que dada una lista de usuarios conectados y un usuario, se añade el usuario a la lista de
# conectados en caso de que no lo estuviese previamente

usuario1 = "Charly"
usuario2 = "Mike"
usuario3 = "Octavia"

usuarios_conectados = []

def conectar_usuario(usuario):
    # if usuario not in usuarios_conectados:
    #     usuarios_conectados.append(usuario)
    #     print(f"Se ha conectado {usuario}")
    #     return True
    # else:
    #     print(f"El usuario {usuario} ya estaba conectado")
    #     return False
    if usuario in usuarios_conectados:
        print(f"El usuario {usuario} ya estaba conectado")
        return False

    usuarios_conectados.append(usuario)
    print(f"Se ha conectado {usuario}")
    return True

usuario_registrado = conectar_usuario(usuario1)
usuario_registrado = conectar_usuario(usuario1)
usuario_registrado = conectar_usuario(usuario2)
usuario_registrado = conectar_usuario(usuario3)
usuario_registrado = conectar_usuario(usuario2)
# if usuario_registrado:
#     enviar_email_bienvenida(usuario1)