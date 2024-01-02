thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

num = [100, 50, 65, 82, 23]
num.sort()
print(num)

#Sort Descending
num.sort(reverse = True)
thislist.sort(reverse = True)
print(num)
print(thislist)

#Customize Sort Function
def myfunc(n):
    return abs(n - 5)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)