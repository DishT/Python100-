
a = [ i+1 for i in range (10)]
b = [i for i in a if i%2==0]
c = map(lambda x : x**2 , a )
print (a)
print (b)
print (c)
print (dir(c))
for i in c :
	print (i)