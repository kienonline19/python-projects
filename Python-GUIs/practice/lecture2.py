import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.resizable(0, 0)
root.title("Label Basics!")
root.iconbitmap("../thinking.ico")
root.config(bg="blue")

name_label1 = tk.Label(root, text="Hello, my name is Mike.")
name_label1.pack()

name_label2 = tk.Label(
    root, text="Hello, my name is John.", font=("Arial", 18, "bold"))
name_label2.pack()


name_label3 = tk.Label(root, text="Hello, my name is Paul", bg="#f00")
name_label3.config(font=("Arial", 10))
name_label3.pack(pady=50)

name_label4 = tk.Label(root, text="Hello, my name is Sue", bg="#000", fg="green")
name_label4.pack(pady=(0, 10), ipadx=50, ipady=10, anchor="w")

name_label5 = tk.Label(root, text="Hello, my name is Pat", fg="#123456", bg="#fff")
name_label5.pack(fill="both", padx=10, pady=10, expand=True)

root.mainloop()
