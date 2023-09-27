""" def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, 5, operator=divide)
print(result) """
from operator import itemgetter


def search(seq, expected, finder):
    for elem in seq:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}")


friends = [
    {"name": "Rolf Smith", "age": 23},
    {"name": "Adam Wool", "age": 45},
    {"name": "Anne Pun", "age": 36}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))
print(search(friends, "Rolf Smith", lambda friend: friend["name"]))
print(search(friends, "Rolf Smith", itemgetter("name")))
