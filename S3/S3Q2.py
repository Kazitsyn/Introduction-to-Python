a = [0, -1, 5, 2, 3, 4, 2, 5]
c = 0
for i in range(1, len(a)):
    if a[i-1] < a[i]:
        c += 1
print(c)