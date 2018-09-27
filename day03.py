'''
a = 'abcde'
i = 0
while i < 5:
    print(a[i])
    i +=1
'''
'''#cai shu zi
import random
number = random.randint(1,10)
input_num = eval(raw_input("shu ru yi ge shu zi :"))
if number == input_num:
    print('Good')
else:
    while number != input_num :
        input_num = int(raw_input('again:'))
        if number == input_num:
            print('Good')
        else:
            print('Error')
'''
'''sum = 0
for i in range(1001):
    sum = sum +1
    '''
'''i = 0
sum_ = 0
while i<1001:
    sum_ +=i
    i +=1
print(sum_)
'''

'''i = 1
sum_ = 0
while sum_ < 10000:
    sum_ += i
    i += 1
print(sum_)
'''
'''sum_ = 0
for i in range(142):
    sum_ +=i
print(sum_)
'''
'''#9 * 9 cheng fa biao
i=1
for i in range(10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end='  ')
    print()
'''
#hanshu
def fun1(num1,num2,num3):
    return num1,num2,num3
def fun2(num1,num2,num3):
    n1 = num1 **2
    n2 = num2**2
    n3 = num3**2
    return n1,n2,n3
def fun3(num1,num2,num3,num4,num5,num6):
    res1 = num4 - num1
    res2 = num5 - num2
    res3 = num6 - num3
    print(res1,res2,res3)
a,b,c = fun1(1,2,3)
q,w,e = fun2(a,b,c)
fun3(a,b,c,q,w,e)

