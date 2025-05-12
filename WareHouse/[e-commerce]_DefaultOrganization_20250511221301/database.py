'''
Module to manage product data for the e-commerce platform.
'''
from product import Product
class Database:
    def __init__(self):
        self.products = []
    def load_products(self):
        # In a real application, this would load from a database or file.
        self.products = [
            Product("Laptop", 999.99, "High performance laptop."),
            Product("Smartphone", 499.99, "Latest model smartphone."),
            Product("Headphones", 199.99, "Noise-cancelling headphones.")
        ]
    def get_products(self):
        return self.products