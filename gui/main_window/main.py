import tkinter as tk
from tkinter import messagebox
import customtkinter
# from ...main import confirmExit
import sys


def mainWindow():
    root = MainWindow()
    root.start()


class MainWindow(customtkinter.CTk):

    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()

        self.title("Main")
        self.geometry('1280x720')

        # ============ Exit ============
        self.bind("<Escape>", self.confirmExit)
        self.protocol("WM_DELETE_WINDOW", self.confirmExit)

    def start(self):
        self.mainloop()

    def confirmExit(self, event=0):
        if messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
            self.quit()
