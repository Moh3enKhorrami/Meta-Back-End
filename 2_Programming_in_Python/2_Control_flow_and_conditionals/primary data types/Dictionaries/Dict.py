string = "salam. mohsen ist here and testing python for fun"

counter = dict()
print(counter)
for i in string:
    counter[i] = counter.get(i, 0) +1

for x in list(counter.keys()):
    print("%s appeared %s times" % (x,counter[x]) )

print(counter)