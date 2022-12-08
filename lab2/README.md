# 实验作业一
```
1900017702 ZY
```
要求见pdf文档
## 公钥加密与 PKI 实验
https://www.lanqiao.cn/courses/243
### 实验1:成为数字证书认证机构（CA）
1. 配置文件
    ```bash
    mkdir openssl
    cd openssl

    sudo cp /usr/lib/ssl/openssl.cnf .
    mkdir demoCA
    cd demoCA
    mkdir certs crl newcerts
    touch index.txt
    echo '1000' > serial
    cd ..
    ```
2. 自签名根证书
    ```bash
    openssl req -new -x509 -keyout ca.key -out ca.crt -config openssl.cnf
    ```
### 实验2:为PKILabServer.com生成证书
1. 生成公开/私有密钥对
    ```bash
    openssl genrsa -des3 -out server.key 1024
    ```
2. 生成证书签名请求
    ```bash
    openssl req -new -key server.key -out server.csr -config openssl.cnf
    ```
3. 生成证书
    ```bash
    openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key -config openssl.cnf
    ```
    > 如果 OpenSSL 拒绝生成证书，那很可能是因为你请求中的名字与 CA 所持有的不匹配。匹配规则在配置文件中指定([policy match]处)，你可以更改名字也可以更改规则。都做到这了，就改规则吧。
### 实验3:在网站中使用 PKI
1. 添加域名映射
    ```bash
    sudo vi /etc/hosts
    ```
    最后加上一行
    ```txt
    127.0.0.1 PKILabServer.com
    ```
    映射到本地IP
2. 运行web服务器
    ```bash
    # Combine the secret key and certificate into one file
    cp server.key server.pem
    cat server.crt >> server.pem
    # Launch the web server using server.pem 密码输入之前设置的 pkilab
    openssl s_server -cert server.pem -www
    ```
3. 使用浏览器通过域名访问服务器
    ```txt
    浏览器一般内置了知名CA的证书
    PKILabServer.com的证书是被我们自己的CA签名，浏览器不认识我们的CA

    点击右边的三横线按钮->首选项->高级->证书->查看证书
        （也可以直接在地址栏输入 about:preferances#advanced 进入高级界面）
    你将看到一列证书列表，在这里我们导入我们的证书。
    导入 ca.crt 并且选择 “Trust this CA to identify web sites” 。
    ```
    1. 修改 server.pem 的一个字节并且重启服务器，访问 https://PKILabServer.com:4433 ，你观察到了些什么？确保之后恢复 server.pem.服务器可能无法重启，那样的话，换一个字节做修改。
        > Master-Key变化
    2. 既然 PKILabServer.com 指向 localhost，如果我们使用 https://localhost:4433 替代域名访问，就会连接到同一个服务器。请尝试这么做并解释你的观察。
        > 不能访问。证书是针对PKILabServer.com这个域名的