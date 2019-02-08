class Circle():
	"""docstring for Circle"""
	pi=3.14
	def __init__(self, radius=1):
		
		self.radius=radius

	def area(self):
		return self.radius*self.radius*self.pi
	def circumference(self):
		return 2 * self.pi * self.radius
mycircle=Circle(10)
print(mycircle.radius)
print(mycircle.area())
print(mycircle.circumference())
