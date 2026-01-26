students = [
    {"Name": "ім'я1", "Surname": "прізвище1", "Grades": [90, 85, 30, 25, 100]},
    {"Name": "ім'я2", "Surname": "прізвище2", "Grades": [45, 0, 90, 10, 95]},
    {"Name": "ім'я3", "Surname": "прізвище3", "Grades": [41, 33, 87, 54, 98]},
    {"Name": "ім'я4", "Surname": "прізвище4", "Grades": [68, 91, 18, 63, 97]}
]

print("Name\tSurname\tAverage")
print("-" * 30)

for s in students:
    total = sum(s["Grades"])       
    avg = total / len(s["Grades"]) 
    print(s["Name"], "\t", s["Surname"], "\t", round(avg, 2))

print("-" * 30)

num_disc = len(students[0]["Grades"]) 

for i in range(num_disc):
    summ = 0
    for st in students:
        summ += st["Grades"][i]           
    avg_disc = summ / len(students)     
    print("Discipline", i + 1, ":", round(avg_disc, 2))

print("-" * 35)
