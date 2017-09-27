# from structshape import structshape
value = input("Input your number")

store_list = value.split(",")
store_tuple = tuple(value.split(","))

print (store_list, structshape(store_list))
print (store_tuple, structshape(store_tuple))
