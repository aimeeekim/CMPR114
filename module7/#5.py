def main():
	# Create a variable to use to hold the ocunt.
	# The variable must start with 0.
	count = 0

	# Get a string from the user
	my_string = input('Enter a sentence: ')

	# Count the Ts
	for ch in my_string:
		if ch == 'T' or ch == 't':
			count += 1

	# Print the result.
	print(f'The letter T appears {count} times.')

# Call the main function.
if __name__ == '__main__':
	main()
