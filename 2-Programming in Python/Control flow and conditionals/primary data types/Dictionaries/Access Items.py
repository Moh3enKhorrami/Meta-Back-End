thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#get()
x = thisdict.get("model")
print(x)

#keys()
x = thisdict.keys()
print(x)


#update
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#Get Values
#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change


#Check if Key Exists
#To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")