import random

list_1 = []
for i in range(26):
    random_number = random.randint(2, 10)
    list_1.append(random_number)
print(list_1)

for x in range(len(list_1)):
    if list_1[x] == 10:
        print(x + 1)


