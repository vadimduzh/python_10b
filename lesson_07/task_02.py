lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min_num = lst[0]
for i in lst:
    if i < min_num:
        min_num = i

print(min_num)
