import tkinter as tk
from tkinter import messagebox
import customtkinter


def stockManagement():
    StockManagement()


class StockManagement(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.title("Stock Management")
        self.geometry("1280x720")

        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())

        # self.mainloop()

# if __name__ == "__main__":
#     stockManagement()