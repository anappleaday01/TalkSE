'''
This is the main file for the "Say Hi" application using tkinter.
It creates a simple GUI that displays a button. When the button is clicked,
it shows a message saying "Hi!". It also handles the window close event
with a confirmation dialog.
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
        self.label = tk.Label(master, text="Welcome to the Say Hi App!")
        self.label.pack(pady=10)
        self.greet_button = tk.Button(master, text="Say Hi", command=self.say_hi)
        self.greet_button.pack(pady=10)
        master.protocol("WM_DELETE_WINDOW", self.confirm_exit)  # Add this line for exit confirmation
    def say_hi(self):
        '''
        Displays a message box with the text "Hi!" when the button is clicked.
        '''
        messagebox.showinfo("Greeting", "Hi!")
    def confirm_exit(self):
        '''
        Confirms if the user really wants to exit the application.
        '''
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.master.destroy()
def main():
    '''
    Main function to run the application.
    '''
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
if __name__ == "__main__":
    main()