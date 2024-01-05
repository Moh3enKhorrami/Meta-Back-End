def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
    print(ans)

except divide_by as e:
    print(e, "we cannot divide by zero")

except Exception as e:
    print(e, "something went wrong")