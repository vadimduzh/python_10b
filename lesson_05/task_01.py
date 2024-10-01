import random
count = 0
for i in range(1, 10):
    random_number = random.randint(1, 20)
    if random_number % 2 == 1:
        print(random_number)
        count += 1

print(count)

