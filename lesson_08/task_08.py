import random

lst = []

for i in range(11):
    r = random.randint(1, 10)
    lst.append(r)

count = 1
for i in lst:
    count *= i

print(count)
