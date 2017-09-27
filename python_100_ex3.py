def square_function(num):
	for i in range(num):
		store[i+1] = (i+1)**2
	return store

store = dict()

num = int(input(" "))
print (square_function(num))