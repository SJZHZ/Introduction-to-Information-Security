# 选做实验一
```
1900017702 ZY
```
要求见pdf文档
## 实现RSA算法
### 代码说明
> 实现了一个RSA类
>- 构造函数：\_init_() -> None
>   1. 随机生成素数P, Q
>   2. 计算N, phi
>   3. 限制性随机生成D
>   4. 计算E
>   5. 五元组(P, Q, N, D, E)即为一个RSA对象的内含参数
>   6. 打印公钥(E, N)
>   7. 保存私钥(P, Q, D)
>- 加密函数：Encryption(Msg:int) -> int
>   > Cry = (Msg ** E) % N
>- 解密函数：Decryption(Cry:int) -> int
>   > Msg = (Cry ** D) % N
### 操作流程
1. 运行.py文件
    > 自动生成一个随机化的RSA类<br>
    > 运行一次加密，一次解密
2. 输入明文Msg
    > 输出密文Cry
3. 输入密文CryCry
    > 输出明文MsgMsg
### 注意事项
1. 使用pip加载Crypto模型时，要使用名称pycrypto，而不是Crypto
2. Crypto模型版本太老，不适应最新的python版本：其中的time.clock()应修改为time.perf_counter()