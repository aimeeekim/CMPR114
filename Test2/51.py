class Employee:

    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmployeeNumber(self, employee_number):
        self.employee_number = employee_number

    def getEmployeeNumber(self):
        return self.employee_number

    def toString(self):
        return "Employee Name is: " + self.getName() + ", Employee Number is: " + str(self.getEmployeeNumber())
     
class ProductionWorker(Employee):

    def __init__(self, name, employee_number, shift_number, hourly_pay_rate):
        Employee.__init__(self, name, employee_number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    def getShiftNumber(self):
        return self.shift_number

    def getHourlyPayRate(self):
        return self.hourly_pay_rate
    def toString(self):
        return "Worker Name: " + self.getName() + ", Worker Number: " + str(self.getEmployeeNumber()) + \
               ", Worker Shift Number: " + str(self.getShiftNumber()) + \
               ", Worker Hourly Pay Rate: " + str(self.getHourlyPayRate())
     
worker_name = input("Enter worker name: ")
worker_number = int(input("Enter worker number: "))
worker_shift_number = int(input("Enter worker shift number: "))
worker_hourly_pay_rate = float(input("Enter worker hourly pay rate: "))
worker = ProductionWorker(worker_name, worker_number, worker_shift_number, worker_hourly_pay_rate)
print(worker.toString())