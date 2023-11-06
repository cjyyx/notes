# ipv6 公网服务器

## Termux 配置

### 初始化

**授权读写手机储存**

```bash
termux-setup-storage
```

**换源**

参考 https://mirrors.tuna.tsinghua.edu.cn/help/termux/

**安装基础软件**

```bash
pkg update && pkg upgrade
pkg install tsu vim git python3 openssh pure-ftpd termux-auth -y
```

- tsu：Termux版的su(sudo)
- vim：文本编辑器
- git：版本控制器
- openssh：用于ssh连接
- pure-ftpd：SFTP 文件服务器
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

### 获取 ipv6 地址

首先确保连入的 WiFi 支持 ipv6。

**方法1**

查看手机状态信息，然后 ping 一下试试能不能通

**方法2**

运行以下指令，获取 ipv6 地址

```bash
curl https://ipv6.ddnspod.com
```

> 注意：由于安卓权限问题，不能用 `ip a`、`ifconfig` 等命令直接获取 ipv6 地址。

### 开启 ssh

termux 输入

```bash
sshd -p 9000
```

电脑上输入

```bash
ssh <用户名>@<ipv6 地址> -p 9000
```

## sftp 服务器

运行

```bash
pure-ftpd
```
TODO


### 启动后自动完成配置

首先编辑 .bashrc 文件 `nano ~/.bashrc`

在文件最后添加以下代码

```bash
user_name=$(whoami)  
echo "User name: $user_name"

ip_address=$(curl https://ipv6.ddnspod.com)  
echo "IP address: $ip_address"

sshd -p 9000

echo ""
echo "Please run the following command to establish an ssh connection with Termux:"
echo "ssh $user_name@$ip_address -p 9000"
```


<!-- 
## 安装 Ubuntu

这里建议打开手机代理

```bash
pkg install proot-distro  # 安装 proot-districto
proot-distro list  # 查看可安装的系统
proot-distro install ubuntu  # 安装 Ubuntu
proot-distro login ubuntu # 登录 Ubuntu
```

查看 Ubuntu 版本信息 `cat /etc/issue`

**设置用户**

获取用户名，一般为 `root`

```bash
whoami
```

设置密码

```bash
passwd
```

**ssh**

```bash
apt install openssh-server
```

## 安装 Debian

这里建议打开手机代理

```bash
pkg install proot-distro
proot-distro list
proot-distro install debian
proot-distro login debian
```

查看 debian 版本信息 `cat /etc/issue`

**设置用户**

获取用户名，一般为 `root`

```bash
whoami
```

设置密码

```bash
passwd
```

**安装 ssh**

```bash
apt install openssh-server
```

启动 

```bash
service ssh start
/usr/sbin/sshd -p 8025
```

 -->


## qemu 运行虚拟机

在 Termux 中使用 proot-distro 安装的 linux 系统，是以 chroot（更改根目录）的形式运行的，而不是作为一个独立的虚拟机或容器，因此功能非常受限。


## 参考资料

- Termux-Ubuntu22.0.4项目部署（手机服务器实操！！）, https://blog.csdn.net/m0_56349886/article/details/129758123
- Termux 公网ipv6 域名 ssh访问, https://blog.csdn.net/YiBYiH/article/details/127697310
- 基于ipv6实现几乎零成本的内网穿透方案, https://zhuanlan.zhihu.com/p/638004070
- 在Termux（非root的安卓Linux模拟器）中安装和使用ftp服务器, https://www.cnblogs.com/-fresh/p/10328331.html