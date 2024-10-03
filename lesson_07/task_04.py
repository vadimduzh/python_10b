import random

lst = []
for i in range(31):
    random_num = random.randint(20, 30)
    lst.append(random_num)

max_num = max(lst)
min_num = min(lst)
print(max_num, min_num)

