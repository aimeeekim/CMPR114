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

main()