#starter code
#parent class
"""
class Dog:

	#Class attribute
	species = 'mammal'

	#initializer/ Instance attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

	#instance method
	def description(self):
		return "{} is {} years old.".format(self.name, self.age)

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
"""



#Exercises 1
#Dog Inheritance
#creates a pets class that holds instances of dogs; this class is completely sepearte from doog class
#assign three dog instances to an instance of the pets class.

#output
#I have 3 dogs, Top is 6, Fletcher is 7, Larry is 9, And they're all mammals, of course.

class Pets:
	dogs = []
	def __init__(self, dogs):
		self.dogs = dogs

	def walk(self):
		for dog in self.dogs:
			print(dog.walk())

class Dog:

	#Class attribute
	species = 'mammal'
	is_hungry = True

	#initializer/ Instance attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

	#instance method
	def description(self):
		return "{} is {} years old.".format(self.name, self.age)

	#instance method
	def speak(self, sound):
		return "{} says {}".format(self.name, sound)

	def eat(self):
		self.is_hungry=False

	def walk(self):
		return "{} is walking!".format(self.name)

#Child class (inherits from Dog Class)
class RusselTerrier(Dog):
	def run(self, speed):
		return "{} runs {}".format(self.name, speed)

#Child class (inherits from Dog class)
class Bulldog(Dog):
	def run(self, speed):
		return "{} runs {}".format(self.name, speed)

pets = [
	Bulldog("Top", 6),
	RusselTerrier("Fletcher", 7),
	Dog("Larry", 9)
]


MyPets = Pets(pets)

print("I have {} dogs".format(len(MyPets.dogs)))
for dog in MyPets.dogs:
	print("{} is {} years old".format(dog.name, dog.age))

print("and they are all {}, of course.".format(Dog.species+'s'))


##Exercies : hungry dogs

#using the same file, ad an instance attribute of is_hungry= True to the Dog class

def check_hungriness(dogs):
	count_dogs = 0
	for dog in dogs:
		if dog.is_hungry:
			count += 1

	if count_dogs == len(dogs):
		return "My dogs are hungry."
	return "My dogs are not hungry."

for dog in MyPets.dogs:
	dog.eat()

print(check_hungriness(MyPets.dogs))

#Exercises : dog walking
# walk() method to both the Pets and Dog classes so that when you call the method on the Pets class, each dog
#instance assigned to the Pets class will walk(). Save this as dog_walking.py
#implement the method in the same manner as the speak() method. For Pets class, you will need to iterate through
#the listo f dogs, then call the method itself.

#Tom is walking! Fletcher is walking! Larry is walking!
MyPets.walk()

