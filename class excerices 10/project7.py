class Employee:
	def __init__ (self, name, number):
		self.__name = name
		self.__number = number

	def set_name(self, name):
		self.__name = name

	def set_number(self, number):
		self.__number = number

	def get_name(self):
		return self.__name

	def get_number(self):
		return self.__number

class ProductionWorker(Employee):
	def __init__(self, name, number, shift, rate):
		super().__init__(name, number)
		self.__shift = shift
		self.__rate = rate

	def set_shift(self, shift):
		self.__shift = shift

	def set_rate(self, rate):
		self.__rate = rate

	def get_shift(self):
		return self.__shift

	def get_rate(self):
		return self.__rate

name = input("\nName: ")
number = input("Number: ")
shift = input("Shift(1 - Day, 2 - Night): ")
rate = input("Hourly rate: ")

worker = ProductionWorker(name, number, shift, rate)

print(f"\nName: {worker.get_name()}")
print(f"Number: {worker.get_number()}")
print(f"Shift: {worker.get_shift()}")
print(f"Rate: {worker.get_rate()}")