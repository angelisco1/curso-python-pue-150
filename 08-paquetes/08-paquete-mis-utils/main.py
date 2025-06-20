import mis_utils.traductor
import mis_utils.traductor as mut
from mis_utils.traductor import traduce as tr

from mis_utils import suma, traduce
from mis_utils.operaciones import resta

print(mis_utils.traductor.traduce("hola", "en"))
print(mis_utils.operaciones.resta(1, 2))
print(mut.traduce("patatas", "es"))
print(tr("abrir"))

print(suma(1, 2))
print(traduce("no existe", "de"))


