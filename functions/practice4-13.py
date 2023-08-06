#!/usr/bin/python3

def commonFunctions(list_one, list_two, occurence_number):
    count = 0
    new_list = list()
    for element_one in list_one:
        for element_two in list_two:
            if element_one == element_two:
                count += 1
                print(f"Occurence {count} Found!")
                if count == occurence_number:
                    print("Desired Occurence Found!")
                    new_list.append(element_two)
    return new_list

abc = [1,2,5,5,5,6,7]
xyz = [5]
counter = 3

print(commonFunctions(abc, xyz, counter))

