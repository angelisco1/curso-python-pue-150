import tkinter as tk
import tkinter.messagebox
from .base_page import BasePage


class EditIngredientPage(BasePage):

    def __init__(self, parent, controller, api, *args, **kwargs):
        super().__init__(parent, controller, *args, **kwargs)
        self.api = api

        title = tk.Label(self, text="Editar ingrediente")
        title.pack(pady=10)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nombre:").grid(row=0, column=0, sticky="e", pady=5, padx=5)
        self.entry_name = tk.Entry(form_frame)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Precio:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.entry_price = tk.Entry(form_frame)
        self.entry_price.grid(row=1, column=1, pady=5, padx=5)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Cancelar",
            command=lambda: self.controller.show_frame("home")
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Guardar",
            command=self.submit
        ).pack(side="left", padx=5)

    def submit(self):
        id = self.ingredient_to_edit["id"]
        name = self.entry_name.get().strip()
        price = self.entry_price.get().strip()

        if not name or not price:
            tkinter.messagebox.showerror("Error", "Todos los campos son obligatorios")

        try:
            self.api.update_ingredient(id, name, price)
            tkinter.messagebox.showinfo("Éxito", "Ingrediente actualizado correctamente")
            self.controller.show_frame("home")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"No se pudo actualizar: {e}")

    def refresh(self, id=None):
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        if id is not None:
            self.ingredient_to_edit = self.__load_ingredient(id)
            self.entry_name.insert(0, self.ingredient_to_edit["name"])
            self.entry_price.insert(0, self.ingredient_to_edit["price"])

    def __load_ingredient(self, id):
        return self.api.get_ingredient(id)