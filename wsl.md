# wsl

https://learn.microsoft.com/zh-cn/windows/wsl/

重置
```bash
wsl --unregister Ubuntu
```

# wsl安兔兔跑分
```bash
wget https://file.antutu.com/soft/com.antutu.benchmark_amd64.deb
sudo apt install ./com.antutu.benchmark_amd64.deb
```
安装字体
```bash
sudo ln -s /mnt/c/Windows/Fonts /usr/share/fonts/font
fc-cache -fv
```
运行
```bash
/opt/apps/com.antutu.benchmark/files/bin/benchmark
```

# KDE桌面

https://zhuanlan.zhihu.com/p/338666316

```bash
sudo apt-get install kubuntu-desktop
```

## 软件
https://apps.kde.org/zh-cn/

gnome-software软件管理

plasma-discover软件管理

dolphin文件浏览器
konsole终端
kate
okular
systemsettings系统设置

## 缩放

https://zhuanlan.zhihu.com/p/424930447

https://blog.csdn.net/feiying0canglang/article/details/124695749

`Xft.dpi: 160`
查询`xrdb -query -all | grep Xft`
开机运行`/usr/bin/xrdb -merge ~/.Xresource`

**WSL中并不支持通过rc.local 来实现开机启动**

<!-- ```bash
sudo cp /lib/systemd/system/rc-local.service /etc/systemd/system
sudo vim /etc/systemd/system/rc-local.service
sudo vim /etc/rc.local
sudo chmod +x /etc/rc.local
```

```
[Install]   
WantedBy=multi-user.target   
Alias=rc-local.service
```

```bash
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
/usr/bin/xrdb -merge ~/.Xresource
exit 0
```

```bash
sudo mkdir /etc/rc.d
sudo vim /etc/rc.d/rc.local
sudo chmod +x /etc/rc.d/rc.local
``` -->

https://zhuanlan.zhihu.com/p/569883693

<!-- 在ubuntu终端中运行
```bash
echo -e "[boot]\nsystemd=true" | sudo tee -a /etc/wsl.conf
``` -->
