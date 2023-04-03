str = input("Enter string: ")
consonants = 0
vowels = 0

for i in str:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'
       or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels += 1
    elif( i == ' '):
        continue
    else:
        consonants += 1
 
print(f"Total number of vowels in string = {vowels}")
print(f"Total number of consonants in string = {consonants}")