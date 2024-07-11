#Letter Tokenization
sudlanan = []
word = ""
words = input("Enter a sentence: ")
for i in words:
        word += i
        sudlanan.append(word)
        word = ""
print(sudlanan)
