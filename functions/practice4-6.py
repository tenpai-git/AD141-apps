#!/usr/bin/python3

def positive(p_list):
    for item in p_list.copy():
        if item < 0:
            p_list.remove(item)
            print(item)
            print(p_list)
    return p_list

parameterList = [-1, -2, 3, -10, 4, 5, -3404, 403]
print(f"Parameter list {parameterList}")
print("Returning only positive elements.")
newList = positive(parameterList)
print("New List: " + str(newList))






