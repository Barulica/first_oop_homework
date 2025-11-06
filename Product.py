
from Db import Db

class Product(Db):

    ios_amount = 0
    android_amount = 0

    def __init__(self, name, price, amount, type):
        super().__init__()

        self.name = name
        self.price = price
        self.amount = amount
        self.type = type

        self.increment_number_of_products()
        cursor = self.connection.cursor()
        cursor.execute("insert into products(name,price,amount,type) values (%s, %s, %s, %s)", (name, price, amount, type))
        self.connection.commit()
        cursor.close()


    def increment_number_of_products(self):
        if self.type == "ios":
            Product.ios_amount += self.amount
        elif self.type == "android":
            Product.android_amount += self.amount
        else:
            print("Invalid type")

