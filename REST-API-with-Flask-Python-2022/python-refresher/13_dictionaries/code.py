""" friend_ages = {
    "Rolf": 24,
    "Adam": 30,
    "Anne": 27
}

friend_ages["Rolf"] = 20

print(friend_ages) """

""" friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]

print(friends[1]["name"]) """

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}%")

student_name = "Jen"

if student_name in student_attendance:
    print(f"{student_name}: {student_attendance[student_name]}%")
else:
    print(f"{student_name} is not a student in this class.")

vals = student_attendance.values()

print(sum(vals) / len(vals))
