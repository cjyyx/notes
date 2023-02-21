# %%
from typing import List

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# %%
# GIF文件名称
gif_name = "1_1"

# 约化普朗克常数
hbar: float = 1
# 粒子质量
m: float = 1

# 区域[-L,L]
L: float = 30

# 区域网格数
N: int = 100

# 运行的总时间
Time: float = 4
# delta_t
dt: float = 1e-4

dx: float = L / N
x_Line = np.linspace(-L, L, num=N + 1)

# Psi[n,i]的数据结构: list[np.array(N+1)]
array_Psi: List = []

# 势能函数
V = np.zeros(N + 1)

# %%
# 初值条件

# 生成一个等差数列
x_temp = np.linspace(-L, L, num=N + 1)

# 左移波函数的中心
x_temp = x_temp + L/2
# 避免分母为零的错误，将分母中接近零的数替换为一个较小的数（例如1e-6）
x_temp[x_temp == 0] = 1e-6

Psi_temp = (np.sin(x_temp) / x_temp) * np.exp((np.pi/2)*1j * x_temp)

# 归一化
norm = np.sqrt(dx * np.sum(np.abs(Psi_temp)**2))
Psi_temp /= norm

array_Psi.append(Psi_temp)

# %%


def Psi(n: int, i: int) -> float:
    """ 
    从 array_Psi 中读取[n,j]处的值
     """
    return array_Psi[n][i]


def next_step():
    """ 
    计算一个时间步
     """

    new_Psi = np.zeros(N + 1, dtype=np.complex128)
    n = len(array_Psi) - 1

    # 边界条件
    new_Psi[0] = 0
    new_Psi[N] = 0

    for i in range(1, N):
        Temp1 = (-hbar**2 / (2 * m)) * ((Psi(n, i + 1) - 2 *
                                         Psi(n, i) + Psi(n, i - 1)) / (dx**2)) + V[i] * Psi(n, i)
        new_Psi[i] = (Temp1 * dt) / (1j * hbar) + Psi(n, i)

    array_Psi.append(new_Psi)


# %%

for i in tqdm(range(int(Time / dt))):
    next_step()

step_num = len(array_Psi)
print("共{}个时间步".format(step_num))

# %%

gif_time = 5
gif_frame_count = 100

choices = np.linspace(0, step_num, gif_frame_count).astype("int").tolist()

vec_y = np.linspace(0, 1, N + 1)
fig = plt.figure()
ims = []
for choice in choices:
    if (choice > step_num - 1):
        choice = choice - 1

    prob_density = np.abs(array_Psi[choice])**2

    im = plt.plot(x_Line, prob_density, color="blue")
    plt.xlabel("x")
    plt.ylabel("prob_density")
    plt.title("*****")
    ims.append(im)

print("正在生成{}.gif……".format(gif_name))

ani = animation.ArtistAnimation(fig,
                                ims,
                                interval=1000 * (gif_time / gif_frame_count),
                                repeat_delay=1000)
ani.save("{}.gif".format(gif_name), writer='pillow')
