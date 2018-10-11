'''
#1
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        res = self.width * self.height
        print res
    def getP(self):
        zhou = (self.width + self.height) * 2
        print zhou
Rectangle(4,40).getArea()
Rectangle(4,40).getP()
'''
'''
#2
class Account:
    def __init__(self,id1,balance,annuallnterestRate):
        self.__id1 = id1
        self.__balance = balance
        self.__annuallnterestRate = annuallnterestRate
    def getMonthlyIntereRate(self):
        yuelilv = self.__annuallnterestRate / 12
        print ('yue li lv is {}'.format(yuelilv))
    def getMonthlyInterest(self):
        yuelixi = self.__balance * (self.__annuallnterestRate / 12)
        print ('yue li xi is {}'.format(yuelixi))
    def withdraw(self):
        qu = self.__balance - 2500
        yuelilv = self.__annuallnterestRate / 12
        yuelixi = qu * (self.__annuallnterestRate / 12)
        print ('qu zhi hou {} yuelilv {} yuelixi {}'.format(qu,yuelilv,yuelixi))
    def deposit(self):
        cun = (self.__balance-2500) + 3000
        yuelilv = self.__annuallnterestRate / 12
        yuelixi = cun * (self.__annuallnterestRate / 12)
        print ('cun zhi hou {} yuelilv {} yuelixi {}'.format(cun,yuelilv,yuelixi))
A = Account(1122,20000,0.045)
A.getMonthlyIntereRate()
A.getMonthlyInterest()
A.withdraw()
A.deposit()
'''
'''
#3
import math
class RegularPolygon:
    def __init__ (self,n=3,side=1,x=0,y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    def getPerimeter(self):
        zhou = self.__n * self.__side
        print zhou
    def getArea(self):
        area = (self.__n * math.pow(self.__side,2)) / (4 * math.tan(math.pi / self.__n))
        print area


RegularPolygon().getPerimeter()
RegularPolygon().getArea()


RegularPolygon(6,4).getPerimeter()
RegularPolygon(6,4).getArea()

RegularPolygon(10,4,5.6,7.8).getPerimeter()
RegularPolygon(10,4,5.6,7.8).getArea()
'''
'''
#4
class Fan:
    def __init__(self,speed,on=False,radius=5,color='blue'):
        self.__speed = speed   #feng shan su du 
        self.__on = on         #feng shan zhuang tai
        self.__radius = radius #ban jing
        self.__color = color
    def speed(self,SLOW =1,MEDIUM = 2,FAST = 3):
        print self.__speed
    def func(self):
        print self.__on
        print self.__radius
        print self.__color
F1 = Fan(3,True,10,'yellow')
F1.speed()
F1.func()
F2 = Fan(2,False,5,'blue')
F2.speed()
F2.func()
'''
'''
#4
class Fan:
    def __init__(self,speed,radius,color,on):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on
    def show (self):
        print('[+] speed:',self.__speed)
        print('[+] radius:',self.__radius)
        print('[+] color:',self.__color)
        print('[+] on:',self.__on)
F=Fan(speed = 3 ,radius = 5,color = 'yellow',on = False)
F.show()
'''
'''
#5
class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        if self.__a * self.__d - self.__b * self.__c == 0:
            print ('there is no solution to this equation')
            exit (0) # wu bao cuo jie su dang qian dai ma
    def isSolvable(self):
        print (' [+] True')
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f)/(self.__a * self.__d - self.__b * self.__c)
        print (' [+] x:',x)
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        print ('[+] y:',y)
L=LinearEquation(1,2,3,4,5,6)
L.isSolvable()
L.getX()
L.getY()
'''

#6
class LinearEquation:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.__x3 = x3
        self.__y3 = y3
        self.__x4 = x4
        self.__y4 = y4
    def Result(self):
        k1 = (y1 - y2) / (x1 - x2)
        k2 = (x3 - x4) / (y3 - y4)
        if k1 ==k2:
            print('[+] mei you jiao dian')
        else:
            
        if self.__a * self.__d - self.__b * self.__c == 0:
            print ('there is no solution to this equation')
            exit (0) # wu bao cuo jie su dang qian dai ma
    def isSolvable(self):
        print (' [+] True')
    def getX(self):
        x = (self.__e * self.__d - self.__b * self.__f)/(self.__a * self.__d - self.__b * self.__c)
        print (' [+] x:',x)
    def getY(self):
        y = (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
        print ('[+] y:',y)
L=LinearEquation(1,2,3,4,5,6)
L.isSolvable()
L.getX()
L.getY()

