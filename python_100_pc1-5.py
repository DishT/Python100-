l = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 !=0:
        l.append(str(i))
#l = str(l)
#print (l)
print (",".join(l))

# No2. factorial

def fact(num):
    f = []
    factorial = 1
    
    for i in range(0,num):
        factorial = factorial*(i+1)

    return factorial

def generate_square(num):
    dic = {}
    for i in range(num):
        dic[i+1] = (i+1)**2
    return dic

def convert_str_to_tuple(string):
    string_l = string.split(",")
    string_t = tuple(string_l)

    print(string_l)
    print(string_t)

class InputOutputString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("OO is Fun:")
    def printString(self):
        print (self.s.upper())

num = int(input("Please enter a number: "))

print (fact(num))

print(generate_square(num))

convert_str_to_tuple(input("Enter the string: "))

s = InputOutputString()
s.getString()
s.printString()