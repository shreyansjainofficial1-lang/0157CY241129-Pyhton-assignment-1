def validate_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Age validated successfully."

try:
    age = int(input("Enter your age: "))
    print(validate_age(age))
except ValueError as error:
    print("Validation error:", error)
