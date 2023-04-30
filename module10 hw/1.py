class Employee:
    def __init__(self, name, empNum):
        self.__name = name
        self.__empNum = empNum
    
    def set_name(self, name):
        self.__name = name
    def set_empNum(self, empNum):
        self.__empNum = empNum

    def get_name(self):
        return self.__name
    def get_empNum(self):
        return self.__empNum
    
    def __str__(self):
        return f'Name is: {self.__name}\nThe employee Number is: {self.__empNum}\n'


class Supervisor(Employee):
	def __init__(self, name, number, salary, bonus):
		super().__init__(name, number)
		self.__salary = salary
		self.__bonus = bonus

	def set_salary(self, salary):
		self.__salary = salary
	
	def set_bonus(self, bonus):
		self.__bonus = bonus

	def get_salary(self):
		return self.__salary

	def get_bonus(self):
		return self.__bonus

name = input("\nEnter the name: ")
number = input("Enter the number: ")
salary = float(input("Enter the salary: "))
bonus = float(input("Enter the bonus: "))

supervisor = Supervisor(name, number, salary, bonus)

print(f"\nName is: {supervisor.get_name()}")
print(f"Number is: {supervisor.get_number()}")
print(f"Salary is: ${supervisor.get_salary():,.2f}")
print(f"Bonus is: ${supervisor.get_bonus():,.2f}")