# 计算一个数的欧拉函数
import gmpy2
p =gmpy2.mpz(18443)
q =gmpy2.mpz(49891)
e =gmpy2.mpz(19)
phi_n= (p - 1) * (q - 1)
d = gmpy2.invert(e, phi_n)
print("d is:")
print (d)