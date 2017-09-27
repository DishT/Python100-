class rectangle:
	# 接數值 並且初始化
	w = 0
	l = 0
	def __init__(self, w , l):
		self.w = w
		self.l = l
	def area(self):
		print (self.w*self.l)

class Shape:
	def __init__(self):
		pass
	def area(self):
		return 0

class Square(Shape):
	l = 0
	def __init__(self,l=0):
		self.l = l

	def area(self):
		print (self.l**2)

def throws():
	return 5/0

aRectangle = rectangle(2,3)
aRectangle.area()

aSquare = Square(3)
aSquare.area()
#raise RuntimeError('something wrong')

try : 
	throws()
except ZeroDivisionError:
	print ("division by zero!")
except Exception:
	print ('Caught an exception')
finally:
	print ('In finally block for cleanup')