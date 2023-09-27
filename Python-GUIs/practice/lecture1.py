import tkinter as tk

root = tk.Tk()
root.title("Window Basics!")
root.geometry("250x700")
root.resizable(0, 0)
root.config(bg='blue')
root.iconbitmap("../thinking.ico")

top = tk.Toplevel()
top.title("Second Window")
top.geometry("200x200+500+50")
top.config(bg='#123456')

root.mainloop()
