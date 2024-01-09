menu = ["Espresso", "Latte", "Cappuccino", "Macchiato", "Americano", "Cortado", "Decaf"]

def find_coffee(coffee):
    if coffee[0] == "C":
        return coffee


# map_coffee = map(find_coffee, menu)
# print(map_coffee)
# for x in map_coffee:
#     print(x)
    
filter_coffe = filter(find_coffee, menu)
print(filter_coffe)
for x in filter_coffe:
    print(x)