import math

a = int (input("Enter first factor : "))
b = int (input("Enter second factor: "))
c = int( input("Enter third factor: "))

d = b*b - (4*a*c)

if(d<0):
    print ("no solution")

elif(d==0):
    x1 = -1*b/(2*a)
    print ("Solution: " + str(x1))

else:
    x1 = (-1*b - math.sqrt(d))/(2*a)
    x2 = (-1*b + math.sqrt(d))/(2*a)
    print ("Solution: " + str(x1) + ", " + str(x2))