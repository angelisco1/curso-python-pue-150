import tkinter as tk
import tkinter.messagebox
from .base_page import BasePage

class HomePage(BasePage):

    def __init__(self, parent, controller, api, *args, **kwargs):
        super().__init__(parent, controller, *args, **kwargs)
        self.api = api
        self.ingredients = []

        self.title = tk.Label(self, text="Lista de ingredientes")
        self.title.pack(pady=10)

        self.list_frame = tk.Frame(self)
        self.list_frame.pack()

        self.btn_create = tk.Button(
            self,
            text="Crear nuevo ingrediente",
            command=lambda: self.controller.show_frame("create")
        )
        self.btn_create.pack(pady=5)


    def refresh(self):
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        try:
            self.ingredients = self.api.get_ingredients()
            for ingredient in self.ingredients:
                self.__create_ingredient_row(ingredient)
        except Exception as e:
            tk.Label(self.list_frame, text=f"Error al cargar los ingredientes: {e}").pack()


    def __create_ingredient_row(self, ingredient):
        row = tk.Frame(self.list_frame)
        row.pack(fill="x", pady=2)

        ingredient_label = tk.Label(row, text=f"{ingredient["name"]} - {ingredient["price"]:.2f}€", anchor="w")
        ingredient_label.pack(side="left", expand=True, fill="x")

        # btn_edit = tk.Button(row, text="Editar", command=lambda: self.controller.show_edit_page(ingredient))
        btn_edit = tk.Button(
            row,
            text="Editar",
            command=lambda: self.controller.show_frame("edit", id=ingredient["id"])
        )
        btn_edit.pack(side="right")

        btn_delete = tk.Button(row, text="Eliminar", command=lambda: self.__delete_ingredient(ingredient["id"]))
        btn_delete.pack(side="right", padx=5)


    def __delete_ingredient(self, ingredient_id):
        try:
            self.api.delete_ingredient(ingredient_id)
            self.refresh()
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"No se pudo eliminar el ingrediente: {e}")





