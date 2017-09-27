import re
import time
from datetime import datetime

password = input("Enter your password: ").split(",")
print (password)
password_ok = []
value = []
a = 0
b = 0
c = 0
t0 = datetime.now()
for i in password:
	
	#print(len(i) >= 6 ,len(i) <= 12 ,i.isdigit() ,i.isupper() ,i.islower())

	if len(i) >= 6 and len(i) <= 12 :
		for x in i:
			if x.isdigit(): a = 1 
			elif x.isupper(): b = 1
			elif x.islower(): c = 1
			elif "$" in x or "#" in x or "@" in x: d =1 
	if (a + b + c + d) == 4:
		password_ok.append(i)
		(a,b,c,d) = (0,0,0,0)
dt1 = datetime.now() - t0

t0 = datetime.now()

for i in password:
	if len(i) < 6 and len(i) >12 :
		continue
	else:
		pass

	if (re.search("[a-z]",i)) and (re.search("[0-9]",i)) and (re.search("[A-Z]",i)) and (re.search("[$#@]",i)) and not(re.search("\s",i)):
		value.append(i)

dt2 = datetime.now() - t0

print (",".join(value), dt2)
print (",".join(password_ok),dt1)

print ("Regex/ without Regex", dt2/dt1)