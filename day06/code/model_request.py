from openai import OpenAI
from dotenv import load_dotenv
from common import get_llm_response

load_dotenv()

#初始化客户端
client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
result = get_llm_response(client, user_prompt='你是谁？', stream=True)

for chunk in result:
    print(chunk.choices[0].delta.content, end='')
