import time
from configparser import ConfigParser

config = ConfigParser()
config.read("ajustes.ini")

print(config.sections())
print(config.options("theme"))

# option = "code"
option = "format"
if config.has_section("currency") and config.has_option("currency", option):
    print(f"Code: {config["currency"][option]}")
else:
    print(f"No existe la opción '{option}' en la sección 'currency'")


print(type(config["animations"]["enabled"]))
print(type(bool(config["animations"]["enabled"])))
print(type(config.getboolean("animations", "enabled")))
print(type(config["animations"]["duration"]))
print(type(int(config["animations"]["duration"])))
print(type(config.getint("animations", "duration")))


print(config.get("api", "basePath"))


# Escribir un archivo INI

config = ConfigParser()
config["pagination"] = {
    "limit": "10"
}
config["sort"] = {
    "order": "asc"
}

with open("ajustes-api.ini", "w") as file:
    config.write(file)


time.sleep(4)

config["pagination"]["limit"] = "5"
with open("ajustes-api.ini", "w") as file:
    config.write(file)
