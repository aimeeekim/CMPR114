import employeeclass

def main():
	Employee1 = employeeclass.Employee("Susan Meyers", "47899", "Accounting", "Vice President")
	Employee2 = employeeclass.Employee("Mark Jones", "39119", "IT", "Programmer")
	Employee3 = employeeclass.Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

	print(f"\nEmployee 1's name is: {Employee1.get_name()}, ID: {Employee1.get_ID()}, Department: {Employee1.get_department()}, Title: {Employee1.get_title()}")
	print(f"\nEmployee 2's name is: {Employee2.get_name()}, ID: {Employee2.get_ID()}, Department: {Employee2.get_department()}, Title: {Employee2.get_title()}")
	print(f"\nEmployee 3's name is: {Employee3.get_name()}, ID: {Employee3.get_ID()}, Department: {Employee3.get_department()}, Title: {Employee3.get_title()}")

main()