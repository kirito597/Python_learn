from openai import OpenAI
import streamlit as st
from common import get_llm_response

# qwen:https://dashscope.aliyuncs.com/compatible-mode/v1
# deepseek:https://api.deepseek.com

#实现助手侧边栏布局
with st.sidebar:
    api_vendor = st.radio(label='请选择模型提供商', options=['ChatTongYi', 'DeepSeek'])
    if api_vendor == 'ChatTongYi':
        base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
        mode_options = ['qwen-plus', 'qwen3-max', 'qwen-turbo']
    elif api_vendor == 'DeepSeek':
        base_url = 'https://api.deepseek.com'
        mode_options = ['deepseek-chat', 'deepseek-reasoner']

    #模型名称
    model_name = st.selectbox(label='请选择要使用的模型', options=mode_options)
    #apikey让用户自己填写
    api_key = st.text_input(label='请输入你的key', type='password')

#给模型发送请求模板
def get_answer(question: str):
    client = OpenAI(base_url=base_url, api_key=api_key)
    stream = get_llm_response(
        client = client,
        model = model_name,
        user_prompt = question,
        stream=True
    )
    for chunk in stream:
        yield chunk.choices[0].delta.content or ''


st.write('## 我的个人AI超级助手')
st.divider()

if not api_key:
    st.error('请提供访问大模型的API KEY！！！')
    #可以终止后续代码的执行
    st.stop()

#消息列表，把ai回复和问的问题添加进消息里面
if 'messages' not in st.session_state:
    st.session_state['messages'] = [('ai', '你好我是你的个人超级助手,我叫宁姚。')]

#页面渲染
for role, content in st.session_state['messages']:
    st.chat_message(role).write(content)

user_input = st.chat_input(placeholder='请输入')
if user_input:
    #历史模板表示的历史消息，-1表示只取最后一次回复
    _,history = st.session_state['messages'][-1]

    #用户问题
    #st.chat_message用于展示用户消息的 角色 根据不同角色的消息位置的排列和图标展示
    st.chat_message('human').write(user_input)
    st.session_state['messages'].append(('human', user_input))

    #ai回答，在ai回答问题之前需要时间，可以给个延迟
    with st.spinner('正在思考中...'):
        answer = get_answer(f'{history},{user_input}')
        result = st.chat_message('ai').write_stream(answer)
        st.session_state['messages'].append(('ai', result))