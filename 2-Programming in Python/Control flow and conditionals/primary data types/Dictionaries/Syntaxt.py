thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Dictionary Items
print(thisdict["brand"])

#Dictionary Length
print(len(thisdict))

#Dictionary Items - Data Types
#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


#The dict() Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)