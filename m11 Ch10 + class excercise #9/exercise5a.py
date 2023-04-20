class BankAccount:

	def __init__(self, bal):
		self.__balance = bal

	def deposit(self, amount):
		# add the balance
		self.__balance += amount

	def withdraw (self, amount):
		if self.__balance >= amount:
			
			# subtract the balance
			self.__balance -=amount
		
		else:
			print("\nError: Insufficient funds")

	def get_balance(self):
		return self.__balance