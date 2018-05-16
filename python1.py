#coding:utf-8
#SyntaxError: Non-ASCII character '\xe5' in file main.py on line 37, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
import math

print 'hello world 1'
print "hello world 2"
print ('hello world 3')
print('hello world 4')


a = 123
print type(a)

a = '456'
print type(a)

a = 8.70
print type(a)

a = -3
b = 4
print abs(a)
print max(a, b)
print min(a, b)

a = 123
b = '456'
#print a + b

print a + int(b)
print str(a) + b

print '------ [+,-,*,/, **, //]----------'
a = 2
b = 10
print a+b
print a-b
print a*b
print a/b,',', float(a)/b
print a//b
print a, ' 的平方 = ' , a , ' ** ' , b , ' = ', a**b
print a, ' 的平方 = math.pow(' , a , ',' , b , ') = ', math.pow(a,b)
print a%b , '餘數'

a = 1.1
print a, ' 無條件進位 =', math.ceil(a) 
print a, ' 無條件捨去 =',  math.floor(a)
print a, ' 四捨五入 =', round(a)
print "=========="
a = 1.9
print a, ' 無條件進位 =', math.ceil(a) 
print a, ' 無條件捨去 =',  math.floor(a)
print a, ' 四捨五入 =', round(a)

# Python3  
#a = input('your name:')
# Python 2
#a = raw_input('your name:')
#print 'a=', a

print '----------------'
a = 50
if a > 50:
    print '大於 50'
elif a < 30:
    print '小於 30'
else:
    print '30~50 之間。切記:else 後面就不能再放條件'
    
print '----------------'
#不小心買到Samsung Note 7、聽說電池快沒電時容易有爆炸的風險，怎麼辦?! 利用邏輯運算來提醒我們這個危機吧！
phone = 'iPhone'
battery = 5
if phone == 'Samsung Note 7' and battery < 10:
    print '要爆炸了~快逃!'
elif phone != 'Samsung Note 7' and battery < 10:
    print '幸好不是 note 7, 該充電囉~'
elif phone != 'Samsung Note 7' or battery > 90:
    print '不是 note 7 或電池充飽，沒有爆炸危機'
else:
    print '不知道會花生甚麼事!'

print '---------迴圈-------'
#for [變數名稱] in range(範圍, 比如從數字X到Y):    
for i in range(0, 10):
   print i

print '--------99乘法表--------'
#如果不希望print出來的結果換行且要有空格，可以使用end=’ ’
# Python 2.x for end=" " is print i, 
for i in range(1, 10):
    for j in range(1, 10):
        print i , '*' , j, '=' , i*j, ' ', 
    print '\n'

print '-------從1到10、每次加2的數列---------'
for i in range(1, 10, 2):
    print i

print '-------從10到2、每次-3的數列---------'
for i in range(10, 1, -3):
    print i    
    
print '------ LIST ----------'
a = ['Lynn', 0.87, 1234, True]
print len(a)
#print a[0]
#print a[1]
#print a[2]
for i in range(0, len(a)):
    print a[i]

for i in a:
    print i

#建立一個空的list: a = list() 或是 a = []都可以
#list.append(x): 把變數x塞到list的最後面
#list.insert(i, x): 把變數x塞到i這個位置上
#list.pop(): 把list的最後一格丟掉
#list.pop(i): 把list的第i格丟掉
#list.remove(x): 會把第一個出現的變數x拿掉
#list.clear(): 把list內的資料全部清光光
#max(list): 找出list中最大值
#min(list): 找出list中最小值
#sum(list): 找出list數字總和

a = [1, 2, 3]
print a
a.append(4)
print a
a.insert(2, 2.5)
print a
print sum(a)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print a[  : 2]
print a[ 2:  ]
print a[ 2: 5]
print a[  :  ]

print '------ Dict 字典 ----------'
a = { 'one': 1, 'two': 2, 'three': 3 }
print a
print a['one']
print a['two']
print a['three']
del a['two']
print a
a['four'] = 4
print a
# print a['not_found'] 
# KeyError: 'not_found'
print 0 in a.keys() # return false
print 1 in a.values() # return true
print 'three' in a.keys() # return true
print 9 in a.values() # retun false
#a.get(key, default_value)
print a.get('two', '找無') # return 找無, 因為被刪了
print a.get('four', '找無') # return 4
print a['four']  # 會 exception KeyError, 沒 default value


