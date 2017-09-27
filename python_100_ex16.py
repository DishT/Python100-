numbers = input("Enter the numbers: ").split(",")

odd_list = [ i for i in numbers if int(i)%2 !=0]

print (",".join(odd_list))