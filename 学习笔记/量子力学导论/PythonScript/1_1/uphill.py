# %%
from typing import List

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

# %%
# GIF文件名称
gif_name = "uphill"

# 约化普朗克常数
hbar: float = 1.
# 粒子质量
m: float = 10000

# 区域[-L,L]
L: float = 4e-1

# 区域网格数
N: int = 1000

# 运行的总时间
Time: float = 15
# delta_t
dt: float = 5e-4

dx: float = L / N
x_Line = np.linspace(-L, L, num=N + 1)

# Psi[n,i]的数据结构: list[np.array(N+1)]
array_Psi: List = []

# 势能函数
V = np.zeros(N + 1)

for i in range(int(N/2),int(N)):
    V[i]=0.03*(i-int(N/2))


# 粒子参数
sigma: float = 2e-2
x0: float = -L/3
p0: float = 150

# 隐式方法用的矩阵
matrix_S = np.zeros([N+1, N+1])


# %%
# 初值条件，高斯波函数


def project_init():
    """ 
    清空array_Psi;
    设定初值条件;
    生成隐式方法需要的矩阵，默认边界条件为驻点;
     """
    global array_Psi, matrix_S

    array_Psi = []

    # 生成一个等差数列
    x = np.linspace(-L, L, num=N + 1)

    # 高斯波函数
    Psi_temp = (1/(2*np.pi*(sigma**2))**(1/4)) * \
        np.exp(-(x-x0)**2/(2*sigma)**2)*np.exp(1j * p0*x/hbar)

    # 归一化
    norm = np.sqrt(dx * np.sum(np.abs(Psi_temp)**2))
    Psi_temp /= norm

    array_Psi.append(Psi_temp)

    # 隐式方法需要的矩阵
    A = (1j * hbar)/dt - (hbar**2)/(m*(dx**2))-V
    B = (hbar**2)/(2*m*(dx**2))

    vec_temp1 = np.ones(N)

    matrix_T = (
        B*np.diagflat(vec_temp1, 1) +
        np.diagflat(A, 0) +
        B*np.diagflat(vec_temp1, -1)
    )
    matrix_T[0][0] = matrix_T[N][N] = 1
    matrix_T[0][1] = matrix_T[N][N-1] = 0

    matrix_T_inv = np.linalg.inv(matrix_T)

    vec_temp2 = np.ones(N+1)
    matrix_Temp1 = np.diagflat(vec_temp2, 0)
    matrix_Temp1[0][0] = matrix_Temp1[N][N] = 0

    matrix_S = np.dot(matrix_T_inv, matrix_Temp1)*(1j*hbar/dt)


# %%
""" 
边界条件可采用吸收边界条件、非定常边界条件、周期边界条件
 """


def Psi(n: int, i: int) -> float:
    """ 
    从 array_Psi 中读取[n,i]处的值；
     """
    if (n < 0):
        print("warning: mistake n!!!")
        return 0

    if (i >= 0 and i <= N):
        return array_Psi[n][i]
    # elif (i == -1):
    #     # 边界条件
    #     return 2*array_Psi[n][0]-array_Psi[n][1]
    #     # return array_Psi[n][0]
    # elif (i == N+1):
    #     # 边界条件
    #     return 2*array_Psi[n][N]-array_Psi[n][N-1]
    #     # return array_Psi[n][N]
    else:
        print("warning: mistake i!!!")
        return 0


def apply_absorbing_boundary_conditions(psi, dx, dt, absorbing_width):
    # 这个函数chatgpt给的，不知道对不对
    """
    在一维波函数 psi 上应用外推网格法吸收边界条件。
    psi: 一维波函数数组，大小为 (nx,)
    dx: 空间步长
    dt: 时间步长
    absorbing_width: 吸收层宽度，以空间步长为单位

    返回更新后的波函数 psi_new。
    """
    # 计算波函数大小
    nx = psi.shape[0]

    # 计算梯度和二阶导数
    d_psi_dx = np.gradient(psi, dx)
    d2_psi_dx2 = np.gradient(d_psi_dx, dx)

    # 计算吸收层内的外推距离和衰减系数
    x_absorb = np.linspace(-absorbing_width*dx, 0, absorbing_width)
    k = np.log(2)/((absorbing_width*dx)**2)

    # 应用吸收边界条件
    psi_new = psi.copy()
    for i in range(absorbing_width):
        # 对吸收层左侧的波函数进行外推和衰减
        psi_new[i] = psi[i] - \
            np.exp(-k*(x_absorb[i]-dx)*dt)*(d_psi_dx[i]+d2_psi_dx2[i]*dx)*dx
        psi_new[i] *= np.exp(-k*(x_absorb[i]-dx)*dt)
        # 对吸收层右侧的波函数进行外推和衰减
        psi_new[-i-1] = psi[-i-1] - \
            np.exp(-k*(x_absorb[i]-dx)*dt) * \
            (-d_psi_dx[-i-1]+d2_psi_dx2[-i-1]*dx)*dx
        psi_new[-i-1] *= np.exp(-k*(x_absorb[i]-dx)*dt)

    return psi_new


def next_step():
    """ 
    计算一个时间步
     """

    # 显式方法

    # new_Psi = np.zeros(N + 1, dtype=np.complex128)
    # n = len(array_Psi) - 1

    # for i in range(1, N):
    #     Temp1 = (-hbar**2 / (2 * m)) * ((Psi(n, i + 1) - 2 *
    #                                      Psi(n, i) + Psi(n, i - 1)) / (dx**2)) + V[i] * Psi(n, i)
    #     new_Psi[i] = (Temp1 * dt) / (1j * hbar) + Psi(n, i)

    # # new_Psi = apply_absorbing_boundary_conditions(new_Psi, dx, dt, 20)

    # 隐式方法

    new_Psi = np.dot(matrix_S, array_Psi[-1])
    
    # 周期边界条件
    new_Psi[0]=new_Psi[N-1]
    new_Psi[N]=new_Psi[1]

    array_Psi.append(new_Psi)


# %%

def Wave_function_rendering(aPsi):
    wave_norm = np.abs(aPsi)
    real_part = np.real(aPsi)
    imag_part = np.imag(aPsi)

    plt.xlabel("x")
    plt.legend(["Wave function norm", "real_part", "imag_part","V"])
    # plt.ylabel("prob_density")
    # plt.title("*****")

    frame = []

    im1 = plt.plot(x_Line, wave_norm, color="orange",
                   label="Wave function norm")
    im2 = plt.plot(x_Line, real_part, color="blue", label="real_part")
    im3 = plt.plot(x_Line, imag_part, color="red", label="imag_part")
    im4 = plt.plot(x_Line, V, color="black", label="V")

    frame = im1+im2+im3+im4

    return frame


def new_Wave_function_rendering():
    fig = plt.figure(figsize=(10, 4))
    Wave_function_rendering(array_Psi[-1])


def Gif_making(gif_time=2, gif_frame_count=20, gif_name="test"):
    """ 
    gif_time:GIF时长;
    gif_frame_count:GIF图片数目;
    gif_name:GIF图片名称，不用包括".gif";
     """
    step_num = len(array_Psi)

    choices = np.linspace(0, step_num, gif_frame_count).astype("int").tolist()

    fig = plt.figure(figsize=(10, 4))
    # ax = fig.add_subplot(111)
    # ax.set
    artists = []
    for choice in choices:
        if (choice > step_num - 1):
            choice = choice - 1
        frame = Wave_function_rendering(array_Psi[choice])
        artists.append(frame)

    print("正在生成{}.gif……".format(gif_name))

    ani = animation.ArtistAnimation(fig,
                                    artists,
                                    interval=1000 *
                                    (gif_time / gif_frame_count),
                                    repeat_delay=1000)
    ani.save("{}.gif".format(gif_name), writer='pillow')

# %%


def next_run(step_num):
    for i in tqdm(range(step_num)):
        next_step()


def new_run(step_num):
    project_init()
    next_run(step_num)


# %%
if __name__ == "__main__":

    new_run(int(Time / dt))

    step_num = len(array_Psi)
    print("共{}个时间步".format(step_num))

    Gif_making(5, 50, gif_name)
