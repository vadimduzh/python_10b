import random

count = int(input("Enter the total or people: "))

lst = []
for i in range(1, count + 1):
    random_num = random.randint(280, 370)
    lst.append(random_num)

print(lst)

max_num = max(lst)
num = lst.index(max_num)
print(max_num, num)
