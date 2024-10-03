import random

lst = []
for i in range(32):
    random_num = random.randint(7, 15)
    lst.append(random_num)

print(lst)

count = 0
for i in range(len(lst)):
    if lst[i] == max(lst):
        count += 1
        print(i + 1)
