sentence = input("Enter your sentence: ")
count_low = 0
count_high = 0
d = {"Low":0, "Upper":0}

for word in sentence:
	if word.islower():
		count_low += 1
		d["Low"] += 1
	elif word.isupper():
		count_high += 1
		d["Upper"] += 1

print ("UPPER CASE", count_high, "LOWER CASE", count_low)
print ("UPPER CASE", d["Upper"], "LOWER CASE", d["Low"])