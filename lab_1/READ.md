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
> ECB加密还能看出图的部分效果，说明还保留了原数据的部分统计信息。<br>
> 而CBC加密则更加混乱，基本看不出原图的样子。
### 实验3:加密模式——损坏的密文
- 加密
```bash
openssl enc -aes-128-ecb -e -in corrupted.txt -out cipher_aes_128_ecb.bin \
-K 0011223344556677889aabbccddeeff \
-iv 0102030405060708
```
- 修改
    > hex editor
- 解密
```bash
openssl enc -aes-128-ecb -d -in cipher_aes_128_ecb.bin -out decrypted.txt \
 -K 0011223344556677889aabbccddeeff \
 -iv 0102030405060708
```
- 对比
    > 实验：OFB只有一个字符错误，而ECB,CBC,CFB都发生了多个字符的错误
    > 理论：对于一处修改，OFB, ECB都只影响自己所在的单元，而CBC影响两个块，CFB则影响全部后续单元
### 实验4:填充
```bash
ll
```
OFB和CFB不填充，而CBC和ECB都作了填充
### 实验5:使用Openssl加密库进行编程
部分代码段如下，完整代码见课程页面
```C
#include<openssl/conf.h>
#include<openssl/evp.h>
#include<openssl/err.h>
int encrypt(unsigned char *plaintext, int plaintext_len,
    unsigned char *key, unsigned char *iv, unsigned char *ciphertext)
{
    //
    调用
    //
    return ciphertext_len;
}
```
### 实验6:生成伪随机数
1. 内核熵（entropy）
    > 计算机本身并不适合生成随机数，所以大多数系统通过物理资源获得随机性。比如 linux 通过以下函数获得随机性。
    ```C
    void add_keyboard_randomness(unsigned char scancode);
    void add_mouse_randomness(__u32 mouse_data);
    void add_interrupt_randomness(int irq);
    void add_blkdev_randomness(int major);
    ```
    > 前两个很好理解，第一个利用键盘按键时序和所按键的对应码，第二个利用鼠标的移动和中断时序。第三个利用所有的中断时序收集随机性，当然，并不是所有的中断都有好的随机性，比如时间中断就是可以预测的，而硬盘中断是一个好选择，第四个函数计算设备块请求的完成时间。<br>
    > 我们使用熵来衡量随机性，在这里熵只意味着计算机当前拥有多少位随机比特。以下命令可以得到系统当前拥有熵的数量：
    ```bash
    cat /proc/sys/kernel/random/entropy_avail
    ```
    > 请移动或者点击鼠标，敲敲键盘，拿电脑闷泡面或者对电脑做点别的什么，之后再一次运行上面的命令，描述你的观察。
2. 从 /dev/random 获得伪随机数
    > Linux 将从物理世界得到的随机数据存于一个随机池中，再由两个设备把随机数据转化成伪随机数。这两个设备有着不同的行为，我们先来学习 /dev/random。<br>
    > 你可以使用以下命令从 /dev/random 得到 16 字节的伪随机数，我们把数据 pipe 到 hexdump 中查看内容。
    ```bash
    head -c 16 /dev/random | hexdump
    ```
    > hexdump：一般用来查看“二进制”文件的十六进制编码<br>
    > 请多次运行该命令，你会发现命令发生阻塞，因为每次取出伪随机数都会导致随机池的熵减少，当熵用完的时候，设备就会被阻塞直到获得足够的熵。请做点什么解决阻塞，让命令打出随机数来。
3. 从/dev/urandom 获得伪随机数
    > 此设备不会被阻塞，即使随机池的熵已经相当低了。 你可以使用以下命令从/dev/urandom 获得 1600 字节的伪随机数，运行几次检测该设备是否会阻塞。
    ```bash
    head -c  1600 /dev/urandom | hexdump
    ```
    > /dev/random 与 /dev/urandom 都是从池中取出随机数据来生成伪随机数的。当熵不够用的时候，/dev/random 会阻塞，而 /dev/urandom 则会持续生成新的数。请把池中的数据看作种子（seed），我们都知道，一颗种子能够生成任意数量的伪随机数。理论上来说, /dev/random 设备更加安全，不过在日常实践中，二者并没有太大区别，因为种子是随机且不可预测的,在取得新的随机数据时该设备就会补种，反而是 /dev/random 设备的阻塞可能导致拒绝服务攻击。<br>
    > 所以推荐使用 /dev/urandom 来获得随机数，为了在程序中使用它，你只需要直接从设备文件中读取。下面的代码片段演示设备的使用方法。
    ```C
    #define LEN 16 // 128 bits
    unsigned char *key = (unsigned char *) malloc(sizeof(unsigned char)*LEN);
    FILE* random = fopen("/dev/urandom", "r");
    fread(key, sizeof(unsigned char)*LEN, 1, random);
    fclose(random);
    ```