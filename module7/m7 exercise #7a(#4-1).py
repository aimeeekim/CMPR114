def main():

	names = ['Howard', 'Jamie', 'Jill']

	print("The list before the insert or remove function")

	print(names)
	
	NameRemove = input("Enter the name to remove: ")

	names.insert(0, 'Joe') # insert the new name at element 0, moving or shifting element 0 to 1
	names.remove(NameRemove) # removes the name from the list
	print("The list after the insert")
	print(names)

main()

def total():
	numbers = [1,2,3,4,5,6,7,8,9,10]
	sum = 0

	for value in numbers:
		sum+=value # total the numbers in the list
	average = sum/len(numbers) # the lens function returns the number of items in the list
	print("The total is", sum, " the average is", average)
	output = open("numbersProject.txt", 'w')
	output.writelines(str(numbers) + '\n')
	output.writelines(str(sum) + '\n')
	output.writelines(str(average) + '\n')

total()
