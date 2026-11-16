start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

if start > end:
    start, end = end, start

print("Palindrome numbers:")
for number in range(max(0, start), end + 1):
    if str(number) == str(number)[::-1]:
        print(number, end=" ")
print()
