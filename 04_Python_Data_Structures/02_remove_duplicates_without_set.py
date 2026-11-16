numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("List after removing duplicates:", unique)
