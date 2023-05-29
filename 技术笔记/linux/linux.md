# 换源

https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/


22.04LTS 2023-1-28
```bash
sudo sed -i "s@http://.*archive.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
sudo sed -i "s@http://.*security.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
```

# vim

https://missing-semester-cn.github.io/2020/editors/

```vim FileName```
开始进入正常模式。

按`i`进入插入模式，跟正常编辑器一样使用。按`Esc`返回正常模式。

按`:`进入命令行模式。`:w`保存，`:q`退出，`:wq`保存然后退出。


# 终端设置代理

![](PasteImage/2023-01-28-13-01-24.png)

```bash
export all_proxy="socks5://192.168.0.106:7890"
```



## 权限设置

```
chmod -R +x <path>
```

## 删除

```bash
rm -rf <foldername>
```



