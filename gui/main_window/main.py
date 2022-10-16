import tkinter as tk
from tkinter import messagebox
from math import ceil
import customtkinter
from controller import *
from datetime import datetime


def mainWindow():
    MainWindow()


def topping(name): # set product for topping 
    global pd
    pd = name


def getCSV():
    global data_pd, data_cart
    # ============ get csv ============
    data_pd = get_data_pd()
    data_cart = get_data_cart()


class Topping(customtkinter.CTkToplevel):

    WIDTH = 720
    HEIGHT = 500

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
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
        self.lst_rec[8] = float(pd[2])-float(pd[3]) # total price (price-discount)
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
        
    def cancel(self):
        self.destroy()

    def total_price(self):
        return self.lst_rec[8]+self.size_price+self.topping_price

    def price_update(self):
        self.var_price.set(f'price {self.total_price()} THB')

    def increase(self):
        self.data_itemcount += 1
        self.lst_rec[8] = (float(pd[2])-float(pd[3]))*self.data_itemcount
        self.lst_rec[4] = self.data_itemcount
        self.var_itemcount.set(f'{self.data_itemcount}')
        self.price_update()

    def decrease(self):
        if self.data_itemcount > 1:
            self.data_itemcount -= 1
            self.lst_rec[8] = (float(pd[2])-float(pd[3]))*self.data_itemcount
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

    def save(self):
        self.lst_rec[8] = self.total_price()
        write_data_cart(self.lst_rec)
        self.master.update_cart_button()
        self.cancel()


class Payment(customtkinter.CTkToplevel):
    
    WIDTH = 500
    HEIGHT = 300

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.title("Payment")
        self.geometry(f"{Payment.WIDTH}x{Payment.HEIGHT}")

        # ============ make resizable = Fasle ============
        self.minsize(Payment.WIDTH, Payment.HEIGHT)
        self.maxsize(Payment.WIDTH, Payment.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog
        
        # ============ main frame ============
        self.main_frame = customtkinter.CTkFrame(master=self, width=Payment.WIDTH-50, height=Payment.HEIGHT-50, corner_radius=10)
        self.main_frame.grid(column=0, row=0, pady=20, padx=20)
        self.main_frame.grid_propagate(False)

        # input paid amount
        self.paid_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text="Paid Amount (THB)",
                                              text_font=("Roboto Medium", -18))
        self.paid_label.grid(row=0, column=0, padx=20, pady=(20,0), sticky="w")
        self.paid_entry = customtkinter.CTkEntry(master=self.main_frame, 
                                                    placeholder_text="", 
                                                    width=Payment.WIDTH-100,
                                                    text_font=("Roboto Regular", -24))
        self.paid_entry.grid(column=0, row=1, padx=20, columnspan=2)
        self.paid_entry.focus()
        self.clear_button = customtkinter.CTkButton(self.main_frame,
                                 width=100,
                                 height=30,
                                 text='Clear',
                                 command=self.clear,
                                 corner_radius=5,
                                 fg_color="#a82222",
                                 hover_color="#7f1a1a",
                                 text_font=("Roboto Regular", -12))
        self.clear_button.grid(row=2, column=0, padx=20, sticky="w", pady=(20,0))

        self.fullypaid_button = customtkinter.CTkButton(self.main_frame,
                                 width=150,
                                 height=60,
                                 text="Fully Paid",
                                 command=self.fullypaid,
                                 corner_radius=15,
                                 text_font=("Roboto Regular", -20))
        self.fullypaid_button.grid(row=3, column=0, padx=(20, 0), sticky="w", pady=(20,0))
        self.proceed_button = customtkinter.CTkButton(self.main_frame,
                                 width=150,
                                 height=60,
                                 text="Proceed",
                                 command=self.proceed,
                                 fg_color="#5aa822",
                                 hover_color="#447f1a",
                                 corner_radius=15,
                                 text_font=("Roboto Regular", -20))
        self.proceed_button.grid(row=3, column=1, padx=(20, 0), sticky="w", pady=(20,0))

        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())

    def clear(self):
        self.paid_entry.delete(0, 'end')

    def fullypaid(self):
        self.paid_entry.delete(0, 'end')
        self.paid_entry.insert(0, self.get_total())

    def get_total(self):
        total = 0
        for i in data_cart:
            total += float(i[8])
        return str(total)
    
    def proceed(self):
        try:
            if float(self.paid_entry.get()) < float(self.get_total()):
                 messagebox.showwarning("warning", "The paid amount must exceed the total price.")
                 return
        except:
            messagebox.showerror("error", "Only digits allowed.")
            return

        global change, subtotal, paid_amount
        change = float(self.paid_entry.get()) - float(self.get_total())
        subtotal = float(self.get_total())
        paid_amount = float(self.paid_entry.get())
        # clear_data_cart()
        # self.master.update_cart_button()
        self.master.open_Receipt()
        self.destroy()


class Receipt(customtkinter.CTkToplevel):

    WIDTH = 600
    HEIGHT = 720

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.title("Receipt")
        self.geometry(f"{Receipt.WIDTH}x{Receipt.HEIGHT}")
        self.grid_propagate(False)

        # ============ make resizable = Fasle ============
        self.minsize(Receipt.WIDTH, Receipt.HEIGHT)
        self.maxsize(Receipt.WIDTH, Receipt.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog

        # ============ main frame ============
        self.main_frame = customtkinter.CTkFrame(master=self, width=Receipt.WIDTH-50, height=Receipt.HEIGHT-50, corner_radius=10)
        self.main_frame.grid(column=0, row=0, pady=20, padx=20)
        self.main_frame.grid_propagate(False)

        # top
        self.shop_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text="Bubble Milk Tea Shop",
                                              text_font=("Roboto Medium", -18),
                                              anchor="center")
        self.shop_label.grid(row=0, column=0, padx=20, pady=10, columnspan=4)
        self.receipt_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text="Receipt",
                                              text_font=("Roboto Regular", -16),
                                              anchor="center")
        self.receipt_label.grid(row=1, column=0, padx=20, pady=(10, 0), columnspan=4)
        
        # pd
        self.row = 2
        for value in data_cart:
            self.qty_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{value[4]}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
            self.qty_label.grid(row=self.row, column=0, padx=(10, 0), sticky='w')
            self.product_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{value[1]}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
            self.product_label.grid(row=self.row, column=1, padx=(5, 0), sticky='w')
            if float(value[4]) > 1:
                self.price_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{float(value[2])-float(value[3]):.2f}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
                self.price_label.grid(row=self.row, column=2, padx=(5, 0), sticky='w')
            self.totalprice_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{float(value[8]):.2f}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
            self.totalprice_label.grid(row=self.row, column=3, padx=(5, 10), sticky='w')
            
            self.row += 1
        # next
        self.discount_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"Discount",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.discount_label.grid(row=self.row, column=0, padx=(5, 10), sticky='w')
        self.discountam_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{self.sum_dis():.2f}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.discountam_label.grid(row=self.row, column=2, padx=(5, 10), sticky='w')
        # next
        self.row += 1
        self.subtotal_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"Subtotal",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.subtotal_label.grid(row=self.row, column=0, padx=(5, 10), sticky='w')
        self.allqty_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{self.sum_qty()} Items",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.allqty_label.grid(row=self.row, column=1, padx=(5, 10), sticky='w')
        self.subtotalprice_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{subtotal:.2f}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.subtotalprice_label.grid(row=self.row, column=2, padx=(5, 10), sticky='w')
        # next
        self.row += 1
        self.paid_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"Paid Amount",
                                              text_font=("Roboto Regular", -18),
                                              anchor='w')
        self.paid_label.grid(row=self.row, column=0, padx=(5, 10), sticky='w')
        self.paidam_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{paid_amount:.2f}",
                                              text_font=("Roboto Regular", -18),
                                              anchor='w')
        self.paidam_label.grid(row=self.row, column=2, padx=(5, 10), sticky='w')
        # next
        self.row += 1
        self.change_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"Change",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.change_label.grid(row=self.row, column=0, padx=(5, 10), sticky='w')
        self.changeam_label = customtkinter.CTkLabel(master=self.main_frame,
                                              text=f"{change:.2f}",
                                              text_font=("Roboto Regular", -16),
                                              anchor='w')
        self.changeam_label.grid(row=self.row, column=2, padx=(5, 10), sticky='w')

        # ============ write to history ============
        # dd/mm/YY H:M:S
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        history_lst = []
        for i in data_cart:
            data_lst = [dt_string, i[0], i[1], i[4], i[5], i[6], i[7], i[8]]
            history_lst.append(data_lst)
        write_sales_history(history_lst)

        # ============ reset ============
        clear_data_cart()
        self.master.update_cart_button()

        # ============ Exit ============
        self.bind("<Escape>", lambda q: self.destroy())
        
    def sum_qty(self):
        self.sumqty = 0
        for i in data_cart:
            self.sumqty += int(i[4])
        return self.sumqty

    def sum_dis(self):
        self.sumdis = 0
        for i in data_cart:
            self.sumdis += float(i[3])
        return self.sumdis


class StockManagement(customtkinter.CTkToplevel):

    WIDTH = 300
    HEIGHT = 300

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Stock Management")
        self.geometry(f"{StockManagement.WIDTH}x{StockManagement.HEIGHT}")
        self.grid_propagate(False)
        # ============ make resizable = Fasle ============
        self.minsize(StockManagement.WIDTH, StockManagement.HEIGHT)
        self.maxsize(StockManagement.WIDTH, StockManagement.HEIGHT)

        self.attributes('-topmost', 'true') # always on top
        self.grab_set() # ensure that users can only interact with dialog

        # ============ main ============
        self.save_button = customtkinter.CTkButton(self,
                                 width=150,
                                 height=60,
                                 text="Save",
                                 command=self.save,
                                 fg_color="#5aa822",
                                 hover_color="#447f1a",
                                 corner_radius=15,
                                 text_font=("Roboto Regular", -20)).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # ============ open file ============
        open_pd()

        # ============ Exit ============
        self.bind("<Return>", self.save)
        self.bind("<Escape>", lambda q: self.destroy())
    
    def save(self, *argv):
        self.master.update_product_button()
        self.destroy()


class MainWindow(customtkinter.CTk):

    customtkinter.set_appearance_mode("dark")
    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("POS Software")
        self.geometry(f"{MainWindow.WIDTH}x{MainWindow.HEIGHT}")
        self.resizable(False, False)
        self.refresh()
        # ============ menu ============
        self.button_stock = customtkinter.CTkButton(master=self,
                                 width=60,
                                 height=30,
                                 text="stock",
                                 command=self.open_stockManagement,
                                 corner_radius=15)
        self.button_stock.grid(column=0, row=0, sticky="sw", padx=20, pady=(20,0))                         
        self.button_history = customtkinter.CTkButton(master=self,
                                 width=60,
                                 height=30,
                                 text="history",
                                 command=self.open_history,
                                 corner_radius=15)
        self.button_history.grid(column=0, row=0, sticky="sw", padx=100, pady=(20,0))

        # ============ Product ============
        self.product_frame = customtkinter.CTkFrame(master=self, width=645-50, height=625, corner_radius=10)
        self.product_frame.grid(column=0, row=1, sticky="s", padx=20, pady=20)
        self.all_product = len(data_pd)
        self.product_frame.grid_propagate(False)

        # Label & var
        self.var_label_countproduct = tk.StringVar(value=f"{self.all_product} items found")
        self.label_allproduct = customtkinter.CTkLabel(master=self.product_frame,
                                              text="All Items",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_allproduct.grid(row=0, column=0, pady=(10,0), sticky="sw")

        self.label_countproduct = customtkinter.CTkLabel(master=self.product_frame,
                                              textvariable=self.var_label_countproduct,
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_countproduct.grid(row=2, column=0, pady=(0,10), sticky="se")                                      

            # canvas
        self.product_canvas = customtkinter.CTkCanvas(master=self.product_frame,
                                highlightthickness=0,
                                width=645-90,
                                height=625-20-26-26-10,
                                bg="#2A2D2E")
        self.product_canvas.grid(row=1, column=0, padx=(5, 0), pady=5, sticky="nsew")

        # scrollbar
        self.product_scrollbar = customtkinter.CTkScrollbar(self.product_frame, orientation="vertical", command=self.product_canvas.yview, fg_color="#2A2D2E")
        self.product_scrollbar.grid(row=1, column=1, sticky="ns", padx=(0, 5), pady=5)

        # connect textbox scroll event to scrollbar
        self.product_canvas.configure(yscrollcommand=self.product_scrollbar.set)

        # Create a frame to contain the buttons
        self.product_frame_buttons = customtkinter.CTkFrame(self.product_canvas)
        # self.product_frame_buttons.grid_propagate(False)
        self.product_canvas.create_window((0, 0), window=self.product_frame_buttons, anchor='nw')

        # ============ Product Button ============
        self.product_button_size = 250
        self.product_button_height = 100
        self.product_col = 2
        self.product_row = ceil(self.all_product/self.product_col)
        self.items_count = 0
        
        self.pd_buttonlst = []
        for i in range(self.product_row):
            for j in range(self.product_col):
                self.b = customtkinter.CTkButton(self.product_frame_buttons,
                                    width=self.product_button_size,
                                    height=self.product_button_height,
                                    text="",
                                    command=lambda button_count=self.items_count : self.cart_update(button_count),
                                    corner_radius=10,
                                    border_width=1,
                                    border_color="white", 
                                    fg_color=None, 
                                    text_color="white",
                                    text_font=("Roboto Medium", -16))
                self.b.configure(text= data_pd[self.items_count][1])
                self.b.grid(row=i, column=j, pady=10, padx=10, sticky="nsew")
                self.pd_buttonlst.append(self.b)
                self.items_count += 1
            if i == self.product_row-2:
                self.product_col -= (self.product_col*self.product_row)-self.all_product
        
        self.update_idletasks()
        
        if self.product_row > 5:
            self.product_canvas.config(scrollregion=(0,0,0,self.product_frame_buttons.winfo_height()+5))
        else:
            self.product_canvas.config(scrollregion=(0,0,0,self.product_frame.winfo_width()+10))
        # ============ Cart ============

        # main frame
        self.cart_frame = customtkinter.CTkFrame(master=self, width=645-50, height=625, corner_radius=10)
        self.cart_frame.grid(column=1, row=1, sticky="e", padx=(20, 20), pady=20)
        self.cart_frame.grid_propagate(False)

        # Label & var
        self.all_items = len(data_cart)
        
        self.total_price = 0
        self.total_dis = 0

        self.var_allcart = tk.StringVar(value=f"Total {self.all_items} items")
        self.var_totalprice = tk.StringVar(value=f"{self.total_price:.2f} THB")
        
        self.label_itemcart = customtkinter.CTkLabel(master=self.cart_frame,
                                              text="Item Cart",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_itemcart.grid(row=0, column=0, pady=(10,0), sticky="sw")
        
        self.label_allcart = customtkinter.CTkLabel(master=self.cart_frame,
                                              textvariable=self.var_allcart,
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_allcart.grid(row=0, column=1, pady=(10,0), sticky="se")
        
        self.label_dis = customtkinter.CTkLabel(master=self.cart_frame,
                                              text="Discount",
                                              text_font=("Roboto Medium", -18))
        self.label_dis.grid(row=2, column=0, pady=(10,0), sticky="sw")
        self.var_dis = tk.StringVar(value="0.00 THB")
        self.label_dis_price = customtkinter.CTkLabel(master=self.cart_frame,
                                              textvariable=self.var_dis,
                                              text_font=("Roboto Medium", -18))
        self.label_dis_price.grid(row=2, column=1, pady=(10,0), sticky="se")

        
        self.label_totalprice = customtkinter.CTkLabel(master=self.cart_frame,
                                              textvariable=self.var_totalprice,
                                              text_font=("Roboto Medium", -24))
        self.label_totalprice.grid(row=3, column=1, pady=(10), sticky="se")

        self.button_clear = customtkinter.CTkButton(self.cart_frame,
                                 width=150,
                                 height=60,
                                 text="Clear",
                                 command=self.clear_button,
                                 corner_radius=15,
                                 fg_color="#a82222",
                                 hover_color="#7f1a1a",
                                 text_font=("Roboto Regular", -20))
        self.button_clear.grid(row=4, column=0, pady=(10,0), sticky="s")

        self.button_pay = customtkinter.CTkButton(self.cart_frame,
                                 width=150,
                                 height=60,
                                 text="Pay Now",
                                 command=self.pay_button,
                                 corner_radius=15,
                                 fg_color="#5aa822",
                                 hover_color="#447f1a",
                                 text_font=("Roboto Regular", -20))
        self.button_pay.grid(row=4, column=1, pady=(10,0), sticky="s")
                        
        # create scrollable 

            # Create a frame for the canvas with non-zero row&column weights
        self.cart_sub_frame = customtkinter.CTkFrame(master=self.cart_frame, width=645-100, height=625-250, corner_radius=10)
        self.cart_sub_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="nsew")
        self.cart_sub_frame.grid_rowconfigure(0, weight=1)
        self.cart_sub_frame.grid_columnconfigure(0, weight=1)
        self.cart_sub_frame.grid_propagate(False)

            # canvas
        self.cart_canvas = customtkinter.CTkCanvas(master=self.cart_sub_frame,
                                highlightthickness=0,
                                width=self.cart_sub_frame.winfo_width()-140,
                                height=self.cart_sub_frame.winfo_width()-140,
                                bg="#343638")
        self.cart_canvas.grid(row=0, column=0, padx=(5, 0), pady=5, sticky="nsew")

        # scrollbar
        self.cart_scrollbar = customtkinter.CTkScrollbar(self.cart_sub_frame, orientation="vertical", command=self.cart_canvas.yview)
        self.cart_scrollbar.grid(row=0, column=1, sticky="ns", padx=(0, 5), pady=5)

        # connect textbox scroll event to scrollbar
        self.cart_canvas.configure(yscrollcommand=self.cart_scrollbar.set)

        # Create a frame to contain the buttons
        self.frame_buttons = customtkinter.CTkFrame(self.cart_canvas, fg_color="#343638") #343638
        self.cart_canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        # cart button
        self.cart_button_width = 30
        self.cart_button_count = 0
        for i in range(self.all_items):
            # label
            self.label_product = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=data_cart[i][1],
                                              text_font=("Roboto Medium", -16),
                                              anchor="w")
            self.label_product.pack(fill=tk.BOTH, padx=10)

            self.label_size = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"size: {data_cart[i][5]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_size.pack()
            
            self.label_topping = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"Topping: {data_cart[i][6]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_topping.pack()

            self.label_swlv = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"Sweetness Level: {data_cart[i][7]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_swlv.pack()

            self.label_ttp = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"{float(data_cart[i][8]):.2f} THB",
                                              text_font=("Roboto Medium", -16),
                                              anchor="w")
            self.label_ttp.pack()

            self.b = customtkinter.CTkButton(self.frame_buttons,
                                 width=self.cart_button_width,
                                 height=self.cart_button_width,
                                 text=f"Remove",
                                 command=lambda button_count=self.cart_button_count : self.remove_button(button_count),
                                 corner_radius=10,
                                 fg_color="#a82222",
                                 hover_color="#7f1a1a",
                                 text_font=("Roboto Regular", -12))
            # self.b.grid(row=i+1, column=0, pady=5, padx=10, sticky="sw")
            self.b.pack(pady=5, padx=10, anchor="w")

            self.cart_button_count += 1
        
        self.update_idletasks() 
        
        if self.frame_buttons.winfo_height()+5 < self.cart_sub_frame.winfo_width(): # +pady
            self.cart_canvas.config(scrollregion=(0,0,0,365)) # 2 items
        else:
            self.cart_canvas.config(scrollregion=(0,0,0,self.frame_buttons.winfo_height()))
        
        # ============ Update ============
        self.update_label() # update label
        
        # ============ Exit ============
        self.bind("<Escape>", self.confirmExit)
        self.protocol("WM_DELETE_WINDOW", self.confirmExit)

        self.mainloop()

    def cart_update(self, b_index):
        data = data_pd[b_index]
        topping(data) # set data to global
        Topping(self) # run Topping class

    def clear_button(self):
        for widget in self.frame_buttons.winfo_children(): # clear button list
            widget.destroy()
        clear_data_cart() # clear csv
        self.update_cart_button()

    def pay_button(self):
        if data_cart:
            Payment(self)
        else:
            messagebox.showwarning("warning", "Cart is empty.")

    def open_stockManagement(self):
        StockManagement()

    def open_history(self):
        open_sales_history()

    def open_Receipt(self):
        Receipt(self)

    def cal_total_price(self):
        self.cal = 0
        for i in data_cart:
            self.cal += float(i[8])+float(i[3])
        self.total_price = self.cal
        self.var_totalprice.set(f'{self.total_price:.2f} THB')

    def cal_total_discount(self):
        self.cal = 0
        for i in data_cart: # get discount
            self.cal += float(i[3])
        self.total_dis = self.cal
        self.var_dis.set(value=f'{self.total_dis:.2f} THB')

    def update_label(self):
        self.cal_total_discount()
        self.cal_total_price()
        self.all_items = len(data_cart)
        self.var_allcart.set(value=f"Total {self.all_items} items")

    def remove_button(self, index):
        remove_row(index)
        self.update_cart_button()

    def update_product_button(self):
        self.refresh() # get csv again
        self.update_label() # update price label
        for widget in self.product_frame_buttons.winfo_children(): # clear button list
            widget.destroy()
        
        # update
        self.all_product = len(data_pd)
        self.var_label_countproduct.set(value=f"{self.all_product} items found")
        
        # run again
        self.product_col = 2
        self.product_row = ceil(self.all_product/self.product_col)
        self.items_count = 0
        
        self.pd_buttonlst = []
        for i in range(self.product_row):
            for j in range(self.product_col):
                self.b = customtkinter.CTkButton(self.product_frame_buttons,
                                    width=self.product_button_size,
                                    height=self.product_button_height,
                                    text="",
                                    command=lambda button_count=self.items_count : self.cart_update(button_count),
                                    corner_radius=10,
                                    border_width=1,
                                    border_color="white", 
                                    fg_color=None, 
                                    text_color="white",
                                    text_font=("Roboto Medium", -16))
                self.b.configure(text= data_pd[self.items_count][1])
                self.b.grid(row=i, column=j, pady=10, padx=10, sticky="nsew")
                self.pd_buttonlst.append(self.b)
                self.items_count += 1
            if i == self.product_row-2:
                self.product_col -= (self.product_col*self.product_row)-self.all_product
        
        self.update_idletasks()
        
        if self.product_row > 5:
            self.product_canvas.config(scrollregion=(0,0,0,self.product_frame_buttons.winfo_height()+5))
        else:
            self.product_canvas.config(scrollregion=(0,0,0,self.product_frame.winfo_width()+10))

    def update_cart_button(self):
        self.refresh() # get csv again
        self.update_label() # update price label

        for widget in self.frame_buttons.winfo_children(): # clear button list
            widget.destroy()
        self.cart_button_count = 0
        for i in range(self.all_items):
            # label
            self.label_product = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=data_cart[i][1],
                                              text_font=("Roboto Medium", -16),
                                              anchor="w")
            self.label_product.pack(fill=tk.BOTH, padx=10)

            self.label_size = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"size: {data_cart[i][5]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_size.pack()
            
            self.label_topping = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"Topping: {data_cart[i][6]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_topping.pack()

            self.label_swlv = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"Sweetness Level: {data_cart[i][7]}",
                                              text_font=("Roboto Medium", -12),
                                              text_color="gray",
                                              anchor="w")
            self.label_swlv.pack()

            self.label_ttp = customtkinter.CTkLabel(master=self.frame_buttons,
                                              text=f"{float(data_cart[i][8]):.2f} THB",
                                              text_font=("Roboto Medium", -16),
                                              anchor="w")
            self.label_ttp.pack()

            self.b = customtkinter.CTkButton(self.frame_buttons,
                                 width=self.cart_button_width,
                                 height=self.cart_button_width,
                                 text=f"Remove",
                                 command=lambda button_count=self.cart_button_count : self.remove_button(button_count),
                                 corner_radius=10,
                                 fg_color="#a82222",
                                 hover_color="#7f1a1a",
                                 text_font=("Roboto Regular", -12))
            # self.b.grid(row=i+1, column=0, pady=5, padx=10, sticky="sw")
            self.b.pack(pady=5, padx=10, anchor="w")

            self.cart_button_count += 1
        
        self.update_idletasks() 
        
        if self.frame_buttons.winfo_height()+5 < self.cart_sub_frame.winfo_width(): # +pady
            self.cart_canvas.config(scrollregion=(0,0,0,365)) # 2 items
        else:
            self.cart_canvas.config(scrollregion=(0,0,0,self.frame_buttons.winfo_height()))

    def refresh(self):
        getCSV()
        
    def confirmExit(self, event=0):
        if messagebox.askokcancel('Quit', 'Are you sure you want to exit?', icon = 'warning'):
            self.quit()
