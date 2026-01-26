class Student:
    def __init__(self, name, group, avg_grade):
        self.name = name
        self.group = group
        self.avg_grade = avg_grade

    def show_info(self):
        print("Ім'я:", self.name)
        print("Група:", self.group)
        print("Середній бал:", self.avg_grade)
        print("------")

s1 = Student("ім'я1", "IPZ-1", 80)
s2 = Student("ім'я1", "IPZ-2", 90)
s3 = Student("ім'я1", "IPZ-3", 100)

s1.show_info()
s2.show_info()
s3.show_info()
