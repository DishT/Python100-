
bank_account = 0

while True:
	bank_react = input("Please Enter Your action: ").split()
	
	if len(bank_react) == 0: break

	bank_action = bank_react[0]
	bank_number = int(bank_react[1])

	if bank_action == "D": 
		bank_account += bank_number
	
	elif bank_action == "W" : 
		bank_account -= bank_number

print("Your Bank Account: ", bank_account)