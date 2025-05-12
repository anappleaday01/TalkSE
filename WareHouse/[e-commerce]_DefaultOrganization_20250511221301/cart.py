'''
Module to define the Cart class for managing shopping cart functionality.
'''
class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product):
        self.items.append(product)
    def remove_product(self, product):
        try:
            self.items.remove(product)
        except ValueError:
            print(f"Product {product.name} not found in cart.")
            # User feedback can be added here if needed
    def view_cart(self):
        return self.items
    def total_price(self):
        return sum(product.price for product in self.items)