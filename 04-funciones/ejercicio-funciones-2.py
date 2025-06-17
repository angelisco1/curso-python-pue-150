# Ejercicio 2
# Crear una función que dada una lista de series (cada serie tiene titulo, capitulos, finalizada,
# capitulos_vistos) nos devuelva las series que han finalizado pero todavía no hemos terminado de ver

series = [
    {
        "titulo": "Vikings",
        "finalizada": True,
        "capitulos": 100,
        "capitulos_vistos": 97
    },
    {
        "titulo": "Game of thrones",
        "finalizada": True,
        "capitulos": 80,
        "capitulos_vistos": 80
        # "capitulos_vistos": 60
    },
    {
        "titulo": "House of the dragon",
        "finalizada": False,
        "capitulos": 20,
        "capitulos_vistos": 19
    }
]

def get_finalizadas_sin_ver(lista_series):
    series_por_terminar = []

    for serie in lista_series:
        if serie["finalizada"] and serie["capitulos"] > serie["capitulos_vistos"]:
            series_por_terminar.append(serie)

    return series_por_terminar

series_para_terminar = get_finalizadas_sin_ver(series)

for serie in series_para_terminar:
    print(f"Te quedan {serie["capitulos"] - serie["capitulos_vistos"]} capítulos por ver de {serie["titulo"]}")