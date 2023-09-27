import tkinter as tk

root = tk.Tk()
root.title("Radio Button Basics")
root.iconbitmap("../thinking.ico")
root.geometry("350x350")
root.resizable(False, False)


def make_label():
    if number.get() == 1:
        output_label = tk.Label(output_frame, text="1 one 1")
    elif number.get() == 2:
        output_label = tk.Label(output_frame, text="2 one 2")

    output_label.pack()


input_frame = tk.LabelFrame(root, text="This is fun!", width=350, height=100)
input_frame.pack(padx=10, pady=10)

number = tk.IntVar()
number.set(1)
radio1 = tk.Radiobutton(input_frame, text="Print the number 1!", variable=number, value=1)
radio2 = tk.Radiobutton(input_frame, text="Print the number 2!", variable=number, value=2)

radio1.grid(row=0, column=0, padx=10, pady=10)
radio2.grid(row=0, column=1, padx=10, pady=10)

print_button = tk.Button(input_frame, text="Print the number!", command=make_label)
print_button.grid(row=1, column=0, columnspan=2, pady=5)

output_frame = tk.Frame(root, width=350, height=250)
output_frame.pack(padx=10, pady=10)

root.mainloop()
