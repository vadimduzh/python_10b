import random

list_1 = []
for i in range(31):
    random_num = random.randint(-5, 10)
    list_1.append(random_num)

print(list_1)
for l in list_1:
    if l < 0:
        print(list_1.index(l) + 1)
        break

