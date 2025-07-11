import logging

print("Un mensaje")

logging.basicConfig(level=logging.INFO, filename="mi-app.log")

logging.warning("Un mensaje")
logging.debug("Un mensaje")
logging.info("Un mensaje")

logger1 = logging.getLogger("log1")
logger2 = logging.getLogger("log2")

logger1.setLevel(logging.ERROR)
# logger2.setLevel(logging.INFO)


logger1.error("Errores everywhere...")
logger1.critical("Este mensaje se autodestruira en 1 min con todo lo que haya a menos de 1KM. Corre.")
logger1.info("Hoy hace fresquito")

logger2.info("Hoy hace fresquito. A ver si sigue así.")

console_handler = logging.StreamHandler()
logger2.addHandler(console_handler)

logger2.info("Hoy hace fresquito. A ver si sigue así.")

file_handler = logging.FileHandler(filename="errors.log")
file_handler.setLevel(logging.INFO)

formato1 = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s>%(funcName)s>Nº%(lineno)d - %(message)s")
file_handler.setFormatter(formato1)

logger1.addHandler(file_handler)

logger1.error("Errores everywhere...")
logger1.critical("Este mensaje se autodestruira en 1 min con todo lo que haya a menos de 1KM. Corre.")
logger1.info("Hoy hace fresquito")


def sumar(n1, n2):
    suma = n1 + n2
    logger1.info(f"La suma de {n1} y {n2} es {suma}")
    return suma

sumar(1, 2)