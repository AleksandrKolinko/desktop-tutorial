from pathlib import Path


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.price}, {self.category}"


class Shop:
    def __init__(self):
        self.file_name = 'products.txt'

    def get_products(self):
        data = ''
        if Path(self.file_name).is_file():
            with open(self.file_name, 'r') as file:
                data = file.read()
        return data

    def add(self, *products):
        for product in products:
            name_product = self.get_products().split('\n')
            exists_product = False
            for i in name_product:
                if product.name in i:
                    exists_product = True
                    print(f"Продукт {product.name} уже есть в магазине")
                    break
            if not exists_product:
                with open(self.file_name, 'a') as file:
                    file.write(str(product) + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
