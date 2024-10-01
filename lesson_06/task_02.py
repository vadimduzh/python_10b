import random

count_3 = 0
list_2 = []
for i in range(32):
    random_num = random.randint(0, 10)
    if random_num == 0:
        count_3 += 1

print(count_3)
