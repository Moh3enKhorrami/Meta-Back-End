import random
a = 0
z = 99
hads = random.randint(a, z)
print(hads)
javab = input()


while javab != "d" :
    if javab == "b":
        z = hads
        hads = random.randint(a, z)
        print(hads)
        javab = input()
    elif javab == "k":
        a = hads
        hads = random.randint(a, z)
        print(hads)
        javab = input()
    
print("Dorost gofti: ", hads)
    
