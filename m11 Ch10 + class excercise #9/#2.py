class Teacher:
	def __init__(self, name, classRoom, course):
		self.name = name
		self.classRoom = classRoom
		self.course = course
	def GetProfessor(self):
		print("\nProfessor Name is: " + self.name)
		print("Professor assigned class is: " + self.classRoom)
		print("Professor is teaching: " + self.course)

Teacher1 = Teacher("Prof. Sim", "A206", "Python Programming" )
Teacher1.GetProfessor()

Teacher2 = Teacher("Prof. Leeds", "M215", "Statistics")
Teacher2.GetProfessor()
