
cor = input("x,y").split(",")
x = cor[0]
y = cor[1]

array = [] 

for i in range(int(x)):
	#print ("Row", (i+1))
	array.append([])
	for j in range(int(y)):
		array[i].append(i*j)

multlist = [[0 for j in range(int(y))] for i in range(int(x))]

print (multlist)

print (array)
