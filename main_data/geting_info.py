import pandas as pd

stores = []
products_l = []


def products_list():
    excel_data = pd.read_excel('main_data/products_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        print(len(data))
        print(i)
        product = [data['Name'][i], data['Cost'][i]]
        print(data['Name'][i], data['Cost'][i])
        products_l.append(product)
    return products_l


def stores_list():
    excel_data = pd.read_excel('main_data/stores_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        store = [data['Name'][i], data['Adress'][i], data['Work Time'][i]]
        stores.append(store)
    return stores

