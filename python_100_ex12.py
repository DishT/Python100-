values = []
for i in range(1000,3001):
	str_tmp = str(i)
	if int(str_tmp[0])%2 + int(str_tmp[1])%2 + int(str_tmp[2])%2 + int(str_tmp[3])%2 ==0 :
		values.append(str_tmp)
print (",".join(values))