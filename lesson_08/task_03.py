lst = []
for i in range(21):
    n = int(input())
    lst.append(n)

count = 0
ind = 0
for i in lst:
    count += i
    ind += 1

res = count / ind
print(res)
