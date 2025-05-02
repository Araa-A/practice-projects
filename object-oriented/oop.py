# object = A "bundle" of related attributes (variables) and methods (functions)
# 		 Ex. phone, cup, book
# 		 You need a "class" to create many objects

# class = (blueprint) used to design the sstructure and layout of an object

from car import Car

car1 = Car("Batmobile", 2024, "black", False)
car2 = Car("Corvette", 2025, "blue", True)
car2 = Car("Charger", 2065, "yellow", True)

print(car1) # we're given the memory address

print(car2.model)
print(car2.year)
print(car2.colour)
print(car2.forSale)

car1.describe()

# class variables = Shared among all instances of a class
#		          !!Defined outside your constructor
#				Allow you to share data among all objects created from that class

class Student:

	classYear = 2025
	totalStudents = 0

	def __init__(self, name, age):
		self.name = name
		self.age = age
		#Modifying class variable
		Student.totalStudents += 1

student1 = Student("Tash", 18) #instances
student2 = Student("Aleeya", 18)
student3 = Student("Pinny", 18)
student4 = Student("Zhengyi", 18)


print(student1.name)
print(student1.age)
print(Student.classYear)

print((f"My graduating class of {Student.classYear} has {Student.totalStudents} students"))


