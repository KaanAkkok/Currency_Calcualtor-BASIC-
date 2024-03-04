from tkinter import *
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup
import requests

Currency_html = requests.get('https://kur.doviz.com/').text
soup = BeautifulSoup(Currency_html, 'lxml')

USD_to_TRY = float(soup.find('td', {'data-socket-key':'USD'}, {'data-socket-attr':'ask'}).text.replace(',', '.'))
EUR_to_TRY = float(soup.find('td', {'data-socket-key':'EUR'}, {'data-socket-attr':'ask'}).text.replace(',', '.'))

currencies_list = ['USD', 'EUR', 'TRY']

def calculate_it():
    calculated_entry.delete(0,END)
    try:
        amount = float(original_entry.get().replace(',','.'))
        if(currencies_combo1.get() == 'USD' and currencies_combo2.get() == 'USD'):
            rate = 1
        elif(currencies_combo1.get() == 'USD' and currencies_combo2.get() == 'EUR'):
            rate = USD_to_TRY / EUR_to_TRY
        elif(currencies_combo1.get() == 'USD' and currencies_combo2.get() == 'TRY'):
            rate = USD_to_TRY
        elif(currencies_combo1.get() == 'EUR' and currencies_combo2.get() == 'EUR'):
            rate = 1
        elif(currencies_combo1.get() == 'EUR' and currencies_combo2.get() == 'USD'):
            rate = EUR_to_TRY / USD_to_TRY
        elif(currencies_combo1.get() == 'EUR' and currencies_combo2.get() == 'TRY'):
            rate = EUR_to_TRY
        elif(currencies_combo1.get() == 'TRY' and currencies_combo2.get() == 'TRY'):
            rate = 1
        elif(currencies_combo1.get() == 'TRY' and currencies_combo2.get() == 'EUR'):
            rate = 1 / EUR_to_TRY
        elif(currencies_combo1.get() == 'TRY' and currencies_combo2.get() == 'USD'):
            rate = 1 / USD_to_TRY
        else:
            messagebox.showerror("Error", "Please select a currency.")
        calculated_value = amount * rate
        calculated_entry.insert(0, f"{calculated_value:.2f}") 
    except KeyError:
        messagebox.showerror("Error", "Please select a currency.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def clear():
    original_entry.delete(0, END)
    calculated_entry.delete(0, END)
    
window = Tk()
window.geometry("800x200")
window.configure(bg='cyan')
window.title("Currency Calculator")

original_entry = Entry(window, font = ("Helvetica", 18))
original_entry.grid(row=1, column=0, padx=20, pady=20)

calculate_button = Button(window, command=calculate_it, text="Calculate!", font=("Helvetica", 24), bg='lightgreen')
calculate_button.grid(row=1, column=1, padx=10)

calculated_entry = Entry(window, font = ("Helvetica", 18))
calculated_entry.grid(row=1, column=2, padx=20, pady=20)

my_label1 = Label(window, text="Amount", font=("Helvetica", 12), bg='cyan')
my_label1.grid(row=0, column=0)

currencies_combo1 = ttk.Combobox(window, width=25, value=currencies_list, state="readonly")
currencies_combo1.grid(row=2, column=0)

my_label2 = Label(window, text="Result", font=("Helvetica", 12), bg='cyan')
my_label2.grid(row=0, column=2)

currencies_combo2 = ttk.Combobox(window, width=25, value=currencies_list, state="readonly")
currencies_combo2.grid(row=2, column=2)

clear_button = Button(window, command=clear, text="clear", font=("Helvetica", 12), bg='red')
clear_button.grid(row=2, column=1, pady=20)

window.mainloop()