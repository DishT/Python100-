import datetime
def fib_1(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else :
        return fib_1(n-1)+fib_1(n-2)
def fib_2(n):
    if n in known:
        return known[n]
    res = fib_2(n-1)+fib_2(n-2)
    known[n] = res
    return res
known = {0:0, 1:1}

n = int(input("Enter : "))
t0 = datetime.datetime.now()
value = fib_1(n)
t1 = datetime.datetime.now() - t0

t0 = datetime.datetime.now()
value_2 = fib_2(n)
t2 = datetime.datetime.now() - t0
print("t1/t2=", t1/t2)
print (value)

fib_list_1=[fib_1(i) for i in range(n+1)]

fib_list_2=[fib_2(i) for i in range(n+1)]
print(fib_list_1)
print(fib_list_2)

def even (n):
    a = [num for num in range(n+1) if num%2 ==0]
    return a
print (even(n))

def find_57(n):
    b = [num for num in range(n+1) if num%5==0and num%7==0]
    return b

print (find_57(n))