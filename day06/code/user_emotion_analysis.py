from openai import OpenAI
from dotenv import load_dotenv
from common import get_llm_response
import json
import streamlit as st

load_dotenv()

#初始化客户端
client = OpenAI(base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

result = ''

st.write('## 用户情感分析助手')
st.divider()

col1, col2 = st.columns([3,1])

with col1:
    comment = st.text_area(label='请输入用户评价：', height=100)
    button = st.button('确定', type='primary')
    #点击按钮，返回结果
    if button:
        result = get_llm_response(client=client, user_prompt=comment)

with col2:
    if result:
        st.write(f'分析结果:**{result}**')