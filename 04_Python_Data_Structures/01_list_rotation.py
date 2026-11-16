numbers = list(map(int, input("Enter list elements separated by spaces: ").split()))
direction = input("Rotate left or right? ").strip().lower()
k = int(input("Enter number of positions (k): "))

if numbers:
    k %= len(numbers)
    if direction == "left":
        rotated = numbers[k:] + numbers[:k]
    elif direction == "right":
        rotated = numbers[-k:] + numbers[:-k] if k else numbers[:]
    else:
        rotated = None
        print("Invalid direction. Choose left or right.")
    if rotated is not None:
        print("Rotated list:", rotated)
else:
    print("The list is empty.")
