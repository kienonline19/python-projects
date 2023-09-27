""" a = []
b = []

a.append(35)

print(a)
print(b)

print(id(a))
print(id(b)) """

""" a = ()
print(id(a))

a += (15,)
print(id(a)) """

""" a = 8597
b = 8597

print(id(a))
print(id(b))

a = 8598
print(a, b) """

a = "hello"
b = a

print(id(a) == id(b))

a += "world"
print(a == b)

print(id(a) == id(b))

