#Python Objects and Classes

#Exerise "The oldest Dog"

class Dog:
	def __init__(self, name, age):
		self.name = name
		self.age = age


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


print(get_biggest_number(choco.age, cookie.age, berry.name))
#bloo downtown
#박재범 v
#