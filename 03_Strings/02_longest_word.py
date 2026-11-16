sentence = input("Enter a sentence: ")
words = sentence.split()

if not words:
    print("No words found.")
else:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
