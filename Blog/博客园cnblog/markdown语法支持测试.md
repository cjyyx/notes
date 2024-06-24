
## latex 公式

$v, w, \nu, \omega$

$$
\iiint, \oiiint
$$

$\Set{ x | x<\frac 1 2 }$

$\displaystyle \sum_{\substack{0<i<m\\0<j<n}}$

**齐次变换矩阵** $\displaystyle {}_{B}^AT=\left.\left[\begin{array}{ccc|c}&{}_B^AR&&{}^AO_B\\\hline0&0&0&1\end{array}\right.\right]\in\mathbb{R}^{4\times4}$

$$
\langle\theta^{2}\rangle=\frac{1}{Z}\int_{0}^{2\pi}\mathrm{d}\phi\int_{0}^{\pi}\mathrm{d}\theta\sin\theta\theta^{2}\mathrm{e}^{-(EI/2k_{B}Ts)\theta^{2}}
$$

$$
\boxed{M_{\mathrm{cg}} = \underbrace{M_{\mathrm{f}}}_{\text{机身贡献}} +\underbrace{M_{\mathrm{sc},\mathrm{w}} + L_{\mathrm{w}}x_{\mathrm{a}}}_{\text{机载贡献}} + \underbrace{M_{\mathrm{sc},\mathrm{t}} - L_{\mathrm{t}}l_{\mathrm{t}}}_{\text{平地贡献}}}
$$

$$
T\mathrm{cos}\varepsilon - D - W\mathrm{sin}\gamma = \cancel{\frac{W}{g} \frac{\mathrm{d}V}{\mathrm{d}t}}
$$

$$
u_{\substack{\max\\\min}}=\sqrt{z\pm\sqrt{z^{2}-1}}
$$

$$
f(n)=
\begin{cases}
\dfrac{n}{2},&\text{if $n$ is even}\\[2ex]
3n+1,&\text{if $n$ is odd}
\end{cases}
$$

$$
\def\arraystretch{1.5}
\begin{array}{c:c:c}
a & b & c \\ \hline
d & e & f \\
\hdashline
g & h & i
\end{array}
$$


## 注释

下面内容都是是注释掉的：

<!-- 注释注释注释注释注释注释注释 -->

<!-- 注释注释注释注释注释
注释注释
注释注释 -->

<!--
注释注释注释注释

注释注释注释
-->

<!-- 
```x
注释注释
```
-->

```x
<!-- 
注释注释
-->
```

<!-- 
$$注释$$ -->

## Footnotes

Adds support for [^1] syntax to VS Code's built-in markdown preview

[^1]: xxxxx

## 代码

```test
1lL
0oO
Cc
Kk
Pp
Ss
```

```html
<script src="https://blog-static.cnblogs.com/files/guangzan/loader.min.js"></script>

<script>
    const config = {
        // 在这里添加自定义配置
        theme: {
            name: 'geek',
            avatar: 'https://pic.cnblogs.com/avatar/3281293/20230917165414.png',

        },
        github: {
            enable: true,
            color: '#ffb3cc',
            url: 'https://github.com/cjyyx',
        },
        signature: {
            enable: true,
            contents: [
                "This theme is built with <b style='color:#ff6b81'>awescnb</b>.",
                "<b>console.log(🍺);</b>",
            ],
        },
        click: {
            enable: true,
            auto: false,
            colors: ['#FF1461', '#18FF92', '#5A87FF', '#FBF38C'],
            size: 5,
            maxCount: 50,
        },
        postSignature: {
            enable: false,
            enableLicense: false,
            licenseName: '',
            licenseLink: '',
        },

    }
    $.awesCnb(config)

</script>

```


