from datetime import date
from types import new_class
 
def age(birthdate):
    today = date.today()
    age = today.year - birthdate - ((today.month, today.day) < (1, 1))
    return age

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#printing all keys only
# print("Main Keys: ", myfamily.keys())

# Getting One Child
# print("Getting One Child: ", myfamily["child1"])

# printing all items
# print(myfamily.items())


# looping through all
i=1
for family in myfamily.items():
    total_age = age(family[1]['year'])
    print(f"Name of Child # {i} is: {family[1]['name']} Whose Birth Year is: {family[1]['year']} And Total Age is: {total_age}")
    # print(f"Name of Child # {i} is: {family[1]['name']}")
    # print(f"Year of Child # {i}: {family[1]['year']}")
    # print(f"Age of Child # {i}: {total_age}")
    i = i + 1

print("Total # of Childs in The Family is: ", len(myfamily))

# new child added
new_child = {
  "child4" : {
    "name" : "Indiana",
    "year" : 2021
  }
}

# Updating list with adding new object
myfamily.update(new_child)
print(myfamily)

