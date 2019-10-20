#coding=utf-8
'''
class student(object):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def get_grade(self):
        if self.grade >=90:
            return 'A'
        elif self.grade >=60:
            return 'B'
        else:
            return 'C'
    
    def print_grade(self):
        print(self.get_grade())

lisa = student('Lisa', 99)
bart = student('Bart', 59)
print(lisa.name+': ')
lisa.print_grade()
print(bart.name+': ')
bart.print_grade()

1、
在Python中，定义类是通过class关键字
可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

2、访问限制
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
'''

# Python内置的@property装饰器负责把一个方法变成属性调用的
