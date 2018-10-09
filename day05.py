'''#1
class joker:
    print('joker is a good man')
if __name__ == '__main__':
    joker()
'''
'''class joker:
    print('joker is a good man')
class joker2:
    a = 1000
    print a
if __name__ == '__main__':
    print joker2
'''
'''
class jiou:
    def __init__(self):
        self.shu = eval(raw_input("shu ru >>"))
    def fuc(self):
        if self.shu % 2 == 0:
            print '[+] ou'
        else:
            print '[+] ji'
if __name__ == '__main__':
    jiou().fuc()
'''
'''
#EP2
class ep2:
    def __init__(self):
        self.num = 10
        print ' init over! '
    def num_2(self):
        #NUM2 = self.num ** 2
        #self.num = NUM2
        self.num = self.num ** 2
        print self.num
    def num_3(self):
        self.num = self.num ** 3
        print self.num
if __name__ == '__main__':
    huwang = ep2() #shi li hua dui xiang
    huwang.num_2()
    huwang.num_3()
'''
'''
#lei
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def getArea(self):
        res = self.width * self.height
        print res
    def getP(self):
        res2 = 2 * (self.width + self.height)
        print res2
Rectangle(4,40).getArea()
Rectangle(4,40).getP()
'''


