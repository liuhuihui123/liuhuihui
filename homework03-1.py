'''#1
num=float(raw_input("Enter an integer,the input ends if it is 0:"))
zh = 0
f = 0
while (num!=0):
    num=float(raw_input("Enter an integer,the input ends if it is 0:"))
    if num > 0:
        zh + = 1
    elif num < 0:
        f + =1
avg = (zh + f)/2
print(zh,f,avg)
'''
'''
#2
'''
'''#3
num=float(raw_input("Enter an integer,the input ends if it is 0:"))
zh = 0
f = 0
while (num!=0):
    num=float(raw_input("Enter an integer,the input ends if it is 0:"))
    if num > 0:
        zh + = 1
    elif num < 0:
        f + =1
avg = (zh + f)/2
print(zh,f,avg)
'''
'''#4
n = 0
for i in range(100,1000):
    if (i%5==0 & i%6==0):
        print(i, ' ',end=' ')
        n +=1
    if n == 10:
        print('\n')
        n=0
'''
'''#5
#n=1
#while n**2 < 12000:
#    n+=1
#print(n)
n=1
while n**3<12000:
    n +=1
print(n)
'''
'''
#8
a,b=1,3
n=1/3
while a<97:
    a+=2
    b+=2
    n = n + a/b
print(n)
'''
#9
num = eval(input(">>"))
sum_ = 0
for i in range(1,num+1):
    sum_ +=pow((-1),(i+1))/(2 * i - 1)
pi = 4 * sum_
print(pi)
'''#10(bu wan zheng)
for i in range(1,10000):
    s = 0
    for k in range(1,i):
        if i%k == 0:
            s=s+k
        if i ==s:
            print(i)
            break
        '''
'''#11
n=0
for i in range(1,8):
    for j in range (1,8):
        print(i , j)
        n +=1
    print(' ')
print(n)
'''

    

