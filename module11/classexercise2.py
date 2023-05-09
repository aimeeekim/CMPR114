import tkinter

class MyGUI:

    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label.pack()
        self.last_name = tkinter.Label(self.main_window, text='Kim')
        self.last_name.pack()
        self.first_name = tkinter.Label(self.main_window, text='Aimee')
        self.first_name.pack()
        self.age = tkinter.Label(self.main_window, text='21')
        self.age.pack()
        tkinter.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()