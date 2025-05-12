'''
Handles the graphical user interface for the e-commerce application.
'''
import tkinter as tk
from tkinter import messagebox
from product import Product
from cart import Cart
from database import Database
class UserInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("E-Commerce Platform")
        self.cart = Cart()
        self.database = Database()
        self.create_widgets()
    def create_widgets(self):
        self.product_listbox = tk.Listbox(self.root)
        self.product_listbox.pack()
        for product in self.database.get_products():
            self.product_listbox.insert(tk.END, product.name)
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.pack()
        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.pack()
        self.checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout)
        self.checkout_button.pack()
    def add_to_cart(self):
        selected_index = self.product_listbox.curselection()
        if selected_index:
            product = self.database.get_products()[selected_index[0]]
            self.cart.add_product(product)
            messagebox.showinfo("Success", f"{product.name} added to cart.")
    def view_cart(self):
        cart_items = self.cart.view_cart()
        if cart_items:
            messagebox.showinfo("Cart", "\n".join([f"{item.name} - ${item.price:.2f}" for item in cart_items]))
        else:
            messagebox.showinfo("Cart", "Your cart is empty.")
    def checkout(self):
        total = self.cart.checkout()
        messagebox.showinfo("Checkout", f"Total amount: ${total:.2f}")
    def run(self):
        self.root.mainloop()