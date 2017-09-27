from operator import itemgetter

data = []
file = open('data.txt')
for line in file :
    data.append(tuple(line.strip().split(",")))

# 1. input & convert to tuple


#while True:
#    s = input("Enter your number: ").split(",")
#    print (s)
#    if len(s)==1:
#        break
#    data.append(tuple(s)) 

# 2. Sort 

sort = sorted(data, key = itemgetter(0,1,2))
print (sort)