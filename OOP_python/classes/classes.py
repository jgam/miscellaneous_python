#Python Objects and Classes

#Exerise "The oldest Dog"

class Dog:
	#class Attribute
	species = 'mammal'
	#Initializer / Instance Attributes
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def description(self):
		return "{} is {} years old and it is {}".format(self.name, self.age, self.species)

	def speak(self, sound):
		return "{} says {}".format(self.name, sound)


choco = Dog("Choco", 5)
cookie = Dog("Cookie", 6)
berry = Dog("Berry", 7)
print(choco.name)
print(choco.age)
#write a function called, get_biggest_number() that takes any number of ages(*args) and returns. the oldest one.
#Then output the age of the oldest dog like so.

def get_biggest_number(*args):
	try:
		return max(args)
	except:
		return 'wrong arguments!'

#so far is the instantiating objects
#creating unique instance of a class

print(get_biggest_number(choco.age, cookie.age, berry.name))



#instance methods
#defined inside a class and are used to get the contents of an instance.
#they can aslo be used to perform operations with the attributes of our objects.
#Like the __init__method, the first argument is always self

print(choco.description())
print(choco.speak("gruff gruff"))
#bloo downtown
#박재범 v
#행주 drive thru
#주영 - prada
#죠지 - let's go picnic
#식케이 fly
#네이브 overDrive
#이바다 - 야몽음인
#milic - 보물섬
#woodz - different
#썸데프 - 미끌미끌
#2xxx! - ~lonely birds~
#루피 - vegas




#modifying attributes
# you can do so by modifying different attributes.
class Email:
	def __init__(self):
		self.is_sent = False
	def send_email(self):
		self.is_sent = True

my_email = Email()
print(my_email.is_sent)

my_email.send_email()
print(my_email.is_sent)


#****NOW PYTHON INHERITANCE*****
class Dog:
	def __init__(self, breed):
		self.breed = breed

spencer = Dog("German Shepard")
print(spencer.breed)

sara = Dog("Boston Terrier")
print(sara.breed)

