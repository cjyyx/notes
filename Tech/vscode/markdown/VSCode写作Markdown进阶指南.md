<!-- 在 VSCode 中写 Markdown 进阶指南

 -->

最新版的 VSCode 对 Markdown 提供了较多支持，其在预览方面的体验甚至可以与 Markdown Preview Enhanced 插件相比。当然还有一些不足，这里提供了一些优化方法。

VSCode 官方使用说明：<https://code.visualstudio.com/docs/languages/markdown>

# 预览常规设置

![](assets/2024-05-29-12-11-13.png)

打开 vscode 的 `markdown.preview` 设置，可以看到一些设置选项，如字体、字号、行高等。

# 使用 CSS

markdown 预览本质上是一个网页，因此可以使用 CSS 优化。

![](assets/2024-05-29-12-14-28.png)

打开 `markdown.styles` 设置，可以看到添加 CSS 文件路径。支持两种文件路径：

1. 相对路径。相对路径是相对于资源管理器中打开的文件夹进行解释的。如果没有打开的文件夹，则相对于 Markdown 文件的位置解释它们。
2. CSS 文件的 https URL 。

# 数学公式预览优化

打开 vscode 自带的开发者工具，可以看到所有数学公式都有 `class="katex"` 。

![](assets/2024-05-29-12-17-56.png)

目前存在的问题是数学公式太小，于是可以在工作区本地创建 CSS 文件，内容为：

```css
.katex {
    font-size: 1.25em !important;
}
```

然后添加到 `markdown.styles` 。

我也创建了 CSS 文件的 url，可以添加 <https://blog-static.cnblogs.com/files/blogs/825243/vscode-markdown-style.css> 。

# 编辑器体验优化

在用户 `settings.json` 使用如下配置：

```json
"[markdown]": {
    "editor.minimap.enabled": false,
    "editor.glyphMargin": false,
    "editor.renderWhitespace": "all",
},
```

# 图片粘贴

使用 `Paste Image` 插件和 VSCode 自带的 copyFiles 功能。

`Paste Image` 插件设置如下，表明 `Ctrl+Shift+V` 可以把剪切板上的图片保存到工作区的 `assets` 文件中，并在 md 文件中插入图片路径。

![](assets/2024-06-26-23-45-41.png)

VSCode 的 `markdown.copyFiles` 设置如下

![](assets/2024-06-26-23-53-33.png)

此时 `Ctrl+V` 快捷键也可以保存剪切板上的图片到工作区的 `assets` 文件中，并在 md 文件中插入路径。区别在于：

1. VSCode 自带的 copyFiles 功能还可以粘贴图片和音频文件
2. `Paste Image` 插件保存的图片可以自动生成 `Y-MM-DD-HH-mm-ss` 的文件名，而 VSCode 的 copyFiles 功能则不行

因此建议这两种方法配合使用。

# 格式化

`markdownlint` 插件提供了格式化 markdown 代码功能，并会对不规范的 markdown 代码作出警告。使用该插件建议在用户 `settings.json` 使用如下配置

```json
"[markdown]": {
    "editor.defaultFormatter": "DavidAnson.vscode-markdownlint",
    "editor.formatOnSave": true,
},
"markdownlint.config": {
    "MD012": false,
    "MD018": false,
    "MD024": false,
    "MD025": false,
    "MD033": false,
    "MD036": false,
    "MD041": false,
    "MD045": false,
},
```

`Pangu-Markdown` 插件补充了格式化功能，如在中英字符之间插入空格。使用方法为右键点击 Pangu Format。

# 代码补全与快捷功能

`Markdown All in One` 插件可以补全 markdown 代码，包括 latex 函数代码。同时也提供了一些编辑 markdown 的快捷功能。

`Better Markdown & Latex Shortcuts` 插件提供了一些编辑 latex 公式的快捷键。

# 功能拓展

`Markdown Footnotes` 插件让 VSCode 的 markdown 预览支持脚注功能，例如：

```markdown
这是一个脚注 [^1]

[^1]: 脚注 1
```

`Markdown Image Size` 插件提供了调整图片大小的拓展语法。但是该语法应用并不普遍，因此不推荐使用。

# 导出 PDF 和 Word 文档

# 博客写作

`博客园 cnblogs 客户端` 和 `Zhihu On VSCode` 插件都提供了比较好的博客写作体验。

`Markdown Publisher For CSDN/JIANSHU/ZHIHU/JUEJIN/WECH` 插件 <https://blog.csdn.net/qq_21197033/article/details/132297182> 支持 markdown 多平台一键发布，但目前使用体验较差。
