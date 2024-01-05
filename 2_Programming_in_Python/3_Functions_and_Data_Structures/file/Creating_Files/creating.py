try:
    with open ("2_Programming_in_Python\3_Functions_and_Data_Structures\file\Creating_Files\test.txt", mode = "w") as file:
        file.writelines(["Salam Mohsen che khabara", "\nEmroz roze khobie na?"])
except FileNotFoundError as e:
    print("ERROR", e)

