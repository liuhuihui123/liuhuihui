'''#1
import math
r = float(raw_input("Enter the length from the center to a vertex:"))#ding dian dao zhong xin de ju li r
s = 2 * r * math. sin(math.pi/5) #bian chang ji suan gong shi 
area = 5 * s * s / (4 * math.tan(math.pi/5))
print("The area of the pentagon is:{:.2f}".format(area))
'''
'''
#2
import math
x1,y1 = eval(raw_input("Enter point 1 (latitude and longitude) in degrees:"))
x2,y2 = eval(raw_input("Enter point 2 (latitude and longitude) in degrees:"))
radius = 6371.01 #di qiu ban jin
d1 = math.sin(math.radians(x1)) * math.sin(math.radians(x2))
d2 = math.cos(math.radians(x1)) * math.cos(math.radians(x2))*math.cos(math.radians(y1-y2))
d = radius * math.acos(d1 + d2)
print("The distance between the two points is {:.11f} km".format(d))
'''
'''#3
import math
s = eval(raw_input("Enter the side:")) #s wei bian chang 
a1 = 5 * math.pow(s,2)
a2 = 4 * math.tan(math.pi/5)
area = a1 / a2
print("The area of the pentagon is {:.6f}".format(area))
'''
'''#4
import math
n = float(raw_input("Enter the number of sides:")) # n wei bian shu 
s = float(raw_input("Enter the side:")) #s wei bian chang
a1 = n * math.pow(s,2)
a2 = 4 * math.tan(math.pi/n)
area = a1 / a2
print("The area of the polygon is {:.4f}".format(area))
'''
'''#5
num = eval(raw_input("Enter an ASCII code(0 ~ 127):"))
print(chr(num))
'''
'''#6
name = raw_input("Enter employee's  name:")
shijian =  eval(raw_input("Enter number of hours worked in a week:"))
baochou = eval(raw_input("Enter hourly pay rate:"))
lianbangyukou = eval(raw_input("Enter federal tax withholding rate:"))
zhouyukou = eval(raw_input("Enter state taxwithhoiding rate:"))
zhonge = shijian * baochou
lbyukou = zhonge * 0.2
zyukou = zhonge * 0.09
zhongkou = lbyukou + zyukou
zheng = zhonge - zhongkou
print("Employee Name:{}".format(name))
print("Hours Worked:{}".format(shijian))
print("Pay Rate:${}".format(baochou))
print("Gross Pay:${}".format(zhonge))
print("Deductions:")
print("   Federal Withhoiding (20.0%):${}".format(lbyukou))
print("   State Withhoiding (9.0%):${}".format(zyukou))
print("   Total Deduction:${}".format(zhongkou))
print("Net Pay:${}".format(zheng))
'''
'''#7
num = eval(raw_input("Enter an integer:"))
qian = num / 1000
bai = (num%1000)/100
shi = (num%100)/10
ge = num % 10
fx = ge*1000 + shi*100 +bai*10+qian
print(fx)
'''
'''#8
res = ' ' 
for i in "943663522@qq.com":
    res = res + chr (ord(i) + 1)
print(res)
'''

