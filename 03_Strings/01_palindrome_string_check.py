text = input("Enter a string: ")
cleaned = "".join(char.lower() for char in text if not char.isspace())

if cleaned == cleaned[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")
