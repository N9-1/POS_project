import tkinter as tk
from tkinter import messagebox
from turtle import pd
import customtkinter
import csv
from controller import write_data_cart

def topping(name):
    global pd
    pd = name
    Topping()
    # print(get_data_pd())

class Topping(customtkinter.CTkToplevel):

    WIDTH = 720
    HEIGHT = 500

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(f"{pd[1]}")
        self.geometry(f"{Topping.WIDTH}x{Topping.HEIGHT}")

        # ============ make resizable = Fasle ============
        self.minsize(Topping.WIDTH, Topping.HEIGHT)
        self.maxsize(Topping.WIDTH, Topping.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog
        # ============ list for record ============
        self.lst_rec = [] # get range 0-8
        self.lst_rec.extend(pd) # add 0-3
        self.lst_sample = [None] * 5 # add None range
        self.lst_rec.extend(self.lst_sample)
        # print(self.lst_rec)
        # ============ label ============
        self.label_tps = customtkinter.CTkLabel(master=self,
                                              text="Select Topping",
                                              text_font=("Roboto Medium", -18))
        self.label_tps.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # ============ Main frame ============
        self.main_frame = customtkinter.CTkFrame(master=self, width=Topping.WIDTH-50, height=Topping.HEIGHT-118, corner_radius=10)
        self.main_frame.grid(column=0, row=1, sticky="s", padx=20, pady=(0, 20))
        self.main_frame.grid_propagate(False)
        # ============ size ============
        # label
        self.lst_size = ["M","L"]
        self.label_size = customtkinter.CTkLabel(master=self.main_frame,
                                              text="Size",
                                              text_font=("Roboto Medium", -16))
        self.label_size.grid(row=0, column=0, padx=20, pady=10)
        self.combobox_size = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=self.lst_size,
                                       command=self.size_callback)
        self.combobox_size.grid(row=1, column=0, padx=20, pady=(0,10))

        # ============ topping ============
        self.lst_topping = ["None","Boba", "Grass jelly", "Cheese foam", "Taro", "Fruity jelly", "Aiyu jelly"]
        self.label_topping = customtkinter.CTkLabel(master=self.main_frame,
                                              text="topping",
                                              text_font=("Roboto Medium", -16))
        self.label_topping.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_topping = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=self.lst_topping,
                                       command=self.topping_callback)
        self.combobox_topping.grid(row=3, column=0, padx=20, pady=(0,10))

        # ============ sweetness level ============
        self.lst_sweetnesslv = ["100%", "75%", "50%", "25%", "0%"]
        self.label_sweetnesslv = customtkinter.CTkLabel(master=self.main_frame,
                                              text="Sweetness Level",
                                              text_font=("Roboto Medium", -16))
        self.label_sweetnesslv.grid(row=4, column=0, padx=20, pady=10)
        self.combobox_sweetnesslv = customtkinter.CTkOptionMenu(master=self.main_frame,
                                       values=self.lst_sweetnesslv,
                                       command=self.swlv_callback)
        self.combobox_sweetnesslv.grid(row=5, column=0, padx=20, pady=(0,10))

        # ============ list default ============
        self.size_price = 0
        self.topping_price = 0
        self.lst_rec[5] = self.lst_size[0]
        self.lst_rec[6] = self.lst_topping[0]
        self.lst_rec[7] = self.lst_sweetnesslv[0]
        self.lst_rec[8] = int(pd[2])-int(pd[3]) # total price (price-discount)
        # ============ lower button ============
        self.low_frame = customtkinter.CTkFrame(master=self, width=Topping.WIDTH-50, height=35, fg_color="#212325")
        self.low_frame.grid(column=0, row=2, sticky="w", padx=20, pady=(0, 20))
        self.low_frame.grid_propagate(False)
        self.btn_decrease = customtkinter.CTkButton(self.low_frame,
                                 width=30,
                                 height=30,
                                 text='-',
                                 command=self.decrease,
                                 corner_radius=5,
                                 text_font=("Roboto Regular", -18))
        self.btn_decrease.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.data_itemcount = 1
        self.lst_rec[4] = self.data_itemcount
        # print(self.lst_rec)
        self.var_itemcount = tk.StringVar(value=f'{self.data_itemcount}')
        # .set()
        self.label_itemcount = customtkinter.CTkLabel(master=self.low_frame,
                                    textvariable=self.var_itemcount,
                                    text_font=("Roboto Medium", -16))
        self.label_itemcount.grid(row=0, column=1, sticky="w")

        self.btn_increase = customtkinter.CTkButton(self.low_frame,
                                 width=30,
                                 height=30,
                                 text='+',
                                 command=self.increase,
                                 corner_radius=5,
                                 text_font=("Roboto Regular", -18))
        self.btn_increase.grid(row=0, column=3, padx=(0,5), sticky="w")
        self.var_price = tk.StringVar(value=f'price {self.lst_rec[8]} THB')
        self.label_price = customtkinter.CTkLabel(master=self.low_frame,
                                    textvariable=self.var_price,
                                    text_font=("Roboto Medium", -16))
        self.label_price.grid(row=0, column=4, sticky="w")

        self.btn_cancel = customtkinter.CTkButton(self.low_frame,
                                 width=100,
                                 height=30,
                                 text='Cancel',
                                 command=self.cancel,
                                 corner_radius=5,
                                 fg_color="#a82222",
                                 hover_color="#7f1a1a",
                                 text_font=("Roboto Regular", -12))
        self.btn_cancel.grid(row=0, column=5, padx=20, sticky="e")
        self.btn_save = customtkinter.CTkButton(self.low_frame,
                                 width=120,
                                 height=30,
                                 text='Save',
                                 command=self.save,
                                 corner_radius=5,
                                 fg_color="#5aa822",
                                 hover_color="#447f1a",
                                 text_font=("Roboto Regular", -12))
        self.btn_save.grid(row=0, column=6, padx=20, sticky="e")

        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())
        
    def button_event(self):
        print("button pressed")

    def cancel(self):
        self.destroy()

    def total_price(self):
        return self.lst_rec[8]+self.size_price+self.topping_price

    def price_update(self):
        self.var_price.set(f'price {self.total_price()} THB')

    def increase(self):
        self.data_itemcount += 1
        self.lst_rec[8] = (int(pd[2])-int(pd[3]))*self.data_itemcount
        self.lst_rec[4] = self.data_itemcount
        self.var_itemcount.set(f'{self.data_itemcount}')
        self.price_update()
        # print(self.data_itemcount, self.lst_rec[8], self.lst_rec[4])

    def decrease(self):
        if self.data_itemcount > 1:
            self.data_itemcount -= 1
            self.lst_rec[8] = (int(pd[2])-int(pd[3]))*self.data_itemcount
            self.lst_rec[4] = self.data_itemcount
            self.var_itemcount.set(f'{self.data_itemcount}')
            self.price_update()

    def size_callback(self, choice):
        self.lst_rec[5] = choice
        if choice == "L": # L size +15 THB
            self.size_price = 15
        else: self.size_price = 0
        self.price_update()

    def topping_callback(self, choice):
        self.lst_rec[6] = choice
        if choice != "None":  # L topping +10 THB
            self.topping_price = 10
        else: self.topping_price = 0
        self.price_update()

    def swlv_callback(self, choice):
        self.lst_rec[7] = choice

    def optionmenu_callback(self, choice):
        print("optionmenu dropdown clicked:", choice)

    def save(self):
        self.lst_rec[8] = self.total_price()
        write_data_cart(self.lst_rec)
        self.cancel()
        # print(self.lst_rec)
