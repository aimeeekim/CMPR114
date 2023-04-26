class Insect:
	def __init__(self, wings, antennae, eyes):
		self.__wings = wings
		self.__antennae = antennae
		self.__eyes = eyes
		

	def set_wings(self, wings):
		self.__wings = wings

	def set_antennae(self, antennae):
		self.__antennae = antennae

	def set_eyes(self, eyes):
		self.__eyes = eyes

	def get_wings(self):
		return self.__wings

	def get_antennae(self):
		return self.__antennae

	def get_eyes(self):
		return self.__eyes


class Bees(Insect):
	def __init__(self, wings, antennae, eyes, sting):

		super().__init__(wings, antennae, eyes)

		self.__sting = sting

	def set_sting(self, sting):
		self.__sting = sting

	def get_sting(self):
		return self.__sting

class GrassHoppers(Insect):
	def __init__(self, wings, antennae, eyes, jump):

		super().__init__(wings, antennae, eyes)

		self.__jump = jump
	def set_jump(self, jump):
		self.__jump = jump

	def get_jump(self):
		return self.__jump

bees = Bees("has a stinger","has Antennaes", "has compound eyes", "has a wing")
print(f"Bees: {bees.get_wings()}")
print(f"Bees: {bees.get_antennae()}")
print(f"Bees: {bees.get_eyes()}")
print(f"Bees: {bees.get_sting()}")

grasshoppers = GrassHoppers("has jumping abilities","has compound eyes", "has Antennaes", "has wings")
print(f"\nGrasshoppers: {grasshoppers.get_wings()}")
print(f"Grasshoppers: {grasshoppers.get_antennae()}")
print(f"Grasshoppers: {grasshoppers.get_eyes()}")
print(f"Grasshoppers: {grasshoppers.get_jump()}")