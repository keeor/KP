import pandas as pd

stores = []
products = []


def products_list():

    excel_data = pd.read_excel('main_data/products_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        product = [data['Name'][i], data['Cost'][i]]
        products.append(product)
    return products


def get_product_info():
    product = products_list()
    return product


def stores_list():
    excel_data = pd.read_excel('main_data/stores_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        store = [data['Name'][i], data['Adress'][i], data['Work Time'][i]]
        stores.append(store)
    return stores


def get_stores_info():
    store = stores_list()
    return store



