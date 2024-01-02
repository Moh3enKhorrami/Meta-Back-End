#Adding Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Update Dictionary
#The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
#The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict.update({"color": "red"})
print(thisdict)
