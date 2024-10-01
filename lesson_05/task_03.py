import random

count_1 = 0
for i in range(21):
    random_number = random.randint(14, 16)
    if random_number == 16:
        count_1 += 1

print(count_1)

