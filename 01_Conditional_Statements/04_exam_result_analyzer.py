marks = []
for subject in range(1, 6):
    mark = float(input(f"Enter marks for subject {subject} (0-100): "))
    if not 0 <= mark <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print(f"Total marks: {total:.2f}/500")
print(f"Percentage: {percentage:.2f}%")

if any(mark < 33 for mark in marks):
    print("Result: Fail")
elif percentage >= 60:
    print("Result: First Division")
elif percentage >= 50:
    print("Result: Second Division")
elif percentage >= 40:
    print("Result: Third Division")
else:
    
    print("Result: Pass (division not specified in the assignment)")
