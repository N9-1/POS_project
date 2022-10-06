import tkinter as tk
import customtkinter


def mainWindow():
    MainWindow()


class MainWindow(customtkinter.CTkToplevel):

    def __init__(self):
        super().__init__()
        self.title("Main")
        self.geometry("500x400")