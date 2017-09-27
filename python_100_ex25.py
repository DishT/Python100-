class American:
	@staticmethod

	def printNationality():
		print("America")


class NewYorker(American):
	def OK(self):
		print("GOGO")

class Circle:

	radius = 0
	def __init__(self,r):
		self.radius = r
	def area(self):
		return self.radius**2*3.14

anAmerican = American()
print("Object A")
anAmerican.printNationality()

American.printNationality()
aNewYorker = NewYorker()
aNewYorker.OK()
aNewYorker.printNationality()

aCircle = Circle(2)
print(aCircle.area())