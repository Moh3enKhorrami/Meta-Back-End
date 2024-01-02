thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

#List Length
print(len(thislist))

#From Python's perspective, lists are defined as objects with the data type 'list':

print(type(thislist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

#Range of Indexes
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

if "apple" in thislist:
    print("Yes")

#Change Item Value
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Insert Items
thislist.insert(2, "watermelon")
print(thislist)

#Append Items
thislist.append("Moh3en")
print(thislist)

#Extend List
tropical = ["mango2", "papaya"]
thislist.extend(tropical)
print(thislist)

#Remove Specifies Item
thislist.remove("banana")
print(thislist)

#index
thislist.pop(1)
print(thislist)

del thislist[0]
print(thislist)

#Clear
thislist.clear()
print(thislist)