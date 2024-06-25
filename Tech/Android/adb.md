要使用 Android 调试桥（ADB），请按照以下步骤操作：

1. 下载并安装 Android SDK：首先，您需要下载并安装 Android SDK（软件开发工具包）。您可以从 Android 开发者网站（https://developer.android.com/studio/releases/platform-tools）下载适用于您的操作系统的最新版本。

2. 在 Android 设备上启用 USB 调试模式

3. 连接设备到计算机：使用 USB 数据线将 Android 设备连接到计算机。确保设备已正确连接，并且计算机可以识别设备。

4. 打开命令行终端：在计算机上打开命令行终端或命令提示符窗口。

5. 运行 ADB 命令：在打开的命令行终端中，输入以下命令来执行 ADB 命令：
```
adb <command>
```
其中 `<command>` 是您要执行的 ADB 命令。

ADB 命令的一些常见用法包括：
- `adb devices`：列出已连接的设备。
- `adb shell`：进入设备的 shell 环境。
- `adb install <path_to_apk>`：安装一个应用程序。
- `adb uninstall <package_name>`：卸载一个应用程序。
- `adb push <local_path> <device_path>`：将文件从计算机推送到设备。
- `adb pull <device_path> <local_path>`：从设备上拉取文件到计算机。

请注意，具体的 ADB 命令取决于您要执行的操作。您可以在命令行终端中输入 `adb help` 或查阅 Android 开发者文档（https://developer.android.com/studio/command-line/adb）获取更多关于 ADB 命令的信息和示例用法。

在设备的 shell 环境中，您可以使用以下命令来查看设备的信息：

1. `adb shell`：这会将您连接到设备的 shell 环境。

2. `uname -a`：此命令将显示设备的内核版本和其他基本信息。

3. `cat /proc/cpuinfo`：这个命令将显示有关设备 CPU 的信息，如制造商、型号、频率等。

4. `getprop`：此命令将显示设备的各种属性信息，如设备型号、Android 版本、屏幕分辨率等。您可以使用 `getprop` 命令的不同选项来筛选和显示特定属性。

5. `dumpsys`：这个命令用于获取有关设备各个系统服务的详细信息。例如，您可以使用 `dumpsys battery` 查看电池信息，`dumpsys wifi` 查看 Wi-Fi 信息等。

6. `pm list packages`：此命令将列出设备上安装的所有应用程序包名。

7. `df`：这个命令将显示设备上存储空间的使用情况，包括总空间、已用空间和可用空间等信息。

这些是一些常用的命令，可以提供设备的基本信息。您可以根据自己的需求进一步探索其他命令和选项。请注意，具体命令的输出可能因设备型号、Android 版本或设备状态而有所不同。