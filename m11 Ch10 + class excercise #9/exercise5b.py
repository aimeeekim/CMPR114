import exercise5a

def main():

	start_bal = float(input("Enter the starting balance: "))

	# call the external class name
	savings = classExercise9e1.BankAccount(start_bal)

	pay = float(input("How much were you paid this week? "))
	print("That amount will be placed into your account")
	
	# the deposit function is passing one argument called amount
	#so we have to fulfill that argument with pay
	savings.deposit(pay)

	#retrieved the balance frfom the external class
	print(f"\nYour account balance is ${savings.get_balance():,.2f}")

	cash = float(input("\nHow much would you like to withdrawal? "))
	print("That amount will be withdrawn from your account" )

	# calls the withdraw function
	# and fulfills the one argument that is passed with cash
	savings.withdraw(cash)

	#retrieve the balance from external class
	print(f"\nYour account balance is ${savings.get_balance():,.2f}")

main()