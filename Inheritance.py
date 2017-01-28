class Parent():
    def __init__(self, lastName, eyeColor):
        print("Parent Constructor called")
        self.last_name = lastName
        self.eye_color = eyeColor

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys)
        print("Child Constructor called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys
        
##billy_cyrus = Parent("Cyrus", "blue")
miley_cyrus = Child("Cyrus", "blue", 5)
