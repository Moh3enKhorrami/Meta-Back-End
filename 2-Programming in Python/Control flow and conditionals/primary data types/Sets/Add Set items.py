thisset = {"apple", "banana", "cherry"}

#Add Items
thisset.add("orange")

print(thisset)

#2-Add Sets
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add Any Iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)