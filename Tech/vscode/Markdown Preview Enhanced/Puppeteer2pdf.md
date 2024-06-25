#! https://zhuanlan.zhihu.com/p/615810007
# VS Code 中 Markdown Preview Enhanced 插件利用 Chrome (Puppeteer) 导出 pdf 文件使用说明与问题解决

## 准备

预先安装好 Chrome 浏览器。

## 使用方法

右键选择 Chrome (Puppeteer)。

![使用方法](PasteImage/2023-10-12-12-21-35.png)

## 设置 Puppeteer

通过 `front-matter`

即在 markdown **文档开头**加上 yaml 格式的配置代码

```yaml
---
puppeteer:
    format: "A4"
    scale: 1.0
    margin:
        top: 2cm
        right: 3cm
        bottom: 2cm
        left: 3cm
---
```

这里 `format` 表示纸张格式，`scale` 表示缩放，`margin` 表示页边距。

更多设置选项说明可以参考官方文档(https://github.com/puppeteer/puppeteer/blob/v1.8.0/docs/api.md#pagepdfoptions)

## 公式渲染问题

有时会发现一些公式渲染没有显示，这是因为 Puppeteer 导出 pdf 的原理是网页快照。渲染还没有完成，网页已被导出。

解决方案是延迟导出时间，即

```yaml
---
puppeteer:
    timeout: 3000
---
```

表明等待 3000 毫秒（此时认为渲染已完成）后导出

另一种解决方法是修改插件设置，这与上面的方法效果一样

![](PasteImage/2023-10-12-12-12-40.png)

## 代码背景显示问题

有时会发现代码背景没有显示，如图

![](PasteImage/2023-10-12-12-17-10.png)

而预期效果应为

![](PasteImage/2023-10-12-12-15-58.png)

解决方法是修改插件设置，设置打印背景

![](PasteImage/2023-10-12-12-18-11.png)

## 保存时自动导出

```yaml
---
export_on_save:
    puppeteer: true # 保存文件时导出 PDF
    puppeteer: ["pdf", "png"] #保存文件时导出 PDF 和 PNG
    puppeteer: ["png"] # 保存文件时导出 PNG
---
```

## 图片调整大小

导出的pdf文档中，图片可能过大，解决方法是添加自定义 css。

即在 `front-matter` 后加上

```html
<style>
img{
    width: 60%;
    padding-left: 20%;
}
</style>
```

这段代码的意思是，把所有图片的宽度设置为段落宽度的60%，并向右移20%（即让图片居中）。

也可导入外部 css 文件。

如在文件 `style.css` 中有

```css
img{
    width: 60%;
    padding-left: 20%;
}
```

在markdown文件的`front-matter`后加上

```
@import "style.css"
```

此时效果与上相同。

当然有更好玩的方法，使 `style.css` 为

```css
img[src*="#w100"] {
width: 100%;
}

img[src*="#w80"] {
width: 80%;
}

img[src*="#w60"] {
width: 60%;
}

img[src*="#w50"] {
width: 50%;
}

img[src*="#w30"] {
width: 30%;
}

img[src*="#w20"] {
width: 20%;
}

img[src*="#w10"] {
width: 10%;
}
```

此时 markdown 写法如下，就可以调整图片大小

```markdown
![img.png](./<path>/img.png#w60)
```


## 页码显示

可以在导出的 pdf 文件上显示页码

```yaml
---
puppeteer:
    timeout: 3000
    displayHeaderFooter: true
    headerTemplate: '<span class="pageNumber"></span>'
    footerTemplate: '
        <div style="font-size: 10px; margin-left: 20px;">
        <span class="pageNumber"></span> / 
        <span class="totalPages"></span>
        </div>
        '
---
```

## 简单排版

添加大段空行

```markdown
<p style="margin-bottom: 400px;"></p>
```

换页，只有在导出为PDF时才会起作用

```markdown
<div STYLE="page-break-after: always;"></div>
```

## 总结

比较合适的 `front-matter` 为

```yaml
---
puppeteer:
    scale: 0.8
    margin:
        top: 2cm
        right: 3cm
        bottom: 2cm
        left: 3cm
    timeout: 3000
    displayHeaderFooter: true
    headerTemplate: '<span class="pageNumber"></span>'
    footerTemplate: '
        <div style="font-size: 10px; margin-left: 20px;">
        <span class="pageNumber"></span> / 
        <span class="totalPages"></span>
        </div>
        '
---
```