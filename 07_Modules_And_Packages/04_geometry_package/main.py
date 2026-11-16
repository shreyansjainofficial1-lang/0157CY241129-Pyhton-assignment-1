from geometry.circle import area as circle_area, circumference
from geometry.rectangle import area as rectangle_area, perimeter

radius = float(input("Enter circle radius: "))
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

if radius < 0 or length < 0 or width < 0:
    print("Dimensions cannot be negative.")
else:
    print(f"Circle area: {circle_area(radius):.2f}")
    print(f"Circle circumference: {circumference(radius):.2f}")
    print(f"Rectangle area: {rectangle_area(length, width):.2f}")
    print(f"Rectangle perimeter: {perimeter(length, width):.2f}")
