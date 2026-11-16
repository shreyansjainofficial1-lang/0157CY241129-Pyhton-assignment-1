count = int(input("Enter number of students: "))
students = {}

for _ in range(count):
    name = input("Student name: ")
    marks = float(input(f"Marks for {name}: "))
    students[name] = marks

if not students:
    print("No student records entered.")
else:
    topper = max(students, key=students.get)
    average = sum(students.values()) / len(students)
    failures = [name for name, mark in students.items() if mark < 33]

    print("Marks:", students)
    print("Topper:", topper, "-", students[topper])
    print(f"Average marks: {average:.2f}")
    print("Failed students:", failures if failures else "None")
