# coding:utf8
import hashlib

# 明文为： TASC_O3RJMV_WDJKX_ZM
# 密文为 : e9032___da___08____911513_0___a2

str1 = "TASC"
str2 = "O3RJMV"
str3 = "WDJKX"
str4 = "ZM"

# 将所有可打印字符存入数组 , 用于遍历所有字符
res = ['  ', '!', '"', '#', '$', '%', '&','(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

def getMd5(plaintext):
    md5Object = hashlib.md5()
    #md5Object.update(str(plaintext))
    md5Object.update(plaintext.encode("utf8"))  # 指定编码格式，否则会报错
    return md5Object.hexdigest()

for i in res:
    for j in res:
        for k in res:
            plaintext = str1 + i + str2 + j + str3 + k + str4 # 拼接明文字符串
            print(plaintext + " ",)
            md5 = getMd5(plaintext)
            print(md5)
            # 判断是否成功
            if md5.startswith("e9032") and md5.endswith("a2"):
                print("Success ! The plaintext is : " + plaintext)
                exit(0)