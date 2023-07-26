#!/usr/bin/python3

def string_counter(strTC):
    return len(strTC)

def get_second_element(listIterator):
    return listIterator[1] #strToCount[i][1] which is the length of the string

strToCount = str()
countList = list()

while True:
    strToCount = input("Enter a string to count (or \"end\" to exit): ")   
    if strToCount == "end":
        break
    else:
        new_list = [strToCount, string_counter(strToCount)]
        countList.append(new_list)

# print(countList)

sortedCountList = sorted(countList, key=get_second_element)
sortedCountList.reverse()

print(sortedCountList)
print()
highestRightIndent = int(sortedCountList[0][1])

#Justify
for aList in sortedCountList:
    print(f"{aList[0]:>{highestRightIndent}}")
    
