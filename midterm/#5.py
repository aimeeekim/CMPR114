numList = [20,21,22,23,24,25,26,27,28,29,30]
i = 0
sum = 0
avg = 0
for i in numList:
	sum += i
avg = sum/len(numList)
print(f"\nSum is: {sum}")
print(f"\nAverage is: {avg}")