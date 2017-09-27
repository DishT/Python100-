class question5(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Hello, Input your word...")
    def printString(self):
        print(self.s.upper())

strObj = question5()
strObj.getString()
strObj.printString()