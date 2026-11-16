a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))


x, y = abs(a), abs(b)
if x == 0:
    hcf = y
elif y == 0:
    hcf = x
else:
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    hcf = x


if a == 0 or b == 0:
    lcm = 0
else:
    multiple = max(abs(a), abs(b))
    while multiple % abs(a) != 0 or multiple % abs(b) != 0:
        multiple += 1
    lcm = multiple

print("HCF:", hcf)
print("LCM:", lcm)
