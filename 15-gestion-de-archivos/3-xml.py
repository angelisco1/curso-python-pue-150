import xml.etree.ElementTree as ET

ingrediente_chorizo = """<ingredient>
        <id>18</id>
        <name>Chorizo</name>
        <price currency="EUR">1.85</price>
    </ingredient>""".strip()

ingrediente_patata = """<ingredient>
        <id>37</id>
        <name>Patata</name>
        <price currency="EUR">0.85</price>
    </ingredient>""".strip()


lista_ingredientes = f"""
<ingredients>
    {ingrediente_chorizo}
    {ingrediente_patata}
</ingredients>
"""

print(lista_ingredientes)

arbol = ET.fromstring(ingrediente_chorizo)
print(arbol.tag)
print(arbol.text)

nodo_name = arbol.find("name")
print(nodo_name.text)
nodo_name.text = "Carne"
print(nodo_name.text)

nodo_price = arbol.find("price")
print(nodo_price.attrib)

arbol = ET.fromstring(lista_ingredientes)
ingredientes = arbol.findall("ingredient")
print(ingredientes)
print(ingredientes[1].find("name").text)

nombres_ingredientes = arbol.findall("ingredient/name")
print(nombres_ingredientes)


# Creación de un XML
raiz = ET.Element("pizza")

nodo_name = ET.SubElement(raiz, "name")
nodo_name.text = "BBQ"

nodo_price = ET.SubElement(raiz, "price", { "currency": "EUR" })
nodo_price.text = "7.99"

nodo_ingredientes = ET.SubElement(raiz, "ingredients")

ingredientes = [
    { "id": 1, "name": "Salsa BBQ", "price": 0.15 },
    { "id": 2, "name": "Carne picada", "price": 1.25 },
    { "id": 3, "name": "Queso", "price": 0.75 },
    { "id": 4, "name": "Bacon", "price": 1.0 },
]

for ing in ingredientes:
    nodo_ingrediente = ET.SubElement(nodo_ingredientes, "ingredient")
    id = ET.SubElement(nodo_ingrediente, "id")
    id.text = str(ing["id"])
    name = ET.SubElement(nodo_ingrediente, "name")
    name.text = ing["name"]
    price = ET.SubElement(nodo_ingrediente, "price", { "currency": "EUR"})
    price.text = str(ing["price"])


pizza_bbq = ET.ElementTree(raiz)
ET.indent(pizza_bbq, space="  ", level=0)
pizza_bbq.write("archivos/bbq.xml", encoding="UTF-8")


# Cargar un XML
pizzaiola = ET.parse("archivos/pizzaiola.xml")
for name in pizzaiola.findall("ingredients/ingredient/name"):
    print(name.text)

prices = []
for price in pizzaiola.findall("ingredients/ingredient/price"):
    prices.append(float(price.text))

precio_pizzaiola = pizzaiola.find("price")
ganancias = float(precio_pizzaiola.text) - sum(prices)
print(f"Con la pizza Pizzaiola ganas: {ganancias:.2f}€")
