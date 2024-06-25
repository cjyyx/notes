## 图形桌面

aidlux打开 cloud_ip

浏览器访问 `http://<ip地址>:8000`

## ssh/scp

用户名 root
密码 aidlux
端口 9022

**ipv6**

修改 `sudo nano /etc/ssh/sshd_config`

```
Port 9022
AddressFamily any
PermitRootLogin yes
PasswordAuthentication yes
ListenAddress 0.0.0.0
ListenAddress ::
```

重启

```bash
# 重新启动ssh
/etc/init.d/ssh restart
# 查看ssh运行状态
/etc/init.d/ssh status
```
