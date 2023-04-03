def main():
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	monthlyRain = []

	print("\nEnter the rain fall for each month:")

	index = 0
	for i in months:
		rain = float(input(f"Enter the amount of rain for {i}: "))
		monthlyRain.insert(index, rain)
		index+=1
	totalRain = total(monthlyRain)
	averageRain = totalRain/len(monthlyRain)
	lessRain = min(monthlyRain)
	lessRainIndex = monthlyRain.index(lessRain)
	mostRain = max(monthlyRain)
	mostRainIndex = monthlyRain.index(mostRain)

	print(f"\nThe total rain in the year was: {totalRain}")
	print(f"The average rain in each month is: {averageRain:.2f}")
	print(f"\nThe month with lowest rain was {months[lessRainIndex]} with {lessRain} inches of rain.")
	print(f"\nThe month with highest rain was {months[mostRainIndex]} with {mostRain} inches of rain.")

	write('yearly_rain.txt', monthlyRain, totalRain, months)

def total(numbers):
	sum = 0
	for value in numbers:
		sum+= int(value or 0)
	return sum

def write(name, monthlyRain, total, months):
	index = 0
	output = open(name, 'w')
	for rain in monthlyRain:
		output.writelines(f"{months[index]}: {rain} inches\n")
		index+=1
	output.writelines(f"Total rain: {total:.2f} inches\n")
	output.writelines(f"The average rain on this year was {total/len(months)} inches\n")
	lessRain = min(monthlyRain)
	lessRainIndex = monthlyRain.index(lessRain)
	mostRain = max(monthlyRain)
	mostRainIndex = monthlyRain.index(mostRain)
	
	output.writelines(f"The month with lowest rain was {months[lessRainIndex]} with {lessRain} inches of rain.\n")
	output.writelines(f"The month with highest rain was {months[mostRainIndex]} with {mostRain} inches of rain.\n")
main()