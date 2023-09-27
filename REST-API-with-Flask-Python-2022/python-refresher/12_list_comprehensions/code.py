""" numbers = [1, 3, 5]

doubled_numbers = [x*2 for x in numbers]

print(doubled_numbers) """

friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [f for f in friends if f.lower().startswith('s')]

print(friends is starts_s)
print(friends[0] is starts_s[0])

print("friends:", id(friends), "starts_s:", id(starts_s))

starts_s = friends
print("friends:", id(friends), "starts_s:", id(starts_s))
