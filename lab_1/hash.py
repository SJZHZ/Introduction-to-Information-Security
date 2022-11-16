import hashlib
print("请输入 sha1 的值，将根据前 20 位寻找原值")
x = input().lower()
print("\n 请输入任意数据，将根据前 20 位寻找碰撞")
y = input()
sha = hashlib.sha1()
sha.update(y.encode('utf-8'))
sha_y = sha.hexdigest()
print("输入数据的 HASH 为：" + sha_y)
a, b = 0, 0
for i in range(0,10000000):
    tmp = str(i)
    sha.update(tmp.encode('utf-8'))
    sha_tmp = sha.hexdigest()
    if sha_tmp[0:5] == x[0:5]:
        print(x[0:5])
        a+=1
        print("type1：找到原值：" + str(i) + "。其 HASH 值为：" + sha_tmp)
    if sha_tmp[0:5] == sha_y[0:5] and i != y :
        b+=1
        print("type2：找到碰撞：" + str(i) + "。其 HASH 值为：" + sha_tmp)
print("原值次数", a, "碰撞次数", b)