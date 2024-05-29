# %%
import json
from types import SimpleNamespace

import requests

import autogen
from myKey import API_Key, Secret_Key

df = open("test.txt", "w", encoding="utf-8")


# %%
def get_access_token():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}"

    payload = json.dumps("")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def chat_ERNIE_Speed(messages):
    # 文档 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/klqx7b1xf
    url = (
        "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token="
        + get_access_token()
    )

    payload = json.dumps({"messages": messages})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def query_ERNIE_Speed(content):
    return chat_ERNIE_Speed([{"role": "user", "content": content}])


# response = query_ERNIE_Speed("Write python code to print Hello World!")
# print(response)

# %%


class ErnieModelClient:
    def __init__(self, config, **kwargs):
        # print(f"ErnieModelClient config: {config}")
        self.device = config.get("device", "cpu")
        self.model_name = config["model"]

        gen_config_params = config.get("params", {})
        self.max_length = gen_config_params.get("max_length", 256)

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

                # new_message = []
                # for i,m in enumerate(message):
                #     if(len(new_message)%2==0):
                #         if(m["role"]!="assistant"):
                #             new_message.append({"role": "user", "content": m})
                #         else:
                #             con=chat_ERNIE_Speed(new_message)["result"]
                #             new_message.append({"role": "assistant", "content": con})
                #     else:
                #         new_message.append({"role": "assistant", "content": m})

                content = json.dumps(message, indent=2, ensure_ascii=False)
                df.write(content)
                df.write("\n" + "-" * 100 + "\n")
                Ernie_response = query_ERNIE_Speed(content)
                # print(Ernie_response)

                choice = SimpleNamespace()
                choice.message = SimpleNamespace()
                choice.message.content = Ernie_response["result"]
                choice.message.function_call = None
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
        "model": "Ernie",
        "model_client_cls": "ErnieModelClient",
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
assistant1.register_model_client(model_client_cls=ErnieModelClient)

assistant2 = autogen.AssistantAgent(
    "assistant",
    system_message='You are a helpful AI assistant.\nSolve tasks using your skills.\nWhen you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.\nReply "TERMINATE" in the end when everything is done.\n  ',
    llm_config={"config_list": config_list},
)
assistant2.register_model_client(model_client_cls=ErnieModelClient)


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
manager.register_model_client(model_client_cls=ErnieModelClient)


# message = r"""
# \begin{array}{c}
# \mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\sin \left(4\left(t+\frac{\pi}{16}\right)\right)\right]=\mathrm{e}^{\frac{\pi}{16} s} \mathscr{L}[\sin (4 t)]=\mathrm{e}^{\frac{\pi}{16} s} \frac{4}{s^{2}+16} \\
# \mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right]=\mathscr{L}\left[\frac{\sqrt{2}}{2}(\sin 4 t+\cos 4 t)\right]=\frac{\sqrt{2}}{2}\left(\frac{4}{s^{2}+16}+\frac{s}{s^{2}+16}\right)
# \end{array}

# \mathscr{L}\left[\sin \left(4 t+\frac{\pi}{4}\right)\right] 可以化为两个不相等的式子，请问出了什么问题？哪个式子是正确的？
# """

message = r"""
X(\mathrm{j} \omega) * X(\mathrm{j} \omega)=0, |\omega|> 2\omega_{m}，能证明
X(\mathrm{j} \omega)=0, |\omega|>\omega_{m} 吗？
其中 * 表示卷积和
"""

# user_proxy.initiate_chat(assistant, message)
user_proxy.initiate_chat(manager, message=message)
# print(query_ERNIE_Speed(message)["result"])
