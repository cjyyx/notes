# %%
import json

import requests

from myKey import API_Key, Secret_Key

# %%


def get_access_token():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}"

    payload = json.dumps("")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


# %%

# 文档 https://cloud.baidu.com/doc/WENXINWORKSHOP/s/klqx7b1xf

def main():
    """
    替换下列示例中的创建服务时填写的API名称
    """
    url = (
        "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token="
        + get_access_token()
    )

    payload = json.dumps({"messages": [{"role": "user", "content": "介绍一下北京"}]})
    headers = {"Content-Type": "application/json"}

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == "__main__":
    main()
