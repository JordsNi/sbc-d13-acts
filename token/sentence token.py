#Sentence Tokenization
special_char = ['@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','\ ','|','{','}','~',':',']']
sudlanan = []
word = ""
words = input("Enter a sentence: ").lower()
for i in words:
    if i in special_char :
        sudlanan.append(word)
        word = ""
    elif i  == "'":
        word += i
    else:
        word += i
print(sudlanan)
