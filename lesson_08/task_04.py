import random

count_2 = 0
ind = 0
count_1 = 0
lst = []
for i in range(201):
    r = random.randint(10, 1100)
    if r > 1000:
        count_1 += 1
    lst.append(r)

count = 0
ind = 0
for i in lst:
    count += i
    ind += 1

res = count / ind
print(count)
print(res)
print(count_1)
