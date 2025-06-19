# traducciones = {
#     "hola": {
#         "en": "hello",
#         "es": "hola"
#     },
#     "patatas": {
#         "en": "potatoes",
#         "es": "patatas"
#     }
# }

traducciones = {
    "en": {
        "hola": "hello",
        "patatas": "potatoes",
        "abrir": "open"
    },
    "es": {
        "hola": "hola",
        "patatas": "patatas",
        "abrir": "abrir"
    }
}

def traduce(texto: str, lang="en"):
    texto_minus = texto.lower()

    # if lang in traducciones:
    #     if texto_minus in traducciones[lang]:
    #         return traducciones[lang][texto_minus]
    #     return f"No tenemos la traducción de {texto_minus}"
    # return f"No tenemos traducciones para el {lang}"

    if lang not in traducciones:
        return f"No tenemos traducciones para el {lang}"

    if texto_minus not in traducciones[lang]:
        return f"No tenemos la traducción de {texto_minus}"

    return traducciones[lang][texto_minus]
