'''#1
def Num(N):
    for n in range(1,N):
        n1 = n*(3*n-1)/2
        print(n1,end=' ')
        if n%10==0:
            print('\n')
Num(100)
'''
'''#1
#_*_coding:UTF-8-
def getPentagonalNumber(n):
    return n*(3*n - 1)/2
    last = 0
    for i in range(1,101):
        new = i/10;
        if(last!=new):
            print getPentagonalNumber(i)
        else:
            print getPentagonalNumber(i)
        last = new
'''
'''#2
def sumDigits(n):
    s = 0
    while (n%10!=0):
        g=n%10
        s += g
        n=n//10
    print(s)
m=eval(raw_input('shu ru yi ge shu:'))
sumDigits(m)
'''
'''#3
print("Enter three numbers:")
x = eval(raw_input(">>"))
y = eval(raw_input(">>"))
z = eval(raw_input(">>"))
if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print("The sorted numbers are:{} {} {}".format(x, y, z))
'''
'''#5
for i in range(49,91):
    print(chr(i),end=' ')
    if i%10==0:
        print('\n')
'''
'''#6
def Year(year):
    if (year%4==0) and (year%100!=0):
        print('366 days in {}'.format(i))
    else:
        print('365 days in {}'.format(i))
for i in range(2010,2021):
    Year(i)
'''
'''#7
x1,y1 = (eval(raw_input('shu ru x1 and y1 for point1:')))
x2,y2 = (eval(raw_input('shu ru x2 and y2 for point2:')))
def distance(x1,y1,x2,y2):
    sum = ((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)**0.5
    print(sum)
distance(x1,y1,x2,y2)
'''
'''#9
import time
t = time.time()
print(time.ctime(t))
'''
'''#10
import random
n1 = random.randint(1,6)
n2 = random.randint(1,6)
n = n1 + n2
#print(n1, n2 ,n1+n2)
if n==7 or  n==11:
    print("You rolled {} + {} = {}".format(n1,n2,n))
    print("You win")
if n==2 or n ==3 or n ==12:
    print("You rolled {} + {} = {}".format(n1,n2,n))
    print("You lose")
if n ==4 or n==5 or n ==6 or n==8 or n==9 or n==10:
    print("You rolled {} + {} = {}".format(n1,n2,n))
    print("point is {}".format(n))
    if n==n:
        print("You rolled {} + {} = {}".format(n1,n2,n))
        print("You win")
    else:
        print("You rolled {} + {} = {}".format(n1,n2,n))
        print("You lose")
'''

