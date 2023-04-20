class Students:
	
	def GetInformation(self):
		print("\nStudent Last name is " + self.Lastname)
		print("Student First name is " + self.Firstname)
		print("studen Address is " + self.Address)
		print("Sstudent City is " + self.City)
		print("student State is " + self.State)
		print("student Zipcode is " + self.Zipcode)

#creates the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345"

#creates the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garen Grove"
Student2.State = "CA"
Student2.Zipcode = "67890"

#creates the Student2 object
Student3 = Students()
Student3.Lastname = input("\nEnter last name: ")
Student3.Firstname = input("Enter first name: ")
Student3.Address = input("Enter address: ")
Student3.City = input("Enter city: ")
Student3.State = input ("Enter state: ")
Student3.Zipcode = input("Enter zip code: ")

Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()