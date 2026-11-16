def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return x * half * half

base = float(input("Enter base: "))
exponent = int(input("Enter integer exponent: "))
if base == 0 and exponent < 0:
    print("Zero cannot have a negative exponent.")
else:
    print("Result:", power(base, exponent))
