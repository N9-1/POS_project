import tkinter as tk
from tkinter import messagebox
import customtkinter


def stockManagement():
    StockManagement()


class StockManagement(customtkinter.CTkToplevel):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Stock Management")
        self.geometry(f"{StockManagement.WIDTH}x{StockManagement.HEIGHT}")

        # ============ make resizable = Fasle ============
        self.minsize(StockManagement.WIDTH, StockManagement.HEIGHT)
        self.maxsize(StockManagement.WIDTH, StockManagement.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog
        
        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())
        
