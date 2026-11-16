def sum_n(number):
    if number < 0:
        raise ValueError("Enter a non-negative integer.")
    if number == 0:
        return 0
    return number + sum_n(number - 1)

n = int(input("Enter n: "))
print("Sum:", sum_n(n))
