def factorial(num):
	number = 1
	for i in range(int(num)):
		number = (i+1)*number
	print (number)
# 8! = 8 * 7!....... , 0! = 1
def factorial_2(num):
	if num == 0 :
		return 1
	else:
		return num * factorial_2(num-1)
def factorial_3(num):
	

num = input()
factorial(num)

print (factorial_2(num))