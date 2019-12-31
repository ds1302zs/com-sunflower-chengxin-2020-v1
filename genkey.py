import math
import random
import binascii
import base64
def exp_mode(base, exponent, n):
    bin_array = bin(exponent)[2:][::-1]
    r = len(bin_array)
    base_array = []
    pre_base = base
    base_array.append(pre_base)
    for _ in range(r - 1):
        next_base = (pre_base * pre_base) % n
        base_array.append(next_base)
        pre_base = next_base
    a_w_b = __multi(base_array, bin_array)
    return a_w_b % n
def __multi(array, bin_array):
    result = 1
    for index in range(len(array)):
        a = array[index]
        if not int(bin_array[index]):
            continue
        result *= a
    return result

def tongyu(a,b,n):
    if a%n==b%n:
        return True
    return False

def gcd(a,b):
        while a!=0:
            a,b = b%a,a
        return b
#定义一个函数，参数分别为a,n，返回值为b
def findModReverse(a,m):#这个扩展欧几里得算法求模逆
    if gcd(a,m)!=1:
        return None
    u1,u2,u3 = 1,0,a
    v1,v2,v3 = 0,1,m
    while v3!=0:
        q = u3//v3
        v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
    return u1%m

def proBin(w):  # w表示希望产生位数
    list = []
    list.append(1)  #最高位定为1
    for i in range(w - 2):
        c = random.randint(0, 1)
        list.append(c)
    list.append(1)
    ls2 = [str(j) for j in list]
    ls3 = ''.join(ls2)
    b = int(ls3[0])
    for i2 in range(len(ls3) - 1):
        b = b << 1
        b = b + int(ls3[i2 + 1])
    return b

#因为Python支持大整数运算，所以在此也可以不用快速乘法，而直接使用乘法*。
def quickPower(a, b, c):
    result = 1
    while b > 0:
        if (b & 1):
            result=result*a%c #此为直接乘法
        a=a*a%c #此为直接乘法
        b >>= 1
    return result

#如果返回值为TRUE表示n为素数，返回值为FALSE表示n为合数。
def MillerRabinPrimeTest(n):
    a = random.randint(2,n-2) #随机第选取一个a∈[2,n-2]
    # print("随机选取的a=%lld\n"%a)
    s = 0 #s为d中的因子2的幂次数。
    d = n - 1
    while (d & 1) == 0: #将d中因子2全部提取出来。
        s += 1
        d >>= 1

    x = quickPower(a, d, n)
    for i in range(s): #进行s次二次探测
        newX = quickPower(x, 2, n)
        if newX == 1 and x != 1 and x != n - 1:
            return False #用二次定理的逆否命题，此时n确定为合数。
        x = newX

    if x != 1:  # 用费马小定理的逆否命题判断，此时x=a^(n-1) (mod n)，那么n确定为合数。
        return False

    return True  # 用费马小定理的逆命题判断。能经受住考验至此的数，大概率为素数。


# 经过连续特定次数的Miller-Rabin测试后，
# 如果返回值为TRUE表示n为素数，返回值为FALSE表示n为合数。
def isPrimeByMR(n):
    if ((n & 1) == 0 or n % 5 == 0):
        return False
    for i in range(100):
        if MillerRabinPrimeTest(n) == False:
            return False
    return True

def generate_password():
    import random
    length = 64
    seed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(''.join(random.choice(seed) for _ in range(length)))

def ioput():
    keyp=proBin(2048)
    keyq=proBin(2048)
    while isPrimeByMR(keyp)==False:
        keyp=proBin(2048)
    while isPrimeByMR(keyq)==False:
        keyq=proBin(2048)
    keyN=keyp*keyq
    keyr=(keyp-1)*(keyq-1)
    keye=65537
    keyd=findModReverse(keye,keyr)
    strkeyN=str(keyN)
    strkeye=str(keye)
    strkeyd=str(keyd)
    print("N:")
    bytekeyN=base64.b64encode(strkeyN.encode('utf-8'))
    bytekeye=base64.b64encode(strkeye.encode('utf-8'))
    bytekeyd=base64.b64encode(strkeyd.encode('utf-8'))
    print(str(bytekeyN,'utf-8'))
    print("公钥：")
    print(str(bytekeye,'utf-8'))
    print("私钥：")
    print(str(bytekeyd,'utf-8'))

ioput()
input()
