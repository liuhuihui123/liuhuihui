'''# 1.
celsius = int(raw_input("Enter a degree in celsius:>>"))
fahrenheit = (9.0 / 5.0) * celsius + 32
print(fahrenheit)
'''
'''#2.
radius = float(raw_input("shu ru radius:>>"))
length = float(raw_input("shu ru length:>>"))
area = radius * radius * 3.14
volume = area * length
print(area)
print(volume)
'''
'''#3.
feet = float(raw_input("Enter a value for feet:>>"))
meters = feet * 0.305
print(meters)
'''
'''#4.
kilograms = float (raw_input("Enter the amount of water in kilograms:>>"))
initialtemperature = float (raw_input("Enter the initial temperature:>>"))
finaltemperature = float (raw_input("Enter the final temperature:>>"))
Q = kilograms * (finaltemperature - initialtemperature) * 4184
print(Q)
'''
'''#5.
balance,rate= eval(raw_input("Enter balance and interest rate (e.g., 3 for 3%):>>"))
lx = balance * (rate/1200.0)
lx=round(lx,5)
print(lx)
'''
'''#6.
v0,v1,t = eval(raw_input("Enter v0,v1 and t:>>"))
a = (v1-v0)/t
a = round(a,4)
print(a)
'''
'''#7.
amout = float(raw_input("Enter the monthly saving amout:>>"))
ll = 0.05/12
m1 = amout * (1+ll)
m2 = (amout + m1) * (1+ll)
m3 = (amout + m2) * (1+ll)
m4 = (amout + m3) * (1+ll)
m5 = (amout + m4) * (1+ll)
m6 = (amout + m5) * (1+ll)
m6 = round(m6 , 2)
print(m6)
'''
#8.
number = eval(raw_input("Enter a number between 0 and 1000:>>"))
bai = number / 100
shi = number / 10 % 10
ge = number % 10
sum = bai + shi + ge
print (sum)

