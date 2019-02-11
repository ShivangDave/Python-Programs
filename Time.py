from time import time

start_time = time()

for i in range(1000):
    i = i + 1
    print(i)

end_time = time()
elapsed = end_time - start_time
print(elapsed)
