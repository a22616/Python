'''
30 what is inheritance ?
ans : Inheritance is a way of exeating a new class from an 
    existing class.

31 TYPE OF INHERITANCE
ans : Single inheritance
      single inheritance occure when child class inherits only
      a "single" parent class

      Multiple inhertance
      Multiple inheritance occure when child class inherits only
      a "more" parent class

      Multilevel inheritance
      Multilevel inheritance occure when "more" child class inherits only
      a single parent class
'''

# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the __init__ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()
