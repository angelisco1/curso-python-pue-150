
def logger(metodo_a_decorar):
    def wrapper(*args, **kwargs):
        print(f"Se está llamando a {metodo_a_decorar.__name__}")
        print(f"ARGS: {args}")
        return metodo_a_decorar(*args, **kwargs)
    return wrapper

class Persona:
  def __init__(self, nombre, apellidos):
      self.nombre = nombre
      self.apellidos = apellidos

  @logger
  def get_nombre_completo(self):
    return f"{self.nombre} {self.apellidos}"

  def __repr__(self):
      return f"Persona => {self.nombre}"

charly = Persona('Charly', 'Falco')
print(charly.get_nombre_completo())