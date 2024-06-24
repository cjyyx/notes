

## 使用pandoc把markdown编译为pdf

先安装pandoc和XeLaTeX，并且有合适的CJK字体。

> https://pandoc.org/installing.html
> LaTeX的下载和使用（on Vscode）, https://zhuanlan.zhihu.com/p/120815558

然后，使用以下命令
```bash
pandoc input.md -o output.pdf --pdf-engine=xelatex -V CJKmainfont="SimSun"
```

其中，`input.md`是markdown文件，`output.pdf`是生成的pdf文件，`--pdf-engine=xelatex`指定使用XeLaTeX引擎，`-V CJKmainfont="SimSun"`指定使用宋体作为中文主字体。

如果想要更美观的排版效果，可以使用一些pandoc的模板，或者自己编写一个。

or


```bash
pandoc -f markdown+tex_math_single_backslash -o test1.pdf --pdf-engine=pdflatex
```


https://zhuanlan.zhihu.com/p/444440478

## 输出网页

```bash
pandoc -f markdown -t html -o output.html input.md

or

pandoc test1.md -f markdown -t html -s -o test1.html
```

## 转docx

```bash
chcp 65001
pandoc "报告.md" -s -o test.docx -t docx --reference-doc "D:\\BackupNetdisk\\School\\智能控制技术及应用\\大作业\\MyProject\\custom-reference.docx"
pandoc "报告.md" -s -o test.docx -t docx --reference-doc "custom-reference.docx"
```

