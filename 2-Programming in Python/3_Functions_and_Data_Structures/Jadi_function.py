hour = int(input("How many hours did you work per month?"))
per_hour = int(input("How much do you get paid per hour?"))

def salary (hour, per_hour):
    if hour > 320:
        return "You worked more than the allowed hours per month."
    elif per_hour <= 8:
        return "Why do you work for this amount of salary!"
    else:
        total = hour * per_hour
        return total

print(salary(hour, per_hour))