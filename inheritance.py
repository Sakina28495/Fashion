class Animal():
	"""docstring for Animal"""
	def __init__(self,fur):
		self.fur=fur
		
	def report(self):
		print("Animal")

	def eat(self):
		print('Eating')
class Dog(Animal):
	def __init__(self,fur):
		Animal.__init__(self,fur)
		print("Dog Created")

#override method
	def report(self):
		print("Hi Dogs")
d=Dog('fuzzy')
d.eat()
d.report()
a=Animal()
a.eat()
a.report()