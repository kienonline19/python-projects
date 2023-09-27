import os
import tkinter as tk
from tkinter import ttk, filedialog


def save_file():
    file_path = filedialog.asksaveasfilename()

    try:
        file_name = os.path.basename(file_path)
        text_widget = root.nametowidget(notebook.select())
        content = text_widget.get("1.0", "end-1c")

        with open(file_path, 'w') as file:
            file.write(content)
    except (AttributeError, FileNotFoundError):
        print("Save operation cancelled!")
        return

    notebook.tab("current", text=file_name)


def open_file():
    file_path = filedialog.askopenfilename()

    try:
        file_name = os.path.basename(file_path)

        with open(file_path, 'r') as file:
            content = file.read()

    except (AttributeError, FileNotFoundError):
        print("Open operation cancelled")
        return

    create_file(content, file_name)


def create_file(content='', title="Untitled"):
    text_area = tk.Text(notebook)
    text_area.insert("end", content)
    text_area.pack(fill="both", expand=True)

    notebook.add(text_area, text=title)
    notebook.select(text_area)


root = tk.Tk()
root.title("Teclado Text Editor")
root.option_add("*tearOff", False)

main = ttk.Frame(root)
main.pack(fill="both", expand=True, padx=1, pady=(4, 0))

menu_bar = tk.Menu()
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(menu=file_menu, label="File")

file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open...", command=open_file)

notebook = ttk.Notebook(main)
notebook.pack(fill="both", expand=True)

create_file()
create_file()

root.mainloop()
