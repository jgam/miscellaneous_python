#parent class
class Dog:

	#Class attribute
	species = 'mammal'

	#initializer / Instance attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

	#instance method
	def description(self):
		return "{} is {} years old".format(self.name, self.age)

	#instance method
	def speak(self, sound):
		return "{} says {}".format(self.name, sound)

#Child class (inherits from Dog Class)
class RusselTerrier(Dog):
	def run(self, speed):
		return "{} runs {}".format(self.name, speed)

#Child class (inherits from Dog class)
class Bulldog(Dog):
	def run(self, speed):
		return "{} runs {}".format(self.name, speed)

#Child classes inherit attributes and
#behaviors from the parent class
jim = Bulldog("Jim",12)
print(jim.description())

#Child classes have specific attributes
#and behaviors as well
print(jim.run("slowly"))


#Now parent VS child classes
#The isInstance() function is used to determine if an instance is also an instance
#of a certain parent class

# is Jim an instance of Dog()?
print(isinstance(jim, Dog))#true

#Is Julie an instance of Dog()?
julie = Dog("Julie", 100)
print(isinstance(julie, Dog))#true

#Is johnny walker an instance of Bulldog()
johnnywalker = RusselTerrier("johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))#RusselTailer is not a Bulldog class rather, it is RusselTerrier class or Dog class.

#Is julie an instance of jim?
print(isinstance(julie, jim))#no because jim is an instance of a class and julie is an instance of parent class.


#Overriding the functionality of a parent class





