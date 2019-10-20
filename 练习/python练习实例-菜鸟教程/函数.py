# def f(a,data=[]):
#     data.append(a)
#     return data

# def f1(a,data=None):
#     if data is None:
#         data=[]
#     data.append(a)
#     return data

# print(f(1))
# print(f(2))
# print(f(3))
# print("\n")
# #比较一下前后输出的不同
# print(f1(1))
# print(f1(2))
# print(f1(3))

#高阶函数
#高阶函数（Higher-order function）或仿函数（functor）是可以接受函数作为参数的函数：
#使用一个或多个函数作为参数
#返回另一个函数作为输出

# def high(l):
#     return [i.upper() for i in l]

# def test(h,l):
#     return h(l)

# l=["i","am","zw1sh"]
# print(test(high,l))


#map 函数
#map 是一个在 Python 里非常有用的高阶函数。它接受一个函数和一个序列（迭代器）作为输入，然后对序列（迭代器）的每一个值应用这个函数，返回一个序列（迭代器），其包含应用函数后的结果

# l=[1,2,3,4,5]
# def square(num):
#     return num*num

# print(list(map(square,l)))