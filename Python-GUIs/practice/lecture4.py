import tkinter as tk

root = tk.Tk()
root.title("Entry Basics!")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap("../thinking.ico")


def print_message():
    msg = text_entry.get()
    tk.Label(output_frame, text=msg, bg="red").pack()
    text_entry.delete(0, tk.END)


def count_up(number):
    global value
    tk.Label(output_frame, text=number, bg="red").pack()
    value = number + 1


input_frame = tk.Frame(root, width=500, height=100, bg="blue")
input_frame.pack(padx=10, pady=10)

output_frame = tk.Frame(root, width=500, height=400, bg="red")
output_frame.pack(padx=10, pady=(0, 10))
output_frame.pack_propagate(False)

text_entry = tk.Entry(input_frame, width=40)
text_entry.grid(row=0, column=0, padx=5, pady=5)
input_frame.grid_propagate(False)

print_button = tk.Button(input_frame, text="Print",
                         width=15, command=print_message)
print_button.grid(row=0, column=1, padx=5, pady=5)

value = 0

count_button = tk.Button(input_frame, text="Count", width=15, command=lambda: count_up(value))
count_button.grid(row=1, column=0, sticky="WE", padx=5, pady=5)

root.mainloop()
