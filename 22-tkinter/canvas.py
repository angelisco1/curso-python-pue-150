import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1024x690")
ventana.title("Paint")


canvas = tk.Canvas(ventana, background="white", width=1000, height=400)
canvas.pack()

id_line = canvas.create_line(0, 0, 1000, 400, fill="blue")
id_rectangle = canvas.create_rectangle(600, 200, 1000, 400, fill="yellow")
id_oval = canvas.create_oval(100, 60, 500, 200, fill="orange")


def mover_circulo():
    canvas.move(id_oval, 100, 200)

ventana.after(2500, mover_circulo)


ventana.mainloop()