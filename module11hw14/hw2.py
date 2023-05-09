import tkinter

class TestAVG:
	def __init__(self):
		# Create the main window.
		self.main_window = tkinter.Tk()

		# Create the five frames.
		self.test1_frame = tkinter.Frame(self.main_window)
		self.test2_frame = tkinter.Frame(self.main_window)
		self.test3_frame = tkinter.Frame(self.main_window)
		self.test4_frame = tkinter.Frame(self.main_window)
		self.test5_frame = tkinter.Frame(self.main_window)
		self.avg_frame = tkinter.Frame(self.main_window)
		self.button_frame = tkinter.Frame(self.main_window)

		# Create and pack the widgets for test 1
		self.test1_label = tkinter.Label(self.test1_frame, text = "Enter Test 1 score: ")
		self.test1_entry = tkinter.Entry(self.test1_frame, width=10)

		self.test1_label.pack(side="left")
		self.test1_entry.pack(side="left")

		# Create and pack the widgets for test 2
		self.test2_label = tkinter.Label(self.test2_frame, text = "Enter Test 2 score: ")
		self.test2_entry = tkinter.Entry(self.test2_frame, width=10)

		self.test2_label.pack(side="left")
		self.test2_entry.pack(side="left")
		
		# Create and pack the widgets for test 3
		self.test3_label = tkinter.Label(self.test3_frame, text = "Enter Test 3 score: ")
		self.test3_entry = tkinter.Entry(self.test3_frame, width=10)

		self.test3_label.pack(side="left")
		self.test3_entry.pack(side="left")

		# Create and pack the widgets for test 4
		self.test4_label = tkinter.Label(self.test4_frame, text = "Enter Test 4 score: ")
		self.test4_entry = tkinter.Entry(self.test4_frame, width=10)

		self.test4_label.pack(side="left")
		self.test4_entry.pack(side="left")

		# Create and pack the widgets for test 5
		self.test5_label = tkinter.Label(self.test5_frame, text = "Enter Test 5 score: ")
		self.test5_entry = tkinter.Entry(self.test5_frame, width=10)

		self.test5_label.pack(side="left")
		self.test5_entry.pack(side="left")

		# Create and pack the widges for the average
		self.result_label = tkinter.Label(self.avg_frame, text = "Average: ")
		self.avg = tkinter.StringVar() # To Update avg_label
		self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)

		self.sum_label = tkinter.Label(self.avg_frame, text = "Total: ")
		self.total = tkinter.StringVar() # TO Update total_label
		self.total_label = tkinter.Label(self.avg_frame, textvariable=self.total)

		self.result_label.pack(side="left")
		self.avg_label.pack(side="left")
		self.sum_label.pack(side="left")
		self.total_label.pack(side="left")

		# Create and pack the button widgets
		self.calc_button = tkinter.Button(self.button_frame, text ="Average", command=self.calc_avg)
		self.quit_button = tkinter.Button(self.button_frame, text = "Quit", command = self.main_window.destroy)

		self.calc_button.pack(side="left")
		self.quit_button.pack(side="left")

		# Pack the frames.
		self.test1_frame.pack()
		self.test2_frame.pack()
		self.test3_frame.pack()
		self.test4_frame.pack()
		self.test5_frame.pack()
		self.avg_frame.pack()
		self.button_frame.pack()

		# Start the main loop
		tkinter.mainloop()

	# The calc_avg method is the callback function fro the calc_button widget
	def calc_avg(self):

		# Get the three test scores and store them in variables
		self.test1 = float(self.test1_entry.get())
		self.test2 = float(self.test2_entry.get())
		self.test3 = float(self.test3_entry.get())
		self.test4 = float(self.test4_entry.get())
		self.test5 = float(self.test5_entry.get())

		# Calculate the average
		self.average = (self.test1 + self.test2 + self.test3 + self.test4 + self.test5) / 5.0
		
		#Calculate the total
		self.sum = self.test1 + self.test2 + self.test3 + self.test4 + self.test5

		# Update the avg_label widget by storing the value of self.average in the StringVar
		# object refernec by avg.
		self.avg.set(self.average)
		self.total.set(self.sum)

# Create an instance of the TestAvg class
if __name__ == "__main__":
	test_avg = TestAVG()