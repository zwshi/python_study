'''
输入两个正整数计算他们的最大公约数和最小公倍数
Author:zw1sh
考点：range()的三个参数
'''

x=int(input("x="))
y=int(input("y="))

if x>y:
    x,y=y,x
for fac in range(x,0,-1):
    if x%fac==0 and y%fac==0:
        print('%d和%d的最大公约数是%d' % (x, y, fac))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // fac))
        break