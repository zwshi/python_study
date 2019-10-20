import sys
def mintoH(m):
    if m<60:
        n=m
        h=0
    elif m==60:
        n=0
        h=1
    elif m<0:
        raise ValueError("Input number cannot be negative")
    else:
        h=int(m/60)
        n=m%60
    print("{0} H,{1} M".format(int(h),int(n)))

try:
    mintoH(int(sys.argv[1]))
except:
    print("Parameter Error")