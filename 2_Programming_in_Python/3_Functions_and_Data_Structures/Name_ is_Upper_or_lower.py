input_name = input("")
count_upper = sum(1 for char in input_name if char.isupper())
count_lower = sum(1 for char in input_name if char.islower())

if count_upper > count_lower:
    result = input_name.upper()
else:
    result = input_name.lower()

print(result)
