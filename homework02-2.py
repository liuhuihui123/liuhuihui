'''#1
import math
a, b, c = eval(raw_input("Enter a, b, c:"))
n = b*b-4*a*c
if (n>0):
    r1 =( -b + math.sqrt(b*b-4*a*c))/2*a
    r2 =( -b - math.sqrt(b*b-4*a*c))/2*a
    print(r1 , r2)
elif (n==0):
    r1 =( -b + math.sqrt(b*b-4*a*c))/2*a
    r2 =( -b - math.sqrt(b*b-4*a*c))/2*a
    r1 = r2
    print(r1)
if (n<0) :
    print("The equation has no real roots")
'''
'''#2
import random
n1=random.randint(1,100)
n2=random.randint(1,100)
n=n1+n2
num = raw_input(("qing shu ru shang mian de lia ge shu zhi he:"))
if num == n:
    print("True")
else:
    print("False")
    print(n)
    '''
'''#3
today = eval (raw_input("jin tian shi :"))
day = eval(raw_input("guo le ji tian :"))
week = (today+day)%7
if week == 0:
    print("jin tian shi {} and the future day is Sunday".format(today))
elif week == 1:
    print("jin tian shi {} and the future day is Monday".format(today))
elif week == 2:
    print("jin tian shi {} and the future day is Tuesday".format(today))
elif week == 3:
    print("jin tian shi {} and the future day is Wendnesday".format(today))
elif week == 4:
    print("jin tian shi {} and the future day is Thurday".format(today))
elif week == 5:
    print("jin tian shi {} and the future day is Firday".format(today))
'''
'''#4
print("qing shu ru san ge zheng shu :")
x = eval(raw_input(">>"))
y = eval(raw_input(">>"))
z = eval(raw_input(">>"))
if x>y:
    x,y = y,x
if x>z:
    x,z = z,x
if y>z:
    y,z = z,y
print(x,y,z)
'''
'''#5
w1,p1 = eval(raw_input('Enter weight and price for package 1"'))
w2,p2 = eval(raw_input('Enter weight and price for package 2"'))
baozhuang1 = p1 / w1
baozhuang2 = p2 / w2
if baozhuang1 < baozhuang2:
    print('package 1 has the better price')
elif baozhuang1 >baozhuang2:
    print('package 2 has the better price')
else:
    print('package 1 the same as package 2')
'''
'''#6
month ,year = eval(raw_input("shu ru month and years:"))
a = 0
if(a){
        case 1:
        case 3:
        case 5:
        case 7:
        case 8:
        case 10:
        case 12 :print("31\n");break
        case 2:if (year%4==0 and year%100!=0 | year%400==0):
                     a=29
               else:
                     a=28
        case 4:
        case 6:
        case 9:
        case 11:print("30\n");
        }
print(a)
    '''

'''#7
import random
yingbi = eval(raw_input("cha shi zhengmian(1) huanshi fanmian(0):"))
n = random.randint(0,1) 
if (n == 1):
    print('True')
if n==0:
    print('False')
'''
'''#11
num = eval(raw_input("shu ru yi ge san wei shu:"))
bai = num /100
shi = num/10%10
ge = num % 10
if bai == ge:
    print("{} is a pailndrome".format(num))
else:
    print("{} is not a pailndrome".format(num))
'''
#12
a,b,c = eval(raw_input("shu  ru san jiao xing de san ge bian:"))
zc = a+b+c
if (a+b>c):
    print("The perimeter is {}".format(zc))
else:
    print("shu ru fei fa")

