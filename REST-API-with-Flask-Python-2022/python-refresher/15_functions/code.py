""" def hello():
    print("Hello!")


hello() """
""" print("Welcome to the age in seconds program!")


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")


user_age_in_seconds()

print("Goodbye!") """


# Avoid
""" def print():
    print("Hello world!")


print() """

""" friends = ["Rolf", "Bob"]


def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]
    print(friends)


add_friend() """

""" say_hello()


def say_hello():
    print("Hello!") """
friends = []


def add_friend():
    friends.append("Rolf")


add_friend()
add_friend()
add_friend()

print(friends)
