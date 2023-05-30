import tkinter as tk
from db import geting_info


stores_list = geting_info.stores_list()
products_list = geting_info.products_list()
shopping_cart =[]

root = tk.Tk()
root.title("Сервіс - Кошик споживача")

frame_products = tk.Frame(root)
frame_products.pack(side=tk.LEFT, padx=10)
scrollbar_product_list = tk.Scrollbar(frame_products)
scrollbar_product_list.pack(side=tk.RIGHT, fill=tk.Y)

listbox_product_list = tk.Listbox(frame_products, yscrollcommand=scrollbar_product_list.set)
print(products_list)
for product in products_list:
    listbox_product_list.insert(tk.END, f"{product[0]} {product[1]}")
    listbox_product_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_product_list.config(command=listbox_product_list.yview)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.LEFT, padx=10)


root.mainloop()
