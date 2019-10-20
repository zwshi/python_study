#coding=utf-8

'a test module'
__author__='zwish'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print("hello,world")
    elif len(args)==2:
        print("hello,%s"% args[1])
    else:
        print("too much")

if __name__=='__main__':
    test()


'''
第3行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
第四行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以看到作者

1、sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
2、最后两行：当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，
因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
3、作用域
正常的函数和变量、特殊变量、非公开(private)函数和变量
类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途
类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
例：private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
'''