'''
输出九九乘法表
version:1.0
Author:zw1sh
主要知识点：制表符'\t'
'''

for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(i,j,i*j),end='\t')
    print()
