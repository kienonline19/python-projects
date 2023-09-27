import tkinter as tk

root = tk.Tk()
root.title("Frame Basics!")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap("../thinking.ico")

pack_frame = tk.Frame(root, bg="red")
pack_frame.pack(fill=tk.BOTH, expand=True)

tk.Label(pack_frame, text="text").pack()
tk.Label(pack_frame, text="text").pack()
tk.Label(pack_frame, text="text").pack()

grid_frame1 = tk.Frame(root, bg="blue")
grid_frame1.pack(fill=tk.X, expand=True)

tk.Label(grid_frame1, text="text").grid(row=0, column=0)
tk.Label(grid_frame1, text="text").grid(row=1, column=1)
tk.Label(grid_frame1, text="text").grid(row=2, column=2)

grid_frame2 = tk.LabelFrame(root, text="Grid System Rules!", borderwidth=5)
grid_frame2.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

tk.Label(grid_frame2, text="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa").grid(row=0, column=0)

root.mainloop()
