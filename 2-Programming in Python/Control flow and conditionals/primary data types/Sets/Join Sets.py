set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

#Note: Both union() and update() will exclude any duplicate items.
#The union() method returns a new set with all items from both sets:
set3 = set1.union(set2)
print(set3)

#update()
set1.update(set2)
print(set1)

#Keep ONLY the Duplicates
#The intersection_update() method will keep only the items that are present in both sets.
#Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
z = x.intersection(y)
print(z)

#Keep All, But NOT the Duplicates
#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x.symmetric_difference_update(y)
print(x)

#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#True and 1 is considered the same value:
a = {"apple", "banana", "cherry", True}
b = {"google", 1, "apple", 2}
c = a.symmetric_difference(b)
print(c)


