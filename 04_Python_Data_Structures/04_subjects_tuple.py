subjects = ("English", "Mathematics", "Physics", "Chemistry", "Computer Science")

print("Subjects:", subjects)
print("Third subject:", subjects[2])
print("Total subjects:", len(subjects))

subject = input("Enter a subject to find its index: ")
if subject in subjects:
    print("Index:", subjects.index(subject))
else:
    print("Subject not found.")
