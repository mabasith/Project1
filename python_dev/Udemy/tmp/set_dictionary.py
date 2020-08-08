#Create a set

item = {"arrow", "spear", "rock"}
print(item)
print(len(item))
item.add("dog")
print(item)

num1 = {1,2,3,4}
num2 = {1,3}

if num2.issubset(num1):
    print("Is sub set")
if num1.issuperset(num2):
    print("super set")
print (num1.intersection(num2))

#create a mapping of states to their abbrevation

states = {"Oregon" : "OR", "Florida":"FL", "California" : "CA"}
for state,abbrev in states.items():
    print("%s state has %s"%(state,abbrev))