import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, world!")


root = tk.Tk()
root.title("hello")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="left", fill="x", expand=True)

root.mainloop()

