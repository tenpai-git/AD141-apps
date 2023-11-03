#!/usr/bin/python3
import sys

#Sort and print all arguments without the path in sys.argv[0]
a = [] 
for i in range(len(sys.argv)):
    if i > 0:
#        print(sys.argv[i])
        a.append(sys.argv[i])
a.sort()
print("All of your arguments sorted:" + str(a))

#Add all the arguments together.
j = int()
for i in range(len(sys.argv)):
    k = sys.argv[i]
    if k.isdecimal():
        n = int(k)
        j+=n
    else:
        continue

print("Adding all decimal arguments together as integers:" + str(j))
