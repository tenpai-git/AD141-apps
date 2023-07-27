#!/usr/bin/python3

def newSum(*args):
    total_sum = int()
    for sum in args:
        total_sum += sum
    return total_sum

prompt = str()
newlist = []
i = int()

#while True:
#    if prompt = "End"
#        break
#    else
#        prompt = input("Enter numbers to add (Type \"end\" to end program.): ") 
#        newlist.append(prompt)

print(newSum(5,3,4,5,6,2))
print(newSum(24,434,4))

