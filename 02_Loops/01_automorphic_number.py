number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    square = number * number
    digits = len(str(number))
    if square % (10 ** digits) == number:
        print(number, "is an Automorphic number.")
    else:
        print(number, "is not an Automorphic number.")
