class pen():
    def __init__(self):
        self.__pens = "lead"  # This double underscore denotes that it is a private class variable and can only be accessed within the class.

    def display(self):
        print(self.__pens)  # It retrieves the value of the private variable __pens and prints it.

s1 = pen()  # Creating an instance of the class
s1.display()  # Calling the display function, which prints "lead"
