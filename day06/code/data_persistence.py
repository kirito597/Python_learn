import streamlit as st

#streamlit不会保存数据状态，每次刷新页面会从头到位执行一次python代码
st.write('## 数据持久化')

# num = 0
#
# button = st.button('点击按钮改变值+1')
# if button:
#     num += 1
#     st.write(num)

#可以使用其提供的state状态数据来解决问题
#st.session_state #状态数据，默认返回字典
if 'num' not in st.session_state:
    st.session_state['num'] = 0

button = st.button('点击按钮改变值+1')
if button:
    st.session_state['num'] += 1

st.write(st.session_state['num'])