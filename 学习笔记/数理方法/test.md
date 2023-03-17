$$
\begin{aligned}
\int_{0}^{x} \mathrm{J}_{0}(x) \cos x,dx &= \left[\mathrm{J}_0(x)\sin x\right]0^x - \int{0}^{x} \sin x\cdot(-\mathrm{J}_1(x)),dx \\
&= \mathrm{J}_0(x)\sin x + \mathrm{J}_1(x)\cos x \Big|_0^x \\
&= \mathrm{J}_0(x)\sin x + \mathrm{J}_1(x)\cos x - \mathrm{J}_1(0) \\
&= \mathrm{J}_0(x)\sin x + \mathrm{J}_1(x)\cos x - 1
\end{aligned}
$$

$\mathrm{J}_1'(x) = \mathrm{J}_0(x) - \mathrm{J}_1(x)/x$

$$
\begin{align}
\mathrm{J}1(x) &= \frac{d}{dx} \left(\mathrm{J}0(x)\right) \\
&= \frac{d}{dx} \left(\frac{1}{\pi} \int{0}^{\pi} \cos(x \sin t - t) dt\right) \\
&= \frac{1}{\pi} \int{0}^{\pi} \frac{\partial}{\partial x} \cos(x \sin t - t) dt \\
&= \frac{1}{\pi} \int_{0}^{\pi} \left(\sin t \cos(x \sin t - t)\right) dt \\
&= \frac{1}{x} \cdot \frac{1}{\pi} \int_{0}^{\pi} \frac{\partial}{\partial t} \left(\cos(x \sin t - t)\right) dt \\
&= \frac{1}{x} \cdot \frac{1}{\pi} \int_{0}^{\pi} \left(-\sin t \sin(x \sin t - t) - \cos t \cos(x \sin t - t)\right) dt \\
&= -\frac{1}{x} \mathrm{J}1(x) + \frac{1}{\pi x} \int{0}^{\pi} \cos(x \sin t - t) \cdot \left(\frac{\pi}{2} - t\right) dt \\
&= -\frac{1}{x} \mathrm{J}1(x) + \frac{1}{\pi x} \int{0}^{x \sin \pi} \cos(u - \pi/2) \cdot \frac{\arcsin(u/x)}{\sqrt{x^2 - u^2}} du \quad (\text{令 } u = x \sin t - t) \\
&= -\frac{1}{x} \mathrm{J}1(x) + \frac{1}{\pi x} \int{0}^{x} \frac{\cos(u - \pi/2)}{\sqrt{x^2 - u^2}} du \\
&= -\frac{1}{x} \mathrm{J}_1(x) + \frac{1}{\pi x} \left[\mathrm{J}_0(u) \right]_0^{x} \\
&= \mathrm{J}_0(x) - \frac{1}{x} \mathrm{J}_1(x)
\end{align}
$$