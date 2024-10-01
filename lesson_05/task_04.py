import random

count_2 = 0
for i in range(21):
    random_number = random.randint(0, 10)
    if random_number in [0, 1, 2]:
        count_2 += 1

print(count_2)
