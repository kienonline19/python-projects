"""
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

print(abroad.difference(friends))

locals = {"Rolf"}
abroad = {"Bob", "Anne"}

print(locals.union(abroad))
"""

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)

print(art.symmetric_difference(science))
