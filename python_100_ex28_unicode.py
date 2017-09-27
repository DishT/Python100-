unicodeString = u"Hello World"
print (unicodeString)
print (type(unicodeString))

#s = input()
#u = unicode(s, "utf-8")
#print (u)


value = int(input("Number: "))
sum_up = 0
for i in range (value):
	sum_up += float((i+1)/(i+2))
print (sum_up)


def f (n):
	if n == 0:
		return 1
	else:
		return f(n-1)+100
print (f(value)) 