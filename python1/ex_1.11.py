
a = [1,2,12,4]
b = [2,4,2,8]

def product(a,b):
    result = 0
    for i in range(4):
        result = result + (a[i]*b[i])
    return result

print(product(a,b))



