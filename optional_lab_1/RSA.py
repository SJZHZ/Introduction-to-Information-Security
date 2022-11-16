'''
《信息安全引论》选做实验一
实现 RSA 算法
by 1900017702 ZY
'''
import gmpy2
import random
from math import gcd
from Crypto.Util.number import getPrime
# 注意源代码中的Crypto包 对应的是 安装名称pycrypto

class RSA:
    def __init__(self):                 # 构造函数
        # P, Q, N, E, D
        self.P, self.Q = getPrime(1024), getPrime(1024)     # 随机生成
        self.N = self.P * self.Q
        self.phi = (self.P - 1) * (self.Q - 1)
        while True:                                 # 随机抽取，直到符合条件
            self.E = random.randint(1, self.phi - 1)
            if gcd(self.E, self.phi) == 1:
                break
        self.D = gmpy2.invert(self.E, self.phi)
        # public key
        print("E: ", self.E)
        print("N: ", self.N)

    def Encryption(self, Msg):          # 加密
        Cry = pow(Msg, self.E, self.N)              # 计算密文
        return Cry

    def Decryption(self, Cry):          # 解密
        Msg = pow(Cry, self.D, self.N)              # 计算明文
        return Msg

# 测试语句
test = RSA()
Msg = int(input('M(in): '))
Cry = test.Encryption(Msg)
print('C(out): ', Cry)

Cry = int(input('C(in): '))
MsgMsg = test.Decryption(Cry)
print('M(out): ', MsgMsg)