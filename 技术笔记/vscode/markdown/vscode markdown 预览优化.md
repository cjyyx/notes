#! https://zhuanlan.zhihu.com/p/700473509
# vscode markdown 预览优化：数学公式

最新版的 vscode 对 markdown 提供了较多支持，其在预览方面的体验甚至可以与 Markdown Preview Enhanced 插件相比。当然还有一些不足，这里提供了一些优化方法。

参考：https://code.visualstudio.com/docs/languages/markdown

## 常规设置

![](PasteImage/2024-05-29-12-11-13.png)

打开 vscode 的 `markdown.preview` 设置，可以看到一些设置选项，如字体、字号、行高等。

## 使用 CSS

markdown 预览本质上是一个网页，因此可以使用 CSS 优化。

![](PasteImage/2024-05-29-12-14-28.png)

打开 `markdown.styles` 设置，可以看到添加 CSS 文件路径。支持两种文件路径：

1. 相对路径。相对路径是相对于资源管理器中打开的文件夹进行解释的。如果没有打开的文件夹，则相对于Markdown文件的位置解释它们。
2. CSS 文件的 https URL 。

## 数学公式预览优化

打开 vscode 自带的开发者工具，可以看到所有数学公式都有 `class="katex"` 。

![](PasteImage/2024-05-29-12-17-56.png)

目前存在的问题是数学公式太小，于是可以在工作区本地创建 CSS 文件，内容为：

```css
.katex {
    font-size: 1.25em !important;
}
```

然后添加到 `markdown.styles` 。
