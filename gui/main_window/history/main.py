import tkinter as tk
from tkinter import messagebox
import customtkinter


def history():
    History()


class History(customtkinter.CTkToplevel):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("History")
        self.geometry(f"{History.WIDTH}x{History.HEIGHT}")

        # ============ make resizable = Fasle ============
        self.minsize(History.WIDTH, History.HEIGHT)
        self.maxsize(History.WIDTH, History.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog
        
        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())
        
