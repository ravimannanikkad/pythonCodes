class Student:
   # Defenition of atributes of the class
   def __init__(self,name,major,gpa):
        self.name = name
        self.major =major
        self.gpa=gpa
   # Defining a function for checking if the strudent have a good GPA or not
   def on_honor_roll(self):
       if self.gpa >= 3.5:
           return True
       else:
           return False
