#With the else statement we can run a block of code once when the condition no longer is true:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)