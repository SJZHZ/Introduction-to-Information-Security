# 实验作业一
```
1900017702 ZY
```
要求见pdf文档
## 单向哈希函数与MAC实验
https://www.lanqiao.cn/courses/242
### 实验1:生成消息摘要和MAC
```bash
openssl dgst -[dgsttype] [filename]
```
### 实验2:Keyed Hash和HMAC
```bash
openssl dgst -[dgsttype] -hmac [key] [filename]
```
### 实验3:单向哈希函数的随机性
代码用的是python2，建议在在线实验平台上完成<br>
翻转文件的任意一位，比较前后的Hash值
### 实验4:单向特性（One-Way）与避免冲突特性（Collision-Free）的对比
源文件见hash.py，代码用的是python3，建议在本地完成
<br>
- 朴素的描述性原理：<br>
    > 假设hash函数是统计上均匀分布的，那么【破解次数的期望】就等于【指定满射，随机取值结果正确的概率】的倒数，即E(N)=1/P。<br>
    > 而本题中不论是碰撞还是原值都只检验前五位，所以统计上看它们映射到正确值的概率P均为(1/16)^5，E(N)= 1048576，和实验结果N=10^6差别不太大

## 密钥加解密实验
https://www.lanqiao.cn/courses/241
### 实验1:使用不同的加密算法与加密模式进行加密
```bash
openssl [enc]-[ciphertype] [-e/-d] \
-in [明文/密文] -out [密文/明文] \
-K [十六进制密钥] -iv [十六进制初始向量]
```
### 实验2:加密模式——ECB与CBC的区别
1. 下载图片
2. 分别使用 ECB 和 CBC 模式加密
```bash
openssl enc -aes-128-cbc -e -in pic_original.bmp -out pic_cbc.bmp \
-K 00112233445566778899aabbccddeeff \
-iv 0102030405060708

openssl enc -aes-128-ecb -e -in pic_original.bmp -out pic_ecb.bmp \
-K 00112233445566778899aabbccddeeff \
-iv 0102030405060708
```
3. 修改加密后文件的文件头
- hex editor
    > 按字节读取，是base64而非utf-8形式
4. 打开图片，观察结果
> ecb加密还能看出图的部分效果，说明还保留了原数据的部分统计信息。<br>
> 而cbc加密则更加混乱，基本看不出原图的样子。