units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Units cannot be negative.")
else:
    if units <= 100:
        bill = units * 5
    elif units <= 300:
        bill = 100 * 5 + (units - 100) * 7
    else:
        bill = 100 * 5 + 200 * 7 + (units - 300) * 10

    surcharge = bill * 0.05 if bill > 2000 else 0
    total = bill + surcharge

    print(f"Energy bill: Rs. {bill:.2f}")
    print(f"Surcharge: Rs. {surcharge:.2f}")
    print(f"Total bill: Rs. {total:.2f}")
