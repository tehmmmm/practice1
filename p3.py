# Squares of even numbers
squares = []
for num in range(1, 11):
    if num % 2 == 0:
        squares.append(num * num)
print(squares)
words = ["ai", "python", "data"]
lengths = {}
for word in words:
    lengths[word] = len(word)
print(lengths)
word = "banana"
letters = sorted(set(word))
print(letters)

