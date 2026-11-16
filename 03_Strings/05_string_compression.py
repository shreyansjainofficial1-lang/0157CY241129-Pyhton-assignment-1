text = input("Enter a string: ")

if not text:
    print("Compressed string: ")
else:
    compressed = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(text[i - 1] + str(count))
            count = 1

    compressed.append(text[-1] + str(count))
    print("Compressed string:", "".join(compressed))
