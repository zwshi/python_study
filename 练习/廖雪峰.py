#1、对字符串两边有的空格进行切片处理
# -*- coding: utf-8 -*-
def trim(s):
    if len(s) > 0:
        if s[0] == ' ':
            return trim(s[1:])
        elif s[-1] == ' ':
            return trim(s[:-1])
        else:
            return s
    else:
        return s
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


#2、找出最大最小值
# -*- coding: utf-8 -*-
def findMinAndMax(L):
	if L==[]:
		return (None,None);
	else:
		max=L[0];
		min=L[0];
		for i in L:
			if i>=max:
				max=i;
			elif i<min:
				min=i;
		return (min,max);
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# list中既包含字符串，又包含整数，将字符串提取出来并转换为小写
# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [i.lower() for i in L1 if isinstance(i,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 利用生成器生成杨辉三角
# -*- coding: utf-8 -*-
def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

