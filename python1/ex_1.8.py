from random import seed, random

def RandomNumbers(number):
    seed()
    numbers = []
    for i in range(number):
        numbers.append(random())
    return numbers

N=50
data_list = RandomNumbers(N)
new_list = []

for i in data_list[1:]:
    j = data_list.index(i)
    while j > 0 and data_list[j-1] > data_list[j]:
        data_list[j], data_list[j-1] = data_list[j-1], data_list[j]
        j = j - 1

data_list.reverse()
print (data_list)
