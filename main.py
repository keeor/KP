import tkinter as tk
from db import geting_info

print(geting_info.get_stores_info())
print(geting_info.get_product_info())

stores = geting_info.stores_list()
products = geting_info.products_list()
shopping_cart =[]

root = tk.Tk()
root.title("Сервіс - Кошик споживача")

frame_products = tk.Frame(root)
frame_products.pack(side=tk.LEFT, padx=10)
scrollbar_product_list = tk.Scrollbar(frame_products)
scrollbar_product_list.pack(side=tk.RIGHT, fill=tk.Y)

listbox_product_list = tk.Listbox(frame_products, yscrollcommand=scrollbar_product_list.set)
for product in products:
    listbox_product_list.insert(tk.END, product[0])
    print(product[0])
listbox_product_list.pack(side=tk.LEFT, fill=tk.BOTH)
scrollbar_product_list.config(command=listbox_product_list.yview)

frame_buttons = tk.Frame(root)
frame_buttons.pack(side=tk.LEFT, padx=10)


root.mainloop()
