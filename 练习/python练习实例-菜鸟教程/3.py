#!/usr/bin/python
#coding=utf-8
#计算日期是当年的第几天
year=int(input('year:\n'))
month=int(input('month:\n'))
day=int(input('day:\n'))

#累计每月的天数
months = (0,31,59,90,120,151,181,212,243,273,304,334)

if 0<month<=12:
	sum=months[month-1]
else:
	print('month error')
sum+=day
leap=0
if(year%400==0) or ((year%4==0) and (year%100!=0)):
	leap=1
if(leap==1) and (month>2):
	sum+=1
print('it is %dth day'%sum)