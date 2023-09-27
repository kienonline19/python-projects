import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

tk.Label(root, text="Label left", bg="blue").pack(side="left", fill="both", expand=True)

tk.Label(root, text="Label top", bg="green").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label top", bg="red").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label top", bg="yellow").pack(side="top", fill="both", expand=True)
tk.Label(root, text="Label left", bg="pink").pack(side="left", fill="both", expand=True)
tk.Label(root, text="Label left", bg="magenta").pack(side="left", fill="both", expand=True)

root.mainloop()
