import exercise4a

def main():
	name = input("Enter the name: ")
	address = input("Enter the address: ")
	phone = input("Enter the phone: ")
	city = input("Enter the city: ")
	zipcode = input("Enter zipcode: ")
	age = int(input("Enter age: "))

	# calling the first file, then the name of the class 
	# then the name of the function
	# which equals to the input
	v1 = classExercise9d1.Customer.set_name = name
	v2 = classExercise9d1.Customer.set_address = address
	v3 = classExercise9d1.Customer.set_phone = phone
	v4 = classExercise9d1.Customer.set_city = city
	v5 = classExercise9d1.Customer.set_zipcode = zipcode
	v6 = classExercise9d1.Customer.set_age = age

	print (f"\nHello {v1} your address is {v2} {v4}, {v5}. Your phone # is {v3} and your age is {v6}. " )

main()