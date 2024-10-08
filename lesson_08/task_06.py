import random

lst = []

for i in range(21):
    r = random.randint(1, 50)
    lst.append(r)

count = int(input("Enter the count: "))
x = 0
cost = 0
while x != count:
    i = int(input("Enter the num: "))
    for j in range(len(lst)):
        if j == i:
            cost += lst[j - 1]
    x += 1

print(lst, cost)



