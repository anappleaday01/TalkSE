'''
This is the main file for the Hi Application. It creates a GUI that displays a button,
and when clicked, it shows a message saying "Hi".
'''
import tkinter as tk
from tkinter import messagebox
class MainApp:
    '''
    MainApp class to create the main application window.
    '''
    def __init__(self, master):
        '''
        Initializes the main window and sets up the GUI components.
        '''
        self.master = master
        master.title("Say Hi Application")
        self.label = tk.Label(master, text="Press the button to say hi!")
        self.label.pack(pady=10)
        self.say_hi_button = tk.Button(master, text="Say Hi", command=self.say_hi)
        self.say_hi_button.pack(pady=10)
    def say_hi(self):
        '''
        Displays a message box with the text "Hi".
        '''
        messagebox.showinfo("Greeting", "Hi")
def main():
    '''
    The entry point of the application.
    '''
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()