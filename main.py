
from Product import Product
from ShoppingCart import ShoppingCart

iPhone16 = Product("iPhone 16 Pro", 1000, 15, "ios")
iPhone14 = Product("iPhone 14 Pro", 800, 25, "ios")
iPhone13 = Product("iPhone 13 Pro", 100, 35, "ios")
samsung20 = Product("Samsung 20", 800, 20, "android")
samsung10 = Product("Samsung 10", 500, 45, "android")
samsung30 = Product("Samsung 30", 2000, 105, "android")

cart = ShoppingCart()
cart.add_item(iPhone16)
cart.add_item(iPhone14)
cart.add_item(iPhone13)
cart.add_item(samsung20)
cart.add_item(samsung10)
cart.add_item(samsung30)

cart.show_items()
print (Product.ios_amount, Product.android_amount)
