num = int(input("Enter a Number: "))
n1 = int('%d' %num)
n2 = int('%d%d'%(num,num))
n3 = int('%d%d%d'%(num,num,num))
n4 = int('%d%d%d%d'%(num,num,num,num))
n = n1 + n2 + n3 +n4
print(n)