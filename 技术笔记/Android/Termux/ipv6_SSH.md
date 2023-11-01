# ipv6 SSH 连接

## 初始化

**授权读写手机储存**

```bash
termux-setup-storage
```

**换源**

参考 https://mirrors.tuna.tsinghua.edu.cn/help/termux/

**安装基础软件**

```bash
pkg update && pkg upgrade
pkg install tsu vim git openssh termux-auth iproute2 -y
```

- tsu：Termux版的su(sudo)
- vim：文本编辑器
- git：版本控制器
- openssh：用于ssh连接
- termux-auth：Termux的一个认证模块，用于在Android设备上提供安全的身份验证机制
- -y：自动确认安装以上软件

**设置用户**

获取用户名，比如 `u0_a258`

```bash
whoami
```

设置密码

```bash
passwd
```

## 获取 ipv6 地址

查看手机状态信息，然后 ping 一下试试能不能通

## 开启 ssh

termux 输入

```bash
sshd -p 9000
```

电脑上输入

```bash
ssh <用户名>@<ipv6 地址> -p 9000
```


## 参考资料

- Termux-Ubuntu22.0.4项目部署（手机服务器实操！！）, https://blog.csdn.net/m0_56349886/article/details/129758123
- Termux 公网ipv6 域名 ssh访问, https://blog.csdn.net/YiBYiH/article/details/127697310