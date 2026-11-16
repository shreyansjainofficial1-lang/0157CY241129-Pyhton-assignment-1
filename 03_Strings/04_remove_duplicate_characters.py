text = input("Enter a string: ")
result = ""
seen = set()

for char in text:
    if char not in seen:
        result += char
        seen.add(char)

print("After removing duplicate characters:", result)
