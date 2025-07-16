import tkinter as tk
from api import IngredientAPI
from pages import HomePage, CreateIngredientPage, EditIngredientPage

class AppController(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Gestor de ingredientes")
        self.geometry("1028x690")

        self.api = IngredientAPI()

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["home"] = HomePage(container, self, self.api)
        self.frames["create"] = CreateIngredientPage(container, self, self.api)
        self.frames["edit"] = EditIngredientPage(container, self, self.api)

        for frame in self.frames.values():
            # frame.pack(fill="both", expand=True)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("home")


    def show_frame(self, page, *args, **kwargs):
        frame = self.frames[page]
        frame.tkraise()
        frame.refresh(*args, **kwargs)