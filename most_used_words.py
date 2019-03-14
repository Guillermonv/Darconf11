text = open('docs/words.txt').read()
words = text.split()
word_count = {}
for word in words:
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])