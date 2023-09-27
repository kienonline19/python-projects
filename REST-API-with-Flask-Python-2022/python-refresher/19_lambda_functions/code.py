""" def add(x, y):
    return x + y


print(add(5, 7))
 """

""" add = lambda x, y: x + y
print(add(5, 7))

print((lambda x, y: x + y)(5, 7)) """

def double(x):
    return x * 2


seq = [1, 3, 5, 9]
doubled = [double(n) for n in seq]

print(doubled)

doubled = list(map(double, seq))
print(doubled)

doubled = list(map(lambda x: x*2, seq))
print(doubled)
