string = input("Enter string: ")

capital = False
ch = string[0]

if ch.isupper():
	capital = True

count = 0
result = ""
for i in string:
	if i.isupper() and count > 0:
		result += " "
		result += i.lower()
	else:
		result += i
	count+=1

print(result)