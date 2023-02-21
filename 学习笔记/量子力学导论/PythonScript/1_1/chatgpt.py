import numpy as np
from scipy.constants import hbar
from tqdm import tqdm

# 定义常数
L = 1e-8  # 区域长度（单位：米）
N = 1000  # 离散化格点数
dx = L / N  # 格点间距（单位：米）
mass = 9.10938356e-31  # 电子质量（单位：千克）
E = 10 * 1.60217662e-19  # 能量（单位：焦耳）
h = 2 * np.pi * hbar  # 普朗克常数（单位：焦秒）

# 初始化波函数
psi = np.zeros(N, dtype=np.complex128)
for i in range(N):
    x = i * dx
    k = np.sqrt(2 * mass * E) / h
    psi[i] = np.exp(1j * k * x)

# 归一化波函数
norm = np.sqrt(dx * np.sum(np.abs(psi)**2))
psi /= norm

# 计算演化矩阵
dt = 1e-18  # 时间步长（单位：秒）
alpha = 1j * hbar / (2 * mass * dx**2)
beta = -alpha / 2
A = np.diag(beta * np.ones(N - 1), 1) + np.diag(
    beta * np.ones(N - 1), -1) + np.diag((1 + alpha) * np.ones(N))
B = np.diag(-beta * np.ones(N - 1), 1) + np.diag(
    -beta * np.ones(N - 1), -1) + np.diag((1 - alpha) * np.ones(N))

# 计算演化
T = 1e-15  # 总时间（单位：秒）
t = 0  # 当前时间（单位：秒）
for iii in tqdm(range(100)):
    psi = np.linalg.solve(A, np.dot(B, psi))
    t += dt

# 计算概率密度
prob_density = np.abs(psi)**2

# 绘制概率密度图
import matplotlib.pyplot as plt

plt.plot(np.arange(0, L, dx), prob_density)
plt.xlabel("Position (m)")
plt.ylabel("Probability Density")
plt.show()
