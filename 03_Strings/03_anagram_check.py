first = input("Enter first string: ")
second = input("Enter second string: ")

# Ignore spaces and letter case.
a = sorted(char.lower() for char in first if not char.isspace())
b = sorted(char.lower() for char in second if not char.isspace())

print("The strings are anagrams." if a == b else "The strings are not anagrams.")
