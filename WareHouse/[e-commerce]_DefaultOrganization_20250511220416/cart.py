'''
Defines the Cart class for managing shopping cart functionality.
'''
from product import Product
class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product):
        self.items.append(product)
    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)
    def view_cart(self):
        return self.items
    def checkout(self):
        total = sum(product.price for product in self.items)
        self.items.clear()  # Clear the cart after checkout
        return total