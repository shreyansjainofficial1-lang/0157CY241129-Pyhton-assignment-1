def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for value in range(1, number + 1):
        result *= value
    return result

n = int(input("Enter a non-negative integer: "))
print("Factorial:", factorial(n))
