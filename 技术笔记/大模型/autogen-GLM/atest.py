# %%
import json
from types import SimpleNamespace

import autogen
import requests
from zhipuai import ZhipuAI

from myKey import api_key

df = open("test.txt", "w", encoding="utf-8")

# %%


class GLM4Client:
    def __init__(self, config, **kwargs):
        # print(f"ErnieModelClient config: {config}")

        self.device = config.get("device", "cpu")
        self.model_name = config["model"]

        gen_config_params = config.get("params", {})
        self.max_length = gen_config_params.get("max_length", 1024)

        self.client = ZhipuAI(api_key=api_key)

    def create(self, params):
        """生成文本响应"""
        if params.get("stream", False) and "messages" in params:
            # 不支持流式处理
            raise NotImplementedError("Local models do not support streaming.")
        else:
            # print(f"--- ErnieModelClient create ---")
            # print(params)

            num_of_responses = params.get("n", 1)
            response = SimpleNamespace()

            response.choices = []
            response.model = self.model_name

            for _ in range(num_of_responses):
                message = params["messages"]

                choice = SimpleNamespace()
                choice.message = SimpleNamespace()
                choice.message.function_call = None

                GLMresponse = self.client.chat.completions.create(
                    model="glm-4",
                    messages=message,
                )
                choice.message.content = GLMresponse.choices[0].message.content
                response.choices.append(choice)

            return response

    def message_retrieval(self, response):
        """从生成的响应中检索消息内容"""
        # print(f"--- ErnieModelClient message_retrieval ---")

        if not hasattr(response, "choices"):
            return []

        choices = response.choices
        return [choice.message.content for choice in choices]

    def cost(self, response) -> float:
        """计算响应的成本"""
        response.cost = 0
        return 0

    @staticmethod
    def get_usage(response):
        """返回关于模型使用的统计信息"""
        # 根据需要实现以跟踪模型的使用情况
        # returns a dict of prompt_tokens, completion_tokens, total_tokens, cost, model
        return {}


config_list = [
    {
        "model": "GLM-4",
        "model_client_cls": "GLM4Client",
        "device": "null",
        "n": 1,
        "params": {
            "max_length": 6666,
        },
    },
]

assistant1 = autogen.AssistantAgent(
    "assistant",
    system_message='You are a helpful AI assistant.\nSolve tasks using your skills.\nWhen you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.\nReply "TERMINATE" in the end when everything is done.\n  ',
    llm_config={"config_list": config_list},
)
assistant1.register_model_client(model_client_cls=GLM4Client)

user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=5,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config=False,
    # code_execution_config={
    #     "work_dir": "coding",
    #     "use_docker": False,
    # },
)

message = r"""
\begin{array}{c}
\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\sin \left(4\left(t+\frac{\pi}{16}\right)\right)\right]=\mathrm{e}^{\frac{\pi}{16} s} \mathscr{L}[\sin (4 t)]=\mathrm{e}^{\frac{\pi}{16} s} \frac{4}{s^{2}+16} \\
\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\frac{\sqrt{2}}{2}(\sin 4 t+\cos 4 t)\right]=\frac{\sqrt{2}}{2}\left(\frac{4}{s^{2}+16}+\frac{s}{s^{2}+16}\right)
\end{array}

\mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right] 可以化为两个不相等的式子，请问出了什么问题？哪个式子是正确的？
"""

# message = r"""
# X(\mathrm{j} \omega) * X(\mathrm{j} \omega)=0, |\omega|> 2\omega_{m}，能证明
# X(\mathrm{j} \omega)=0, |\omega|>\omega_{m} 吗？
# 其中 * 表示卷积和
# """

# user_proxy.initiate_chat(assistant1, message=message)
# exit()

assistant2 = autogen.AssistantAgent(
    "assistant",
    system_message='You are a helpful AI assistant.\nSolve tasks using your skills.\nWhen you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.\nReply "TERMINATE" in the end when everything is done.\n  ',
    llm_config={"config_list": config_list},
)
assistant2.register_model_client(model_client_cls=GLM4Client)


# 创建聊天组
groupchat = autogen.GroupChat(
    agents=[user_proxy, assistant1, assistant2],
    messages=[],
    max_round=12,
)

# 创建组管理员
manager = autogen.GroupChatManager(
    groupchat=groupchat,
    llm_config={"config_list": config_list},
)
manager.register_model_client(model_client_cls=GLM4Client)

user_proxy.initiate_chat(manager, message=message)
