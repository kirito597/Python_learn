from openai import OpenAI
from dotenv import load_dotenv

#自动去文件读取相应的信息，这里是apikey
load_dotenv()

#初始化客户端
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# #小样本提示
# messages = [
#     {'role':'system', 'content': ''}
# ]

answer = client.chat.completions.create(
    model='qwen3-max',
    #消息列表，用户和模型的对话
    # stream=True,
    #ai温度，决定其创造性。专业性问题，温度必须给零
    temperature=1.0,
    messages=[
        # #系统提示词
        # {'role':'system', 'content': '你是一个可爱、幽默、风趣的人'},
        # #ai回答
        # {'role':'assistant', 'content': ''},
        #用户提示词
        {'role': 'user', 'content': '你好，我叫小明,是一名python开发工程师'}
    ]
#     messages=messages
)

print(answer.choices[0].message.content)

# #流模式输出
# for chunk in resp:
#     print(chunk.choices[0].delta.content, end='')

#小样本输出

#记忆输出
resp = client.chat.completions.create(
    model='qwen3-max',
    messages=[
        {'role': 'user', 'content':f'{answer}，我的名字是什么？'}
    ]
)

print(resp.choices[0].message.content)