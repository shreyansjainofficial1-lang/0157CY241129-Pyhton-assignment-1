n = int(input("Enter n (the list should contain numbers from 1 to n): "))
numbers = list(map(int, input(f"Enter {n - 1} numbers separated by spaces: ").split()))

if len(numbers) != n - 1:
    print(f"Please enter exactly {n - 1} numbers.")
elif any(number < 1 or number > n for number in numbers) or len(set(numbers)) != len(numbers):
    print("Input must contain distinct numbers from 1 to n.")
else:
    missing = n * (n + 1) // 2 - sum(numbers)
    print("Missing number:", missing)
