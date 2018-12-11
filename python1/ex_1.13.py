import random as r


size = 8
row = {}

for i in range(size):
    row[i] = []
    for _ in range(size):
        row[i].append(r.randint(0,10))
    print(str(row[i]))


column = {}
for i in range(size):
    column[i] = []
    for _ in range(size):
        column[i].append(r.randint(0,10))
    print(str(column[i]))


print("Result")
result = {}
for i in range(size):
    result[i] = []
    for j in range(size):
        result[i].append(column[i][j] + row[i][j])
    print(str(result[i]))