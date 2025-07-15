import tkinter as tk
from tkinter import ttk, colorchooser

from markdown_it.rules_block import list_block

ventana = tk.Tk()
ventana.geometry("1024x690")
ventana.title("Apúntate a la newsletter")

usuarios = [
    { "id": 1, "email": "angel@gmail.com", "password": "1234", "nombre_completo": "Ángel Villalba" },
    { "id": 2, "email": "cfalco@gmail.com", "password": "1234", "nombre_completo": "Charly Falco" },
]

label_categorias = tk.Label(ventana, text="Categorías:")

var_ciencia = tk.IntVar(value=1)
var_tecnologia = tk.IntVar()
var_deporte = tk.IntVar()
var_economia = tk.IntVar()

check_ciencia = tk.Checkbutton(ventana, text="Ciencia", variable=var_ciencia)
check_tecnologia = tk.Checkbutton(ventana, text="Tecnología", variable=var_tecnologia)
check_deporte = tk.Checkbutton(ventana, text="Deporte", variable=var_deporte)
check_economia = tk.Checkbutton(ventana, text="Economía", variable=var_economia)


label_categorias.grid(row=0, column=0)
check_ciencia.grid(row=1, column=0)
check_tecnologia.grid(row=1, column=1)
check_deporte.grid(row=1, column=2)
check_economia.grid(row=1, column=3)


var_lang = tk.StringVar(value="es")

radio_es = tk.Radiobutton(ventana, text="Español", variable=var_lang, value="es")
radio_en = tk.Radiobutton(ventana, text="Inglés", variable=var_lang, value="en")
radio_it = tk.Radiobutton(ventana, text="Italiano", variable=var_lang, value="it")

label_lang = tk.Label(ventana, text="Lenguaje de las noticias:")
label_lang.grid(row=2, column=0)
radio_es.grid(row=3, column=0)
radio_en.grid(row=3, column=1)
radio_it.grid(row=3, column=2)


label_plan = tk.Label(ventana, text="Selecciona el plan:")
desplegable_plan = ttk.Combobox(ventana, values=[
    "Free (1 email/semana)",
    "Premium (1 email/dia)",
    "Premium+ (1 email de cada categoria/dia)"
])

label_plan.grid(row=4, column=0)
desplegable_plan.grid(row=4, column=1)


listbox_tema_color = tk.Listbox(ventana, selectmode=tk.SINGLE)
temas = ["dark", "light", "dark one", "lemon one"]
for tema in temas:
    listbox_tema_color.insert(tk.END, tema)

label_tema_color = tk.Label(ventana, text="Elige el tema de los emails:")

label_tema_color.grid(row=5, column=0)
listbox_tema_color.grid(row=5, column=1)

def choose_color():
    color_rgb, color_hexadecimal = colorchooser.askcolor(color="#")
    print(f"Color: {color_hexadecimal}")

btn_color = tk.Button(ventana, text="Selecciona un color:", command=choose_color)
btn_color.grid(row=6, column=0)


btn = tk.Button(ventana, text="Suscribete")
btn.grid(row=7, column=0)

def subscribe(event):
    print(var_ciencia.get())
    print(var_tecnologia.get())
    print(var_deporte.get())
    print(var_economia.get())

    print(var_lang.get())

    print(desplegable_plan.get())

    for i in listbox_tema_color.curselection():
        print(listbox_tema_color.get(i))

btn.bind("<Button-1>", subscribe)


ventana.mainloop()