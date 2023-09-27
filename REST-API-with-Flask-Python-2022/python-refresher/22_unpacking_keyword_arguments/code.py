""" def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25) """


""" def named(name, age):
    print(name, age)


def named(**kwargs):
    print(kwargs)


def print_nicely(**kwargs):
    named(**kwargs)

    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


# details = {'name': 'Bob', 'age': 25}
# named(**details)

print_nicely(name='Bob', age=25) """

""" def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, name='Bob', age=25) """

"""
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
"""


def myfunction(**kwargs):
    print(kwargs)


myfunction(**"Bob")  # Error: must be mapping
myfunction(**None)  # Error
