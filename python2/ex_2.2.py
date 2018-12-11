import cmath


class Complex():
    real=0
    image=0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        newReal = self.x+other.x
        newImage = self.y+other.y
        return Complex(newReal, newImage)

    def __sub__(self, other):
        newReal = self.x - other.x
        newImage = self.y - other.y
        return Complex(newReal, newImage)

    def __mul__(self, other):
        newReal = self.x * other.x - self.y * other.y
        newImage = self.y * other.x + self.x + other.y
        return Complex(newReal, newImage)

    def __div__(self, other):
        try:
            newReal = (self.x * other.x + self.y * other.y)/(other.x**2+other.y**2)
            newImage = (self.y * other.x - self.x + other.y)/(other.x**2+other.y**2)
            return Complex(newReal, newImage)
        except ZeroDivisionError:
            print("unsolved operation")

    def module(self):
        return ((self.x**2+self.y**2)**(1/2))

    def angle(self):
        if(self.x>0):
            angle=cmath.atan(self.y/self.x)
        elif(self.x<0):
            angle = cmath.atan(self.y / self.x)+cmath.pi
        elif(self.x==0 and self.y>0):
            angle=0.5*cmath.pi
        elif(self.x==0 and self.y<0):
            angle = -0.5 * cmath.pi
        elif(self.x==0 and self.y==0):
            angle=0
        return angle;


a=Complex(3,4)
b=Complex(0,0)
c=a+b
print (c.angle())