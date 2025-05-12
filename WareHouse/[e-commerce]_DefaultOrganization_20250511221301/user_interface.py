'''
Module to define the UserInterface class for the e-commerce platform.
'''
import tkinter as tk
from tkinter import messagebox
from database import Database
from cart import Cart
class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("E-Commerce Platform")
        self.database = Database()
        self.database.load_products()
        self.cart = Cart()
        self.create_widgets()
    def create_widgets(self):
        self.product_listbox = tk.Listbox(self.root)
        for product in self.database.get_products():
            self.product_listbox.insert(tk.END, str(product))
        self.product_listbox.pack()
        self.add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack()
        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack()
    def add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            product = self.database.get_products()[selected_index[0]]
            self.cart.add_product(product)
            messagebox.showinfo("Success", f"Added {product.name} to cart.")
    def view_cart(self):
        cart_contents = self.cart.view_cart()
        if cart_contents:
            cart_summary = "\n".join(str(product) for product in cart_contents)
            messagebox.showinfo("Cart", cart_summary)
        else:
            messagebox.showinfo("Cart", "Your cart is empty.")
    def run(self):
        self.root.mainloop()