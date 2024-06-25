from zhipuai import ZhipuAI

from myKey import api_key

message = r"""
\begin{array}{c}
\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\sin \left(4\left(t+\frac{\pi}{16}\right)\right)\right]=\mathrm{e}^{\frac{\pi}{16} s} \mathscr{L}[\sin (4 t)]=\mathrm{e}^{\frac{\pi}{16} s} \frac{4}{s^{2}+16} \\
\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\frac{\sqrt{2}}{2}(\sin 4 t+\cos 4 t)\right]=\frac{\sqrt{2}}{2}\left(\frac{4}{s^{2}+16}+\frac{s}{s^{2}+16}\right)
\end{array}

\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right] 可以化为两个不相等的式子，请问出了什么问题？哪个式子是正确的？
"""


client = ZhipuAI(api_key=api_key)  # 填写您自己的APIKey
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    # messages=[
    #     {"role": "user", "content": "作为一名营销专家，请为我的产品创作一个吸引人的slogan"},
    #     {"role": "assistant", "content": "当然，为了创作一个吸引人的slogan，请告诉我一些关于您产品的信息"},
    #     {"role": "user", "content": "智谱AI开放平台"},
    #     {"role": "assistant", "content": "智启未来，谱绘无限一智谱AI，让创新触手可及!"},
    #     {"role": "user", "content": "创造一个更精准、吸引人的slogan"}
    # ],
    messages=[
        {
            "role": "user",
            "content": message,
        },
    ],
)
print(response.choices[0].message.content)
