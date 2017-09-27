def upper_function():
	store = []
	while True:

		s = input("Enter your word: ")
		if s :
			store.append(s.upper())
		else:
			break
	for item in store:
		print (item)

upper_function()