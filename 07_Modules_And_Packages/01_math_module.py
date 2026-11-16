import math

number = float(input("Enter a non-negative number for square root: "))
base = float(input("Enter base for power: "))
exponent = float(input("Enter exponent: "))
factorial_number = int(input("Enter a non-negative integer for factorial: "))
angle_degrees = float(input("Enter angle in degrees for trigonometry: "))

if number < 0 or factorial_number < 0:
    print("Square root and factorial inputs must be non-negative.")
else:
    print("Square root:", math.sqrt(number))
    print("Power:", math.pow(base, exponent))
    print("Factorial:", math.factorial(factorial_number))

angle_radians = math.radians(angle_degrees)
print("Sine:", math.sin(angle_radians))
print("Cosine:", math.cos(angle_radians))
print("Tangent:", math.tan(angle_radians))
