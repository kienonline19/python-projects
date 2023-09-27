name = "Bob"
greeting = "Hello, {}"

print(f"Hello, {name}")

# Template strings with .format()
print(greeting.format(name))

name = "Rolf"
print(f"Hello, {name}")
print(greeting.format(name))

print('-' * 30)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)
