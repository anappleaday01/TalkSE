'''
Defines the Product class for the e-commerce application.
'''
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description