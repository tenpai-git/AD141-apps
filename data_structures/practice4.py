#!/usr/bin/python3

#Input inventory.txt
#Whitespace delimited.
"""
Joe Desktop 500
Joe Laptop 200
Joe Desktop 400
Mary Desktop 200
Mary Laptop 800
Beth Laptop 500
Beth Tablet 250
Joe Tablet 250
"""

#Desired output stdout dictionary of dictionaries.
#Note that multiple types of same equipment value are added together. 
"""
{
'Mary': {'Desktop': 200, 'Laptop': 800},
'Beth': {'Tablet': 250, 'Laptop': 500},
'Joe': {'Desktop': 900, 'Tablet': 250, 'Laptop': 200}
}
"""

#Initialize variables. 
customer_list = []
inventory_dict = {}

#Open text file
with open("inventory.txt", "r") as thefile:

    # Read each line into memory. 
    for line in thefile:
        c = line.rstrip().split(" ")
        customer = c[0]
        equip    = c[1]
        value    = c[2]

        #If the key (customer) does not exist, add in the dictionary of the equipment and cost.
        if customer not in inventory_dict.keys(): 
            inventory_dict.update({customer: {equip: value}})

        #Else the customer already exists, add in the additional key value pair.
        #If the key of the key-value pair exists, further calculate and add the extra value to that value. 
        else: 
                if equip not in inventory_dict[customer].keys():
                    inventory_dict[customer].update({equip: value})
                else:
                    old_value = inventory_dict[customer][equip]
                    new_value = int(old_value) + int(value)
                    inventory_dict[customer].update({equip: new_value})

print(inventory_dict)





        

