# -*- coding: utf-8 -*-
import math

a = 123
b = '456'
#print(a + b)
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a + int(b))
print(str(a) + b)


print("---關係運算子 (comparison operator) 需要兩個運算元---")
a = 50
if a > 50:
    print( '大於 50')
elif a < 30:
    print( '小於 30')
else:
    print( '30~50 之間。切記:else 後面就不能再放條件')
    
print('----------------')
#不小心買到Samsung Note 7、聽說電池快沒電時容易有爆炸的風險，怎麼辦?! 利用邏輯運算來提醒我們這個危機吧！
phone = 'iPhone'
battery = 5
if phone == 'Samsung Note 7' and battery < 10:
    print('要爆炸了~快逃!')
elif phone != 'Samsung Note 7' and battery < 10:
    print('幸好不是 note 7, 該充電囉~')
elif phone != 'Samsung Note 7' or battery > 90:
    print('不是 note 7 或電池充飽，沒有爆炸危機')
else:
    print('不知道會花生甚麼事!')



print("---算術運算子 (arithmetic operator) 包含加、減、乘、除、取餘數，皆需兩個運算元 (operand) 構成運算式 (expression) ---")

a = 2
b = 10
print( a+b)
print( a-b)
print( a*b)
print( a/b,',', float(a)/b)
print( a//b)
print( a, ' 的平方 = ' , a , ' ** ' , b , ' = ', a**b)
print( a, ' 的平方 = math.pow(' , a , ',' , b , ') = ', math.pow(a,b))
print( a%b , '餘數')

a = 1.1
print( a, ' 無條件進位 =', math.ceil(a))
print( a, ' 無條件捨去 =',  math.floor(a))
print( a, ' 四捨五入 =', round(a))
print( "==========")
a = 1.9
print( a, ' 無條件進位 =', math.ceil(a))
print( a, ' 無條件捨去 =',  math.floor(a))
print( a, ' 四捨五入 =', round(a))



print("---位元運算子 (bitwise operator) ---")
a = 60            # 60 = 0011 1100  4+8+16+32
b = 13            # 13 = 0000 1101 
c = 0
 
c = a & b;        # 12 = 0000 1100
#  0011 1100 
#  0000 1101
#  0000 1100   兩個為 1 才是 1
print("a & b =", c)
 
c = a | b;        # 61 = 0011 1101 
#  0011 1100 
#  0000 1101
#  0011 1101  只要有一個為 1 就會是 1
print("a | b =", c)
 
c = a ^ b;        # 49 = 0011 0001  =>  0011 1100 ^ 0000 1101
#  0011 1100 
#  0000 1101
#  0011 0001  不一樣的為 1
print("a ^ b =", c)
 
c = ~a;           # -61 = 1100 0011  0011 1100 => 1100 0011
print("~a =", c)
 

print("--- 位移運算子 (shifting operator) 運用在整數資料型態 ---")

c = a << 2;       # 240 = 1111 0000  16+32+64+128
print ("a << 2 =", c)
 
c = a >> 2;       # 15 = 0000 1111  1+2+4+8
print ("a >> 2 =", c)

print("---使用 位移運算子 產生偶數數列 2 4 6 8 10 12 14 16 18-----------")
# 使用 位移運算子 產生偶數數列 2 4 6 8 10 12 14 16 18
for x in range(1, 10):
    print(x, x << 1)

print("---使用 位移運算子 產生奇數列 1 3 5 7 9 11 13 15 17 19-----------")
# 使用 位移運算子 產生奇數列 1 3 5 7 9 11 13 15 17 19
for x in range(2, 40, 4):
    print(x, (x >> 1))

#更簡單的方式    
print("----產生偶數數列 2 4 6 8 10 12 14 16 18----------")
for x in range(2, 20, 2):
    print(x)
print("----產生奇數列 1 3 5 7 9 11 13 15 17 19----------")
for x in range(1, 20, 2):
    print(x)
    
    
print('---------迴圈-------')
#for [變數名稱] in range(範圍, 比如從數字X到Y):    
for i in range(0, 10):
   print(i)

print('--------99乘法表--------')
#如果不希望print出來的結果換行且要有空格，可以使用end=’ ’
# Python 2.x for end=" " is print i, 
for i in range(1, 10):
    for j in range(1, 10):
        print(i , '*' , j, '=' , i*j, ' ', )
    print('\n')

print('-------從1到10、每次加2的數列---------')
for i in range(1, 10, 2):
    print(i)

print('-------從10到2、每次-3的數列---------')
for i in range(10, 1, -3):
    print(i)    
    
print('------ LIST ----------')
a = ['Lynn', 0.87, 1234, True]
print(len(a))
#print(a[0])
#print(a[1])
#print(a[2])
for i in range(0, len(a)):
    print(a[i])

for i in a:
    print(i)

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
print(a)
a.append(4)
print(a)
a.insert(2, 2.5)
print(a)
print(sum(a))

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[  : 2])
print(a[ 2:  ])
print(a[ 2: 5])
print(a[  :  ])

print('------ Dict 字典 ----------')
a = { 'one': 1, 'two': 2, 'three': 3 }
print(a)
print(a['one'])
print(a['two'])
print(a['three'])
del a['two']
print(a)
a['four'] = 4
print(a)
# print(a['not_found'] 
# KeyError: 'not_found'
print(0 in a.keys()) # return false
print(1 in a.values()) # return true
print('three' in a.keys()) # return true
print(9 in a.values()) # retun false
#a.get(key, default_value)
print(a.get('two', '找無')) # return 找無, 因為被刪了
print(a.get('four', '找無')) # return 4
print(a['four'])  # 會 exception KeyError, 沒 default value


#
#分隔符號 - 其他分隔符號有
#分隔符號	功能
#( )	小括弧圍住的運算式會優先計算，函數 (function) 也用小括弧圍住參數列 (parameter list)
#[ ]	序列型態 (sequence type) 的索引符號，或用作定義串列 (list)
#{ }	用作定義字典 (dictionary)
#,	同一行中分隔多個運算式
#:	控制陳述條件 (condition) 後的分隔符號
#.	用為存取物件的方法 (method) 或屬性 (attribute)
#;	可作為單行程式結束的符號，也可不用
#@	用作函數或類別 (class) 定義的特殊標記
