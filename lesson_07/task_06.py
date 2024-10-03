import random

lst = []

for i in range(21):
    random_num = random.randint(0, 100)
    lst.append(random_num)

print(lst)

max_num = max(lst)
min_num = min(lst)
print(min_num, max_num)
