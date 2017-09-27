sentence = input("Enter your sentence: ")
digit = 0
letter = 0
d = {"DIGITs":0,"LETTERs":0}
for i in range (len(sentence)):
	if sentence[i].isdigit():
		digit += 1
		d["DIGITs"] += 1
	elif sentence[i].isalpha():
		letter += 1
		d["LETTERs"] += 1
print ("DIGITs", digit, "LETTERs", letter)
print ("DIGITs", d["DIGITs"], "LETTERs", d["LETTERs"])