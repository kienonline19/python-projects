def add(x, y=8):
    print(x + y)


# add(5, 8)
# add(5)
# add(x=6)
# add(y=5) - TypeError
# add(x=6, y=10)
# add(x=1, 2) - SyntaxError

""" def add(x=1, y):
    print(x + y) SyntaxError """


default_y = 8


def add(x, y=default_y):
    total = x + y
    print(total)


default_y = 10
add(23)
