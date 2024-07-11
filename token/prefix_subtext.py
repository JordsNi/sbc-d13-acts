#Prefix Tokenization
special_char = ['un','im','ir','re','mis','dis']
sudlanan = []
word = ""
words = input("Enter a sentence: ")
for i in words:
    if word in special_char :
        sudlanan.append(word)
        rep = '#'*len(word)
        word = rep
        word += i
    else:
        word += i
sudlanan.append(word)
print(sudlanan)