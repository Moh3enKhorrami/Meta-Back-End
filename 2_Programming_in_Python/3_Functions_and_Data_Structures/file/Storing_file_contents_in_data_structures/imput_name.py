import random

f_name = input("Type the file name: ")
f = open("f_name.txt", "r")
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))