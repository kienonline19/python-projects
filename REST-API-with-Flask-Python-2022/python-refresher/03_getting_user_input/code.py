name = input("enter your name: ")
print(name)

print('-' * 50)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)

square_metres = square_feet / 10.8

print(f"{size_input} ft^2 = {square_metres:.2f} m^2")
