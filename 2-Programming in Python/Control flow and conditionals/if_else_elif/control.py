bill_total = 220
discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    bill_total = bill_total - discount1
    print("Total is greater than 100!")
elif bill_total > 200:
    bill_total = bill_total - discount2
    print("Total is greater than 200!")
else:
    print("Total is less than 100!")

print("total bill: " + str(bill_total))