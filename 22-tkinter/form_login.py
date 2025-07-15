import tkinter as tk

ventana = tk.Tk()
ventana.geometry("1024x690")
ventana.title("Login")

usuarios = [
    { "id": 1, "email": "angel@gmail.com", "password": "1234", "nombre_completo": "Ángel Villalba" },
    { "id": 2, "email": "cfalco@gmail.com", "password": "1234", "nombre_completo": "Charly Falco" },
]

label_email = tk.Label(ventana, text="Email:")
label_pw = tk.Label(ventana, text="Password:")
entry_email = tk.Entry(ventana)
entry_pw = tk.Entry(ventana, show="*")
button_login = tk.Button(ventana, text="Login")

label_email.grid(row=0, column=0)
entry_email.grid(row=0, column=1)
label_pw.grid(row=1, column=0)
entry_pw.grid(row=1, column=1)
button_login.grid(row=2, column=0, columnspan=2, sticky=tk.W+tk.E)

def on_submit(event):
    email = entry_email.get()
    password = entry_pw.get()

    print(f"Credenciales: ({email}, {password})")
    usuario = next((usuario for usuario in usuarios if usuario["email"] == email and usuario["password"] == password))
    if usuario:
        label_bienvenida.config(text=f"Bienvenido {usuario["nombre_completo"]}")
        mensaje_bienvenida.set(f"Bienvenido {usuario["nombre_completo"]}*")
        otro_label_bienvenida.config(text=f"Bienvenido {usuario["nombre_completo"]}")


label_bienvenida = tk.Label(ventana, text= "Bienvenido <sin nombre>")
label_bienvenida.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

mensaje_bienvenida = tk.StringVar(value="Bienvenido <sin nombre>*")

label_bienvenida_dinamica = tk.Label(ventana, textvariable=mensaje_bienvenida)
label_bienvenida_dinamica.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)

otro_label = tk.Label(ventana, textvariable=mensaje_bienvenida)
otro_label.grid(row=5, column=0, columnspan=2, sticky=tk.W+tk.E)

otro_label_bienvenida = tk.Label(ventana, text= "Bienvenido <sin nombre>")
otro_label_bienvenida.grid(row=6, column=0, columnspan=2, sticky=tk.W+tk.E)

button_login.bind("<Button-1>", on_submit)
entry_email.bind("<Return>", on_submit)
entry_pw.bind("<Return>", on_submit)


ventana.mainloop()