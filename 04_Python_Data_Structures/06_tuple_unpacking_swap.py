items = tuple(input("Enter tuple elements separated by spaces: ").split())

if len(items) < 2:
    print("At least two elements are required.")
else:
    first, *middle, last = items
    swapped = (last, *middle, first)
    print("Original tuple:", items)
    print("After swapping first and last:", swapped)
