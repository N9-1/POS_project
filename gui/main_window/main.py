import tkinter as tk
from tkinter import messagebox
import customtkinter
from .stock_management.main import stockManagement


def mainWindow():
    MainWindow()


class MainWindow(customtkinter.CTk):

    customtkinter.set_appearance_mode("dark")
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Main")
        self.geometry(f"{MainWindow.WIDTH}x{MainWindow.HEIGHT}")
        self.resizable(False, False)

        self.button = customtkinter.CTkButton(self, text="Create Toplevel", command=self.create_toplevel)
        self.button.pack(side="top", padx=40, pady=40)
        
        # ============ Exit ============
        self.bind("<Escape>", self.confirmExit)
        self.protocol("WM_DELETE_WINDOW", self.confirmExit)

        
        self.mainloop()

    def create_toplevel(self):
        stockManagement()

    def confirmExit(self, event=0):
        if messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
            self.quit()
