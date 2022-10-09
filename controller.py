import csv
from tkinter import messagebox

# ============ csv ============

def get_data_pd():
    try:
        filepath_pd = '.\data_file\DB_Milk-Tea.csv'
        file_pd = open(filepath_pd)
        reader_pd = csv.reader(file_pd)
        data_pd = list(reader_pd)
        del(data_pd[0]) # delete header
        return data_pd
    except FileNotFoundError:
        data_pd = []
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
        data_cart = []
        return data_cart

def write_data_cart(*argv):
    with open('.\data_file\cart_record.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(*argv)