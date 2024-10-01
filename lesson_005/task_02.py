import random

list_of_nums = []
for i in range(21):
    random_number = random.randint(-50, 50)
    list_of_nums.append(random_number)

new_list = list_of_nums.sort()
print(list_of_nums)
