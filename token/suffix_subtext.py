#Suffix Tokenization
special_char = ['less','ness','tion','ment','ward']
sudlanan = []
word = ""
words = input("Enter a sentence: ")
rev_word = reversed(words)
for i in rev_word:
    word = i + word
    print(word)
if word in special_char:
    sudlanan.append(word)
    rep = '#'*len(word)
    word = rep
    word += i
else:
    word += i
print(sudlanan)