fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

#newlist = [expression for item in iterable if condition == True]
#newlist = [x for x in fruits if "a" in x]

print(newlist)