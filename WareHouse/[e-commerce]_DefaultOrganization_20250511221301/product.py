'''
Module to define the Product class for the e-commerce platform.
'''
class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
    def __str__(self):
        return f"{self.name} - ${self.price}: {self.description}"