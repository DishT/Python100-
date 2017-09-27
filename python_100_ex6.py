import math
def caculation(D):
	Q = math.sqrt((2*50*D)/30)
	return Q

Ds = input("Input your numbers! ").split(",")
#Ds = Ds.split(",")
Qs = []
for i in Ds:
	Qs.append(str(int(caculation(int(i)))))
print (",".join(Qs))