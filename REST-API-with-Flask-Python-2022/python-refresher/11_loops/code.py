number = 7

# user_input = input("Would you like to play? (Y/n) ")

# while user_input != 'n':
#     user_number = int(input("Guess our number: "))

#     if user_number == number:
#         print("You guessed correctly")
#     elif abs(user_number - number) == 1:
#         print("You were off by one")
#     else:
#         print("Sorry, it's wrong")

#     user_input = input("Would you like to play? (Y/n) ")

# Shift + Alt + A
""" while True:
	user_input = input("Would you like to play? (Y/n) ")

	if user_input == 'n':
		break

	user_number = int(input("Guess our number: "))

	if user_number == number:
		print("You guessed correctly")
	elif abs(user_number - number) == 1:
		print("You were off by one")
	else:
		print("Sorry, it's wrong") """

""" friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
	print(f"{friend} is my friend") """

""" for friend in range(4):
	print(f"{friend} is my friend") """

grades = [35, 67, 98, 100, 100]
# total = 0

# amount = len(grades)

# for grade in grades:
#     total += grade

# avg = total / amount
# print(f"Average: {avg:.2f}")

print(sum(grades) / len(grades))
