""" student = {
    "name": "Rolf",
    "grades": (89, 90, 93, 78, 90)
}


def average_grade(seq):
    return sum(seq) / len(seq)


print(average_grade(student["grades"])) """

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (89, 90, 93, 78, 90))
student2 = Student("Rolf", (100, 100, 93, 78, 90))

print(student.name)
print(student.grades)
print(Student.average_grade(student))
print(student.average_grade())
print(student2.average_grade())
