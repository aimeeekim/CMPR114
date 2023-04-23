import retailitemclass

def main():
	item1 = retailitemclass.RetailItem("Jacket", 12, 59.95)
	item2 = retailitemclass.RetailItem("Designer Jeans", 40, 34.95)
	item3 = retailitemclass.RetailItem("Shirt", 20,24.95)

	print(f"\nItem 1: \nDescription: {item1.get_description()}\nUnits in Inventory: {item1.get_units()}\nPrice: ${item1.get_price()}")
	print(f"\nItem 2: \nDescription: {item2.get_description()}\nUnits in Inventory: {item2.get_units()}\nPrice: ${item2.get_price()}")
	print(f"\nItem 3: \nDescription: {item3.get_description()}\nUnits in Inventory: {item3.get_units()}\nPrice: ${item3.get_price()}")
main()