class Person:
	def __init__(self, name, address, telephone):
		self.__name = name
		self.__address = address
		self.__telephone = telephone

	def set_name(self, name):
		self.__name = name

	def set_address(self, address):
		self.__address = address

	def set_phone_number(self,telephone):
		self.__telephone = telephone

	def get_name(self):
		return self.__name

	def get_address(self):
		return self.__address

	def get_phone_number(self):
		return self.__telephone

class Customer(Person):
	def __init__(self, name, address, telephone, customer_number, mail):
		super().__init__(name, address, telephone)
		self.__customer_number = customer_number
		self.__mail = mail

	def set_customer_number(self, customer_number):
		self.__customer_number = customer_number

	def set_mail(self, mail):
		self.__mail = mail

	def get_customer_number(self):
		return self.__customer_number

	def get_mail(self):
		return self.__mail

name = input("\nName is: ")
address = input("Address is: ")
phone = input("Enter telephone number: ")
customer_number = input("Enter customer number: ")
mail = int(input("Would you like to be on the mailing list? (0 - NO and 1 - YES):"))

if mail == 0:
	mail = False
elif mail == 1:
	mail = True
else:
	mail = True

customer = Customer(name, address, phone , customer_number, mail)

print(f"\nName is: {customer.get_name()}")
print(f"Address is: {customer.get_address()}")
print(f"Telehone Number is: {customer.get_phone_number()}")
print(f"Customer Number is: {customer.get_customer_number()}")
print(f"Mailing List is: {customer.get_mail()}")