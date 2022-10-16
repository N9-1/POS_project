import csv
import os

# ============ product ============

def open_pd():
    os.startfile('.\data_file\DB_Milk-Tea.csv')

def get_data_pd():
    try:
        filepath_pd = '.\data_file\DB_Milk-Tea.csv'
        file_pd = open(filepath_pd)
        reader_pd = csv.reader(file_pd)
        data_pd = list(reader_pd)
        del(data_pd[0]) # delete header
        return data_pd
    except FileNotFoundError:
        directory = 'data_file'

        if not os.path.exists(directory):
            os.makedirs(directory)
            
        header = [['ID','Product_Name','Price','Discount']]
        with open('.\data_file\DB_Milk-Tea.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(header)
        data_pd = [] # return empty list
        return data_pd

# ============ cart ============
def get_data_cart():
    try:
        filepath_cart = '.\data_file\cart_record.csv'
        file_cart = open(filepath_cart)
        reader_cart = csv.reader(file_cart)
        data_cart = list(reader_cart)
        del(data_cart[0]) # delete header
        return data_cart
    except FileNotFoundError:
        directory = 'data_file'

        if not os.path.exists(directory):
            os.makedirs(directory)
            
        header = [['ID','Product_Name','Price','Discount','Item','Size','Topping','SweetnessLv','Total_Price']]
        with open('.\data_file\cart_record.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(header)
        data_cart = [] # return empty list
        return data_cart

def write_data_cart(*argv):
    with open('.\data_file\cart_record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(*argv)

def clear_data_cart():
    # open file
    filepath_cart = '.\data_file\cart_record.csv'
    file_cart = open(filepath_cart)
    reader_cart = csv.reader(file_cart)
    data_cart = list(reader_cart)
    with open('.\data_file\cart_record.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_cart[0])
    
def remove_row(n):
    filepath_cart = '.\data_file\cart_record.csv'
    file_cart = open(filepath_cart)
    reader_cart = csv.reader(file_cart)
    data_cart = list(reader_cart)
    index = n
    del data_cart[index+1]
    with open('.\data_file\cart_record.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_cart)

# ============ history ============
def write_sales_history(lst):
    with open('.\data_file\sales_history.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(lst)

def open_sales_history():
    try:
        filepath = '.\data_file\sales_history.csv'
        file_open = open(filepath)
    except FileNotFoundError:
        directory = 'data_file'

        if not os.path.exists(directory):
            os.makedirs(directory)
            
        header = [['time','Product_ID','Product_Name','Qty.','Size','Topping','SweetnessLv','Total']]
        with open('.\data_file\sales_history.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(header)
    os.startfile(filepath)