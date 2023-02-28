import random
n= 20

a = [random.randint(1, 10) for _ in range(n)]
print(a)
b = []

idx = random.randrange(len(a))

a.insert(idx, 0)

for i in range(len(a)):
    if a[i] != 0:
        b.append(a[i]) 
    else:
        break
print(b)
print(max(b))