""" def add(x, y):
    return
    return x + y
    print(x + y) """


# add(5, 8)
# result = add(5, 8)
# print(result)
# print(add(1, 2))  # 3


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


result = divide(15, 3) * 4
print(result)

result = divide(15, 0) * 5
print(result)
