favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]

for item in favorites:
    print("I Like this desert ", item)

# Print whit value
for dex, item in enumerate(favorites):
    print(dex, item)


for x in favorites:
  print(x)
  if x == "churros":
    break