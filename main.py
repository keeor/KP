'''
Сервіс – «Кошик споживача».
Задача сервісу виконати підрахунок вартості кошика споживача за обраними
товарами на вказаних торгівельних майданчиках.
Клієнт сервісу:
a. формує кошик, вводить (обирає) перелік товарів;
b. обирає перелік супермаркетів, які будуть приймати участь у
формуванні кошика.
Сервіс:
c. видає інформацію про загальну вартість товарів по кожному
обраному торгівельному майданчику (з приміткою про відсутність
незнайдених товарів);
d. забезпечує можливість перегляду детальної інформації по обраним
товарам для кожного торгівельного майданчика;
надає інформацію про адресу та режим роботи торгівельного майданчика
'''

import tkinter as tk
from tkinter import *
from db import geting_info as gi
from tkinter.messagebox import showinfo


stores_list = gi.stores_list()
products_list = gi.products_list()
store_name_list = gi.store_list
cart = gi.ShoppingCart()
prod_lst = gi.list_inf()
#Создание интерфейса
root = tk.Tk()
root.title("Сервіс - Кошик споживача")

#Создание чек-листа продуктов
frame_products = tk.Frame(root)
frame_products.pack(side=tk.LEFT, padx=10)
scrollbar_product_list = tk.Scrollbar(frame_products)
scrollbar_product_list.pack(side=tk.RIGHT, fill=tk.Y)
listbox_product_list = tk.Listbox(frame_products, yscrollcommand=scrollbar_product_list.set)

for product in products_list:
    listbox_product_list.insert(tk.END, f"{product[0]}")
    listbox_product_list.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar_product_list.config(command=listbox_product_list.yview)
listbox_product_list.insert(tk.END, ' ')

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.LEFT, padx=10)


frame_list = tk.Frame(root)
frame_list.pack(side=tk.LEFT, padx=10)

def default_list():
    listbox_product_list.delete(0, tk.END)
    for product in products_list:
        listbox_product_list.insert(tk.END, f"{product[0]} ")
        listbox_product_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar_product_list.config(command=listbox_product_list.yview)
    listbox_product_list.insert(tk.END, ' ')

button_list = tk.Button(frame_list, text="All", command=lambda: default_list())
button_list.pack(pady=5)


def add_to_cart():
    # Функція додавання продукту до кошика
    selected_ind = listbox_product_list.curselection()
    i = int(selected_ind[0])
    product = products_list[i][0]
    cart.add_product(product)
    print(cart.products)


button_add_to_cart = tk.Button(frame_buttons, text="Додати в кошик", command=lambda: add_to_cart())
button_add_to_cart.pack(pady=5)

frame_filter = tk.Frame(root)
frame_filter.pack(side=tk.LEFT, padx=10)

label_filter = tk.Label(frame_filter, text="Фільтр")
label_filter.pack()


def filtered_list(sto):
    listbox_product_list.delete(0, tk.END)
    for product in sto:
        listbox_product_list.insert(tk.END, f"{product[0]} ")
        listbox_product_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar_product_list.config(command=listbox_product_list.yview)
    listbox_product_list.insert(tk.END, ' ')

new_list = []
def filter_products():
    print('pass')
    # Функція фільтрації продуктів за магазином
    selected_items = [item.get() for item in checkbox_vars]
    filtered_items = [stores_list[0] for stores_list, selected in zip(stores_list, selected_items) if selected]
    print(filtered_items)
    for i in range(len(prod_lst)):
        if prod_lst[i].name in filtered_items:
            for j in range(len(prod_lst[i].product_list)):
                if prod_lst[i].product_list[j][0] not in new_list:
                    new_list.append(prod_lst[i].product_list[j][0])
                    print(new_list)
        else:




checkbox_vars = []
for item in gi.stores_list():
    var = tk.BooleanVar()
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(frame_filter, text=item[0], variable=var)
    checkbox.pack(side=tk.LEFT)


button_compare = tk.Button(frame_buttons, text="Порівняти", command=lambda: filter_products())
button_compare.pack(pady=5)
var = StringVar()

def calculate_total_cost():
    # Функція розрахунку загальної вартості кошика
    total_cost = cart.calculate_total_cost()
    label_total_cost.config(text=f"Загальна вартість: {total_cost} грн.")


button_calculate_total_cost = tk.Button(root, text="Підрахувати загальну вартість", command=calculate_total_cost)
button_calculate_total_cost.pack(pady=10)

label_total_cost = tk.Label(root, text="Загальна вартість: ")
label_total_cost.pack()

root.mainloop()
