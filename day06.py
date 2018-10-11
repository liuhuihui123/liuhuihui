#EP1
url = 'http://www.baidu.com/?page=?wd=xiaopangzi'
for i in range(100):
    part1 = 'http://www.baidu.com/?page='
    res = part1 + str(i) + '?wd=xiaopangzi'
    print res

