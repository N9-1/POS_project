import tkinter as tk
import customtkinter
from gui.main_window.main import mainWindow

root = customtkinter.CTk()
root.withdraw()

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    mainWindow()

    root.mainloop()