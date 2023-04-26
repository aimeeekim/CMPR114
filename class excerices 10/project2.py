class person:
	def __init__(self, name, age, address, city, state, zipcode):
		self.name = name
		self.age = age
		self.address = address
		self.city = city
		self.state = state
		self.zipcode = zipcode


class Student(person):
	def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):

		super().__init__(name, age, address, city, state, zipcode)

		self.studentID = studentID
		self.GPA = GPA

class Teacher(person):
	def __init__(self, name, age, address, city, state, zipcode, TeacherID, ClassTeaching):
		super().__init__(name, age, address, city, state, zipcode)

		self.TeacherID = TeacherID
		self.ClassTeaching = ClassTeaching

student = Student("Jane Doe", 25, "2178 Av.", "Buena Park", "CA", "23913", 777, 3.8)
print(f"Student Name: {student.name}")
print(f"Student Age: {student.age}")
print(f"Student Address: {student.address}")
print(f"Student City: {student.city}")
print(f"Student State: {student.state}")
print(f"Student Zip Code: {student.zipcode}")
print(f"Student ID: {student.studentID}")
print(f"Student GPA: {student.GPA}")

teacher = Teacher("Ms. Cantor", 45,"79 Av.", "Irvine", "CA", "92618", 7, "Python")
print(f"\nTeacher Name: {teacher.name}")
print(f"Teacher Age: {teacher.age}")
print(f"Teacher Address: {teacher.address}")
print(f"Teacher City: {teacher.city}")
print(f"Teacher State: {teacher.state}")
print(f"Teacher Zip Code: {teacher.zipcode}")
print(f"Teacher ID: {teacher.TeacherID}")
print(f"Teacher Course: {teacher.ClassTeaching}")