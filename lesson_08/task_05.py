import random

max_files = 0
count = 0
for i in range(11):
    r = random.randint()
    count += 1
    if r > max_files:
        max_files = r

print(max_files, count)
