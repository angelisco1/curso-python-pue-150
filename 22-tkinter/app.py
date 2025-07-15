import tkinter as tk
from PIL import Image, ImageTk

from docutils.nodes import compound

ventana = tk.Tk()
ventana.geometry("1024x690")
ventana.title("Ejemplo con tkinter")

label = tk.Label(ventana, text="Hola mundo")
label.pack(pady=5)



otro_label = tk.Label(
    ventana,
    text="Bienvenido al curso",
    anchor="center",
    height=10,
    width=20,
    background="white",
    foreground="black"
)
otro_label.pack(pady=5)

# imagen = tk.PhotoImage(file="images/meme-pensando.png")
imagen_redimensionada = Image.open("images/meme-pensando.png").resize((150, 152))
imagen = ImageTk.PhotoImage(imagen_redimensionada)

label_img = tk.Label(
    ventana,
    image=imagen,
    text="Pensando...",
    compound=tk.BOTTOM,
)
label_img.pack()

label00 = tk.Label(ventana, text="Este en la esquina 0, 0")
label00.place(x=0, y=0)

def saludar():
    nombre = campo_texto.get()
    print(f"Hola {nombre}")
    tk.Label(ventana, text=f"Hola {nombre}").pack()
    campo_texto.insert(tk.END, "!")
    print(campo_pw.get())

emoji_redimensionado = Image.open("images/emoji-saludar.png").resize((20, 20))
emoji = ImageTk.PhotoImage(emoji_redimensionado)
boton1 = tk.Button(
    ventana,
    text="Saludar (disabled)",
    command=saludar,
    state=tk.DISABLED,
    disabledforeground="yellow",
    image=emoji,
    compound=tk.RIGHT
)
boton1.pack()


def habilita_boton1():
    boton1.config(text="Saludar", state=tk.NORMAL)

boton2 = tk.Button(ventana, text="Habilitar saludar", command=habilita_boton1, state=tk.NORMAL,
                   disabledforeground="yellow")
boton2.pack()

def reset_entry():
    campo_texto.delete(0, tk.END)

boton_reset = tk.Button(ventana, text="Resetear campo de texto", command=reset_entry)
boton_reset.pack()

campo_texto = tk.Entry(ventana)
campo_texto.pack()

campo_pw = tk.Entry(ventana, show="*")
campo_pw.pack()


def on_enter(event):
    print(f"Event: {event}")
    saludar()

campo_texto.bind("<Return>", on_enter)



# campo_texto.insert(0, "!")

ventana.mainloop()