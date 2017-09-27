def divide_5():
	store = [] 
	num = input("Enter the 4 dig number: ").split(",")
	for i in num :
		if int(i)%5 == 0:
			store.append(i)
		
	print(",".join(store))

divide_5()
