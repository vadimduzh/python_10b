import random

list_1 = []
for i in range(31):
    skip_lesson = random.randint(0, 5)
    list_1.append(22 - skip_lesson)

count = 0
for i in list_1:
    if i == 22:
        count += 1

print(count)
