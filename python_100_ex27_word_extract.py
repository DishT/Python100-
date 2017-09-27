import re
text = input("Enter the mail: ")

# method 1 :String

num = text.find("@")
num_1 = text.find(".")
text_name = text[:num]
print ("Method 1: ",text_name)

# method 2 :list slice

text_name = text.split("@")[0]
print ("Method 2: ",text_name)

# Method 3 : Re
text_name = re.findall('(.+)@',text)[0]
print ("Method 3: ",text_name)


company = text[num+1:num_1]
print ("Method 1: ",company)

company = text.replace(".","@").split("@")[1]
print ("Method 2: ",company)

company = re.findall('@(.+)\.',text)[0]
print ("Method 3: ",company)

text = input("Enter the Sentence: ")

# Method 1 :Reg

values = re.findall("[0-9]",text)
print ("Method 1: ", values)

# Method 2 : String
values = []

for word in text:
    if word.isdigit():
        values.append(word)
values_1 = [word for word in text if word.isdigit()]
print ("Method 2: ", values, values_1)        

# Method 3 : List
text = text.split()
values_2 = [word for word in text if word.isdigit()]
print ("Method 3: ", values_2)  

