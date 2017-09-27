from datetime import datetime

def fact_1(num):
    if num > 0:
        return num*fact_1(num-1)
    else:
        return 1

def fact_2(num):
    if num in know:
        return know[num]
    
    fac = num*fact_2(num-1)
    know[num] = fac
    return fac
fact = 0
fac = 0
know = {0:1, 1:1}
num = int(input("Please input a number! "))

t0 = datetime.now()
fact = fact_1(num)
print("Method 1, original: ",fact)
dt1 = datetime.now() - t0

t0 = datetime.now()
print("Method 2, dic: ",fact_2(num))
dt2 = datetime.now() - t0

print ("dt1/dt2: ", dt1.total_seconds()/dt2.total_seconds())