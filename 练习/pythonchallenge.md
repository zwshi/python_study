2、

```python
def mov2(str):
	s=""
	for i in str:
        	if i == 'z':
            		r='b'
        	elif i=='y':
            		r='a'
        	elif i.isalpha():
            		j=ord(i)
            		r=chr(j+2)
        	else:
        		r=i
        	s=s+r
        return s

str='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
print mov2(str)
print mov2("map")

            
```



3、

```python
#coding=utf-8
import requests
r=requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")
print r.text


def rare(str):
    dict_char_tmp={i:str.count(i) for i in str}
    return dict_char_tmp

def sort(t):
    retrun sorted(t,key=lambda x:x[1])
fp=open(r'/zw/pythonweb_study/test','r')
str=fp.read()
fp.close
k=rare(str)
print k
m=sort(k.items())
min=m[0][1]
ans=""
for i in m:
    if i[1]==min:
        ans=ans+i[0]
print ans
```

