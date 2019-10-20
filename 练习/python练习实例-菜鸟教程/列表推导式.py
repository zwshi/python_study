#列表推导式
v1=[1,2,3]
v2=[4,5,6]
l=[x*y for x in v1 for y in v2]
print(l)

#嵌套列表解析
#将3x4矩阵转换为4x3
matrix=[
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12]
]

matrix1=[[row[i] for row in matrix] for i in range(4)]  #后面的为外层循环
print(matrix1)