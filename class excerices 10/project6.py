import project3a

def main():
	used_car = project3a.Automobiles("Audi", 2022, 45000, 80000.0, 4)
	used_car2 = project3a.Automobiles("Honda", 2022, 45000, 80000.0, 4)

	print(f"Make: {used_car.get_make()}")
	print(f"Model: {used_car.get_model()}")
	print(f"Mileage: {used_car.get_mileage()}")
	print(f"Price: {used_car.get_price()}")
	print(f"Doors: {used_car.get_doors()}")

	print(f"\nMake: {used_car2.get_make()}")
	print(f"Model: {used_car2.get_model()}")
	print(f"Mileage: {used_car2.get_mileage()}")
	print(f"Price: {used_car2.get_price()}")
	print(f"Doors: {used_car2.get_doors()}")

	truck = project3a.Automobiles("Toyota", "Tacoma", 40000, 12000.0, 4)
	suv = project3a.Automobiles("Volvo", "SE", 30000, 18500.0, 4)
	electric = project3a.Automobiles("Tesla", "Model X", 12000, 86000, 4)

	print(f"\nMake: {truck.get_make()}")
	print(f"Model: {truck.get_model()}")
	print(f"Mileage: {truck.get_mileage()}")
	print(f"Price: {truck.get_price()}")
	print(f"Doors: {truck.get_doors()}")

	print(f"\nMake: {suv.get_make()}")
	print(f"Model: {suv.get_model()}")
	print(f"Mileage: {suv.get_mileage()}")
	print(f"Price: {suv.get_price()}")
	print(f"Doors: {suv.get_doors()}")

	print(f"\nMake: {electric.get_make()}")
	print(f"Model: {electric.get_model()}")
	print(f"Mileage: {electric.get_mileage()}")
	print(f"Price: {electric.get_price()}")
	print(f"Doors: {electric.get_doors()}")
main()