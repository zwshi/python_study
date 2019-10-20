f=open("C:/Users/zw/Desktop/jiang.txt")
s=f.read()
res=""
for c in s:
    if c.isdigit():
        res+=c
print(res)
