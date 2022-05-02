a = [[0, 1], [2, 3]]
print(a)
b = []
for i in range(2):
    b.append(a[i])
b[0][0] = 1
print(b)
print(a)