from collections import Counter
from datetime import datetime

s = input("Enter your sentence: ")

histogram_1 = {}
histogram_2 = []

words = s.split()

print ("Method 1 : Implement by Dictionary")

t0 = datetime.now()
for word in words:
	histogram_1[word] = histogram_1.get(word,0) + 1

for key, value in histogram_1.items():
	print (key,":" ,value)
dt1 = datetime.now() - t0


print ("Method 2 : Implement by List")
t0 = datetime.now()
for word in words:
	if word not in histogram_2:
		histogram_2.append(word)

for i in range(len(histogram_2)):
	print (histogram_2[i], words.count(histogram_2[i]))
dt2 = datetime.now() - t0

print ("dt1/dt2:",dt1/dt2)
count = Counter(s)

#print (count)
