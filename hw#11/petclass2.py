import petclass

def main():
	name = input("\nEnter pet name: ")
	type = input("Enter pet type: ")
	age = int(input("Enter pet age: "))
	
	Pet1 = petclass.Pet(name, type, age)

	petclass.Pet.set_name = name
	petclass.Pet.set_animal_type = type
	petclass.Pet.set_age = age
	

	print(f"\nThe pet name is {Pet1.get_name()}. The pet type is {Pet1.get_animal_type()}. The pet's age is {Pet1.get_age()}")
main()