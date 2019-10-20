#方法 title() 返回字符串的标题版本，即单词首字母大写其余字母小写。
# s="woshi1shui"
# print(s.title())

#方法 upper() 返回字符串全部大写的版本，反之 lower() 返回字符串的全部小写版本

#方法 swapcase() 返回字符串大小写交换后的版本 :）
# s="i am A Student"
# print(s.swapcase())

#方法 isalnum() 检查所有字符是否只有字母和数字，上面的代码中第一行的字符串 s 中包含空格字符，所以返回 False。
# s="i am A Student"
# print(s.isalnum());

#方法 isalpha() 检查字符串之中是否只有字母。
# s="asdasdasdas"
# print(s.isalpha())

#还有类似的：isdigit()、islower()、isupper()

#split()
# s="we are good man"
# print(s.split())
# p="1,2,3,4,5,6.7"
# print(p.split(","))
# #join()
# print("-".join("GNU/linux is good".split()))

#字符串剥离,strip(chars)玻璃指定的字符，如果没指定，则剥离首尾的空格和换行符
# s="  asda dw\n"
# print(s.strip())
# #使用lstrip()和rstrip()指定剥离方向
# print(s.lstrip())
# print(s.rstrip())

#文本搜索find(),找到第一个匹配的字符的位置，从0开始计数
# s="asdasdasddsfasdf0"
# print(s.find("s"))

# #回文检测
# s=input("请输入字符串:")
# r=s[::-1]
# if s==r:
#     print("是回文")
# else:
#     print("不是回文")

# #单词计数
# s=input("请输入要计数的语句:")
# print("一共有{0}个单词".format(len(s.split())))
