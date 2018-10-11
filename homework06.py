#1


'''
#2
def Str(str1,str2):
    print str2.find(str1)
str1 = raw_input("shu ru yi ge zi fu chuan : ")
str2 = raw_input("shu ru yi ge zi fu chuan : ")
Str(str1,str2)
'''
#3


'''
#4
def countLetters(str1):
    sum_ = 0
    for i in range (len(str1)):
        if (str1[i] >= 'a' and str1[i] <= 'z') or (str1[i] >= 'A' and str1[i] <= 'Z'):
            sum_ +=1
    print sum_
str1 = raw_input('shu ru yi chuan zi fu chuan:')
countLetters(str1)
'''
'''
#5
def Num(num1):
    for i in range(len(num1)):
        if num1[i] >= '0' and num1[i] <= '9':
            print num1[i]
        elif (num1[i] >= 'a' and num1[i] <='c') or (num1[i] >='A' and num1[i] <= 'C'):
            print 2
        elif (num1[i] >= 'd' and num1[i] <='f') or (num1[i] >='D' and num1[i] <= 'F'):
            print 3
        elif (num1[i] >= 'g' and num1[i] <='i') or (num1[i] >='G' and num1[i] <= 'I'):
            print 4
        elif (num1[i] >= 'j' and num1[i] <='l') or (num1[i] >='J' and num1[i] <= 'L'):
            print 5
        elif (num1[i] >= 'm' and num1[i] <='o') or (num1[i] >='M' and num1[i] <= 'O'):
            print 6
        elif (num1[i] >= 'p' and num1[i] <='s') or (num1[i] >='P' and num1[i] <= 'S'):
            print 7
        elif (num1[i] >= 't' and num1[i] <='y') or (num1[i] >='T' and num1[i] <= 'Y'):
            print 8
        elif (num1[i] >= 'w' and num1[i] <='z') or (num1[i] >='W' and num1[i] <= 'Z'):
            print 9
num1 = raw_input('Enter phone number:')
Num(num1)
'''
'''
#6
def reverse(s):
   # print s[::-1]
   str = list (s)
   str.reverse()
   res = ''.join(str)
   print res
s = raw_input('shu ru yi ge zi fu chuan:')
reverse(s)
'''
'''
#7
def checkCard(card_num):
    card_list = list (card_num)
    print (card_list)
    Res = 0
    Res_2 = 0
    for i in range(len(card_list)):
        res = int(card_list[i]) * 2
        if res >= 10:
            res_1 = res % 10
            res_2 = res // 10
            res_3 = res_1 + res_2
        else:
            Res += res
        if i % 2 != 0:
            Res_2 += int(card_list[i])
    RES = Res + Res_2
    if RES % 10 == 0:
        print('he fa')
    else:
        print('bu he fa')
card_num = '438857601840707'
checkCard(card_num)
'''         
'''
#8
#d = raw_input('Enter the first 12 digits of an ISBN-13 as a string: ')
#i = 10 - len((d[0] + 3*d[1] + d[2] + 3*d[3] + d[4] + 3*d[5] + d[6]  + 3*d[7] + d[8] + 3*d[9] + d[10] + 3*d[11])) % 10
#li = list (d)
#li.append(i)
#print li

def chechISBN(str_):
    str_list = list(str_)
    SUM = 0
    for i in range(len(str_list)):
        if  i % 2 == 0:
            res = int(str_list[i]) * 3
        else:
            res = int(str_list[i])
        SUM += res
    RES = 10 - SUM % 10
    if RES == 10:
        RES = 0
    print ( RES)
str_ = raw_input('>>')
chechISBN(str_)
'''
'''


