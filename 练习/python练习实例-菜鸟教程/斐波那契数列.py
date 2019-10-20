#!/usr/bin/python3
'''
生成器，迭代器
使用了yield的函数被称为生成器，生成器是一个返回迭代器的函数，在调用生成器运行的过程中，每次遇到yield时，函数会暂停并保存当前所有运行的运行信息，返回yield的值，并在下一次执行next()方法是从当前位置继续运行
'''
import sys
def fibonacci(n):
	a,b,counter=1,1,0
	while True:
		if(counter>n):
			return
		yield a
		a,b=b,a+b
		counter+=1

f=fibonacci(10)  #f是一个迭代器，由生成器返回生成
while True:
	try:
		print(next(f),end=' ')
	except StopIteration:
		sys.exit()
