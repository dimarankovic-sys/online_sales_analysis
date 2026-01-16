from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()

manager.add_product(Product("Laptop", 1200, 3))
manager.add_product(Product("Telefon", 800, 4))
manager.add_product(Product("Slusalice", 150, 6))

cart = Cart()

for product in random.sample(manager.products, 3):
    cart.add_to_cart(product)

cart.display_cart()
print("Ukupno za naplatu:", cart.total_price())
