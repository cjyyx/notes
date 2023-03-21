#! https://zhuanlan.zhihu.com/p/615810007
# Markdown Preview Enhanced插件利用Chrome (Puppeteer)导出pdf文件

## 准备

预先安装好 Chrome 浏览器。

## 使用方法

右键点击预览，选择 Chrome (Puppeteer)。

![使用方法](PasteImage/2023-03-21-16-08-03.png)

## 设置 Puppeteer

通过`front-matter`

即在markdown文档开头加上

```yaml
---
puppeteer:
    format: "A4"
    margin:
        top: 2cm
        right: 3cm
        bottom: 2cm
        left: 3cm
---
```

这里`format`表示纸张格式，`margin`表示页边距。

更多设置可以参考官方文档(https://github.com/puppeteer/puppeteer/blob/v1.8.0/docs/api.md#pagepdfoptions)

## 渲染问题

有时会方向一些渲染没有显示（如公式），这是因为Puppeteer导出 pdf 的原理是网页快照。渲染还没有完成，网页已被导出。

解决方案是延迟导出时间，即

```yaml
---
puppeteer:
  timeout: 3000 # 等待 3000 毫秒（此时认为渲染已完成）后导出
---
```


## 保存时自动导出

```yaml
---
export_on_save:
    puppeteer: true # 保存文件时导出 PDF
    puppeteer: ["pdf", "png"] #保存文件时导出 PDF 和 PNG
    puppeteer: ["png"] # 保存文件时导出 PNG
---
```

## 图片显示

导出的pdf文档中，图片可能过大，解决方法是添加自定义 css。

即在`front-matter`后加上

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

如在文件`style.css`中有

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