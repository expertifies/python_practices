'''
*****************************************************
Author: Urwa Usman
Date: Today
*****************************************************
'''

import os
import flask

# print("HELLO WORLD. My Name is Urwa Usman")
# print(os.listdir())
# print(os.getgroups())

# getNumber = input("Please Enter Marks: \n")
# list = []
# list.append(getNumber)
# getNumber = input("Please Enter Marks: \n")
# list.append(getNumber)
# getNumber = input("Please Enter Marks: \n")
# list.append(getNumber)
# getNumber = input("Please Enter Marks: \n")
# list.append(getNumber)
# print(list)
# list.sort()
# print(list)
# l2 = [30,40,10,4,3,4]
# l2.sort()
# print(l2)

# tuple = (1,3,4,4,2,3,3,3)
# print(tuple[1])
# tuple[1] = 2
# print(tuple.count(3))
# print(sum(tuple))
foo = {
    "logged_in": "yes",
    "town":"Dublin",
    "state":"Ohio",
    "country":"USA",
    "products":
    [
        {
            "pic_id":"1500",
            "description":"Picture of a computer",
            "localion":"img.cloudimages.us/2012/06/02/computer.jpg",
            "type":"jpg",
            "childrenimages":
            [
                {
                    "pic_id":"15011",
                    "description":"Picture of a cpu",
                    "localion":"img.cloudimages.us/2012/06/02/mycpu.png",
                    "type":"png"
                },
                {
                    "pic_id":"15012",
                    "description":"Picture of a cpu two",
                    "localion":"img.cloudimages.us/2012/06/02/thiscpu.png",
                    "type":"png"
                }
            ]
        },
        {
            "pic_id":"1501",
            "description":"Picture of a cpu",
            "localion":"img.cloudimages.us/2012/06/02/cpu.png",
            "type":"png"
        }
    ],
}

# i = 1
# j = 1
# for fo in foo["products"]:
#     print(f"\nItem of index {i} is: {fo} \n")
#     childImage = fo.get("childrenimages")
#     if(childImage is not None):
#         for fs in childImage:
#             description = fs.get("description")
#             print(f"\nItem of parent index {i} and child index {j} is: {description} \n")
#             j = j+1
#     else:
#         print(f"\nChildImages Not Found For Item of parent index {i} and child index {j} \n")

#     i = i+1



    
# print(foo['logged_in']+ " - "+ foo['town']+ " - "+ foo['state']+ " - "+ foo['country'])
# print(foo['products'][0]['childrenimages'][0]["pic_id"])

# print(foo["products"][1].items())

# newvalue = {
#     "newval":"123"
# }

# foo["products"][0].update(newvalue)
# print(foo.get("state1"))
# print(foo["state1"])

# a = 12
# if(a>2):
#     print("a is greater than 2")
#     print("1 a is greater than 2")
# elif(a<12):
#     print("a is less than 12")

def tableFunc(ranges):
    i = 1
    takeInput = int(input("please Enter a value: "))
    for i in range(ranges):
        value = f"{takeInput} X {i+1} = {takeInput * (i+1)} "
        print(value)

tableFunc(10)
















