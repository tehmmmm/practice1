sentence = "the cat and the hat and the bat"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
most_common = max(word_count, key=word_count.get)
print(most_common,word_count[most_common])

