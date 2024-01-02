thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Use the range() and len() functions to create a suitable iterable.
for i in range(len(thistuple)):
  print(thistuple[i])

#while
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
