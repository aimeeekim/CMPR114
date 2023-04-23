class Employee:
	def __init__(self, name, ID, department, title):
		self.__name = name
		self.__ID = ID
		self.__department = department
		self.__title = title
	
	def set_name(self, name):
		self.__name = name

	def set_ID(self, ID):
		self.__ID = ID
	
	def set_department(self, department):
		self.__department = department
	
	def set_title(self, title):
		self.__title = title

	def get_name(self):
		return self.__name

	def get_ID(self):
		return self.__ID

	def get_department(self):
		return self.__department
	def get_title(self):
		return self.__title