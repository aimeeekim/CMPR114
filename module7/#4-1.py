import csv

def main():

	size = int(input("\nEnter the number of test scores: "))
	scores = []

	# Input the test scores
	for i in range(0, size):
		test = float(input("Enter score: "))
		scores.append(test)

	# Create CSV file using scores array
	fileName = "testScores.csv"
	with open(fileName, 'w', newline = '\n' ) as csvfile:
		#creating a csv write object
		csvwriter = csv.writer(csvfile)

		# writing the data rows
		csvwriter.writerow(scores)

	csvfile.close()

	# Open the file.
	csv_file = open('testScores.csv', 'r')

	# Read the file's lines into a list.
	lines = csv_file.readlines()

	# Close the file
	csv_file.close()

	# Process the lines.
	for line in lines: 
		# Get the test scores as tokens.
		tokens = line.split (',')
		# Calculate the total of the test scores.
		total = 0.0
		for token in tokens:
			total += float(token)
		
		# Calculate the average of the test scores.
		average = total/len(tokens)
		print(f'Average: {average}')
# Execute the main function.
if __name__ == '__main__':
	main()
