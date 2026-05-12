import json
"""
函数名称：get_llm_response
params模型参数：
+ client OPenAI标准（SDK），用于发送模型请求
+ * 表示后面的函数参数都必须要使用关键字参数
+ system_prompt 系统提示词
+ few_shot_prompt 小样本提示词
+ user_prompt 用户提示词
+ model 模型名称
+ stream 是否开启流模型
"""


def get_llm_response(client, *, system_prompt='', few_shot_prompt='',
                     user_prompt='', model='qwen3-max', stream=False):
    # 定义聊天列表
    messages = [
    ]

    #判断是否传递那些提示词，如果传递了那么就加入聊天列表中去（空字符串为假）
    if system_prompt:
        messages.append({'role': 'system','content':system_prompt})
    if few_shot_prompt:
        #将few_shot_prompt（json）转换为字典
        messages += json.loads(few_shot_prompt)
    if user_prompt:
        messages.append({'role': 'user','content':user_prompt})

    #发送请求
    resp = client.chat.completions.create(
        model = model,
        messages = messages,
        stream = stream
    )

    #给外界返回结果
    if not stream:
        return resp.choices[0].message.content

    return resp

