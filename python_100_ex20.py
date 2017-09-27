def yield_fun():
    a = 3
    b = 2
    yield a
    c = 4
    yield b
     
generator = yield_fun()
print (generator.__next__())
print (generator.__next__())

def yield_fun_1():
    a = 3
    b = 2
     
    b = yield a
    yield b
     
 
generator = yield_fun_1()
print (generator.__next__())
print (generator.send(8))


class generator:
    num = 0
    store = list()
    def __init__(self,num):
        self.num = int(num)
    def gen(self):
        for i in range (self.num+1):
            if i % 7 == 0:
                self.store.append(i)
        print (self.store)

gen = generator(input(" :"))
gen.gen()

def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

gen_1 = putNumbers(100)
for i in range(101):
    print(gen_1.__next__())