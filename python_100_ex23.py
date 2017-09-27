def caculate(num):
    ''' Return the square value of the input number.

        The input number must be integer.

    '''
    return num**2
print (caculate(3))

print (abs.__doc__)
print (int.__doc__)
print (input.__doc__)
print (caculate.__doc__)

class Person:

    name = "Person"

    def __init__(self, name = None):
        self.name = name
jack = Person("Jack")
print ("%s name is %s" %(Person.name, jack.name))

nico = Person()
nico.name = "ABC"
print ("%s name is %s" %(Person.name, nico.name))