# Z变换

## 定义

$$
X(z) \triangleq \sum_{n=-\infty}^{+\infty} x[n] z^{-n}
$$

$$
x[n]=\frac{1}{2 \pi \mathrm{j}} \oint X(z) z^{n-1} \mathrm{~d} z
$$

$$
x[n] \stackrel{Z}{\longleftrightarrow} X(z)
$$

$$
\left.X(z)\right|_{z=\mathrm{e}^{\mathrm{j} \omega}}=X\left(\mathrm{e}^{\mathrm{j} \omega}\right)=\mathcal{F}\{x[n]\}
$$

## 性质

![](PasteImage/2023-12-23-18-58-39.png)

![](PasteImage/2023-12-23-18-59-07.png)