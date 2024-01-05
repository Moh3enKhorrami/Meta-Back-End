list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#by appending 
for x in list3:
    list1.append(x)
print(list3)

#by extend()
list1.extend(list2)
print(list1)