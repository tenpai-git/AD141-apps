#!/usr/bin/python3

def commonFunctions(list_one, list_two):
    new_list = list()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                new_list.append(element_two)
    return new_list

abc = [1,2,3,4,5,6,7]
xyz = [5,6,7,8,9,10]

print(commonFunctions(abc, xyz))

