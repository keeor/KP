import pandas as pd


class Store:
    def __init__(self, name, adress, work_time):
        self.name = name
        self.adress = adress
        self.work_time = work_time
        self.product_list = []

    def get_name(self, cls):
        Store.name_list.append(self.name)

    def ret_names(self):
        return self.name_list

    def prod_list_data(self, product):
        self.product_list.append(product)


def stores_list():
    stores = []
    excel_data = pd.read_excel('main_data/stores_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        store = [data['Name'][i], data['Adress'][i], data['Work Time'][i]]
        stores.append(store)
    return stores


data = stores_list()
store_list = []
names = []
address = []
work_time = []
products_l = []

# Создание класов в елементах списка и заполнение их инфой
for name in data:
    store_list.append(name)
for i in range(len(store_list)):
    names.append(store_list[i][0])
    address.append(store_list[i][1])
    work_time.append(store_list[i][2])
    store_list[i] = Store(names[i], address[i], work_time[i])

# Заполнение списка продуктов каждого магазина
for i in range(len(store_list)):
    Name = store_list[i].name
    for stor in store_list:
        if stor.name == store_list[i].name:
            excel_data = pd.read_excel(f'main_data/{Name} products_list.xlsx')
            data = pd.DataFrame(excel_data)
            for j in range(len(data)):
                product = [data['Name'][j], data['Cost'][j]]
                store_list[i].prod_list_data(product)


def list_inf():
    return store_list


def products_list():
    products_l = []
    excel_data = pd.read_excel('main_data/products_list.xlsx')
    data = pd.DataFrame(excel_data)
    for i in range(len(data['Name'])):
        product = [data['Name'][i], data['Cost'][i]]
        products_l.append(product)
    return products_l


cart_list = list_inf()


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_cost(self):
        sum_list = []
        sub_list = []
        prod = []
        for i in range(len(cart_list)):
            s = 0
            p = []
            for item in cart_list[i].product_list:
                if item[0] in self.products:
                    s += item[1]
                    if item[0] not in prod:
                        p.append(item[0])
            sum_list.append(s)
            prod.append(p)
            for it in range(len(sum_list)):
                if [cart_list[it].name] not in sub_list:
                    sub_list.append([cart_list[it].name])
        for j in range(len(sum_list)):
            sub_list[j].append(sum_list[j])
            sub_list[j].append(prod[j])

        return(sub_list)
