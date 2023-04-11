def collect_input():
    rent = input("Enter monthly rent expense: ")
    gas = input("Enter monthly gas expense: ")
    food = input("Enter monthly food expense: ")
    clothing = input("Enter monthly clothing expense: ")
    car = input("Enter monthly car expense: ")

    writeFile(rent, gas, food, clothing, car)

def writeFile(rent, gas, food, clothing, car):
    output_file = open("expense.txt", "w")

    output_file.write(f"Monthly Expense\nRent: ${rent}\nGas: ${gas}\nFood: ${food}\nClothing: ${clothing}\nCar: ${car}")
    print('Your file monthlyexpenses.txt was created.')

def readFile():
    input_file = open("expense.txt", "r")
    
    for line in input_file:
        print(line)

collect_input()
readFile()
