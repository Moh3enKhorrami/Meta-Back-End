import time
start_time = time.time()

for i in range (10):
    for j in range(10):
        print(0, end = " ")
    print()
    
print(round((time.time() - strat_time ), 2))