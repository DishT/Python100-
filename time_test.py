import time 

time = time.ctime()
time = time.split()
time = time[1]+"/"+time[2]+"/"+time[4]
print ("time.ctime() : %s" % time)