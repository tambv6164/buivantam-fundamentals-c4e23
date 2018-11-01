counts = {}
raw_word = input("Type some thing you want to count letter: ")
word = raw_word.replace(" ", "").lower()

for letter in word:
    counts[letter] = counts.get(letter, 0) + 1

items = list(counts.items())
items.sort()

for (k, v) in items:
    print(k, v)
