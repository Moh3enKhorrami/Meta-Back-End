thisset = {"apple", "banana", "cherry"}

#Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print(thisset)

#discard() method: 
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("banana")
print(thisset)

#pop()
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed
#The return value of the pop() method is the removed item.
#Remove a random item by using the pop() method:
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = thisset.pop()
print(x)
print(thisset)

#del()
del thisset
print(thisset)

#clear()
thisset.clear()
print(thisset)