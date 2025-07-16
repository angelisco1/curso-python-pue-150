import tkinter as tk
from abc import ABC, abstractmethod


class BasePage(tk.Frame, ABC):
    def __init__(self, parent, controller, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.controller = controller

    @abstractmethod
    def refresh(self):
        pass
