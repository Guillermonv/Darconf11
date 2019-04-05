text = open('docs/words.txt').read()
words = text.split()
word_count = {} #word_count = {'word': 1}
for word in words: # para cada una de las palabras en la lista de palabras
    count = word_count.get(word, 0) # get dice que busque el valor de la palabra word y si no le encuentra retorne 0
    count += 1 # incremento 1
    word_count[word] = count # le asigno a la palabra que esta en la lista +1

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    print(word, word_count[word])