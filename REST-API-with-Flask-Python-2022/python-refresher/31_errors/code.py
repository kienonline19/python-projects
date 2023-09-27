def divide(dividend, divisor):
    # if divisor == 0:
    #     print("Divisor cannot be 0.")
    #     return
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


""" # divide(15, 0)
grades: list[int] = [23]

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    # print("There are no grades yet in your list.")
    print(e)
except ValueError as e:
    print(e)
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you!") """


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": [12]},
    {"name": "Jen", "grades": [100, 90]}
]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades), len(grades))
        print(f"{name} averaged {average}.")
except ZeroDivisionError:
    print(f"ERROR: {name} has no grades!")
else:
    print("-- All student averages calculated --")
finally:
    print("-- End of student average calculation --")
