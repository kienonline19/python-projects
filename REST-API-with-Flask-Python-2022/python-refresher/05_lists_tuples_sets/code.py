l = ["Rolf", "Bob", "Jen", "David"]
t = ("Rolf", "Bob", "Jen", "David")
s = {"Rolf", "Bob", "Jen", "David"}

print(l[0])
print(t[0])

l[0] = "Smith"
print(l)

# t[0] = "Kenny" - TypeError
print(t)

l.append("Jose")
print(l)

l.remove("Bob")
print(l)

s.add("Henry")
s.add("Henry")

print(s)
