import json
import socket

def get_datos(dominio, puerto, ruta):
    cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente_tcp.connect((dominio, puerto))
        print("Se ha establecido la conexión")

        peticion = f"GET {ruta} HTTP/1.1\r\n"
        peticion += f"Host: {dominio}\r\n"
        peticion += "Connection: close\r\n"
        peticion += "\r\n"

        print(peticion)

        cliente_tcp.send(peticion.encode("utf-8"))

        response = b""
        while True:
            datos = cliente_tcp.recv(1024)
            if not datos:
                break
            response += datos

        respuesta = response.decode("utf-8")

        print(respuesta)
        print(type(respuesta))
        # print("******")
        # print(len(respuesta.split("\r\n\r\n")))
        # print("******")

        cuerpo_respuesta = respuesta.split("\r\n\r\n")[1]
        return json.loads(cuerpo_respuesta)

    except Exception as e:
        print(e)
        print("No se ha podido establecer la conexión")
    finally:
        cliente_tcp.close()


# get_datos("www.google.com", 80, "/")
ingredientes = get_datos("localhost", 3000, "/ingredientes")
print(ingredientes)

for i in ingredientes:
    print(i["precio"])

lista_precios = [i["precio"] for i in ingredientes]
dict_precios = {
    "precios": lista_precios
}

with open("lista-precios.json", "w") as file:
    # json_precios = json.dumps(dict_precios, indent=4)
    # file.write(json_precios)
    json.dump(dict_precios, file, indent=4)