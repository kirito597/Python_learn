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
        {"role": "system", "content": "你是一个文本分类器。请根据我提供的示例，严格判断用户输入的情感倾向。请只输出一个词：正面、负面或中性。不要输出任何其他解释。"},
        {'role': 'user', 'content': '换电池报价8万2！二手车商都不敢收，所谓终身质保条款藏着无数套路，新能源韭菜真不是白叫的。'},
        {'role': 'assistant', 'content': '负面'},
        {'role': 'user', 'content': '驾乘体验非常舒服，增程式没有续航焦虑，月均油电费才300块，国产新能源神车当之无愧。'},
        {'role': 'assistant', 'content': '正面'},
        {'role': 'user', 'content': '驾驶质感不错，但车机逻辑混乱需要适应，价格是否合理建议先试驾后再评判，仁者见仁智者见智。'},
        {'role': 'assistant', 'content': '中性'},
        {'role': 'user', 'content': user_prompt},
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

