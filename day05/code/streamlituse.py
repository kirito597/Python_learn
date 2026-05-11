import streamlit as st

# import pandas as pd
#
# # 应用标题
# st.title('成都理工校园数字智慧大屏')
# st.divider()
#
# # 标题组件
# st.header('成都理工校园数字智慧大屏')
# st.subheader('数媒专业')
#
# # 文本组件
# name = st.text_input('请输入你的名字:')
# st.write(f"你输入的名字是：{name}")
# st.divider()
#
# # 显示文本 支持Markdown语法
# st.markdown('# 一级标题')
# st.markdown('## 二级标题')
# st.markdown('### 三级标题')
#
# # 支持html标记的解析
# st.markdown(
#     '<h2 style="color:red;font-size:22px;">你好啊，这是二级标题</h2>',
#     unsafe_allow_html=True
# )
#
# st.markdown(
#     """
#         <h2 style="color:red;font-size:22px;">你好啊，这是二级标题</h2>
#         <div style="width:200px;height:200px;background-color:orange;">这是div标记</div>
#     """,
#     unsafe_allow_html=True
# )
# st.divider()
#
# # 单一文本组件
# st.text("""
#     鸡太美
#     坤坤很牛
#     坤坤喜欢篮球
#     坤坤喜欢rap
# """)
#
# # 按钮组件
# col1, col2 = st.columns(2)
# with col1:
#     st.button('确定')
# with col2:
#     st.button('确定', type='primary')
#
# # 代码组件（修正缩进）
# st.code("""
# def shopping_fn():
#     name = input('请输入商品名称:')
#     if name.strip() == '':
#         print('商品名称不能为空')
#         return
#     print('后续逻辑')
# shopping_fn()
# """, language='python')
#
# # 通用方法
# st.write('hello，美女帅哥们！')
# st.write(666)
# st.write(['a', 'b', 'c'])
# st.write({'name': '张三', 'age': 20})
#
# df = pd.DataFrame({
#     '姓名': ['张三', '李四', '王五'],
#     '年龄': [18, 19, 20],
#     '性别': ['男', '男', '女']
# })
# st.write(df)
#
# # 使用 markdown 显示标题
# st.markdown('# 一级标题')
# st.markdown('## 二级标题')
#
# 图片组件
# st.image(
#     'https://pic.rmb.bdstatic.com/bjh/events/5c4c2f6f2ee97c4de8612026418e372b2310.jpeg@h_1280',
#     width=200,
#     caption='坤坤喜欢篮球、rap、唱歌'
# )
#
# # 视频组件（使用更可靠的视频源）
# st.video('https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4', width=600)

# #复选框
# cb = st.text('请选择你的爱好：')
# like1 = st.checkbox('篮球', value=True)
# like2 = st.checkbox('看电影', value=False)
# st.write(like1)

# #单选框
# gender = st.radio(
#     label='请选择你的性别',
#     options=['男', '女', '保密'],
#     index=0,
#     help='如果不想透露性别，可以选择保密'
# )
#
# if gender == '男':
#     st.write('先生，你好')
# elif gender == '女':
#     st.write('女士，你好')
# else:
#     st.write('你好')
#
# #下拉框
# lesson = st.selectbox(
#     label='请选择你的课程：',
#     options=['Python数据分析','大模型开发','agent应用开发'],
#     index=1,
#     help='如果没有你想要的课程，请联系我们'
# )
# st.write(lesson)
#
# #多选框组件
# options = st.multiselect(
#     label='请问你喜欢的水果是什么',
#     options=['橘子','樱桃','香蕉','哈密瓜','苹果'],
#     help='如果没有你喜欢的水果,可以不选'
# )

# #滑动拉杆组件
# #注意点：min_value,max_value,step值的设置必须是同类型的
# temp = st.slider(
#     label='请设置模型的温度:',
#     min_value=0,
#     step=1,
#     max_value=20,
# )
# st.write(temp)

# #输入框组件
# name = st.text_input("请输入你的名字")
# btn = st.button('确定', type='primary')
# if btn:
#     st.write(name)
#
# st.divider()
#
# username = st.text_input('请输入用户名', max_chars=10, help='最多只能输入10个字符')
# st.write(username)
#
# st.divider()

#多行文本域组件
#placeholder:提示信息，用户输入内容时会隐藏
# text = st.text_area(label='欢迎使用个人AI搜索', placeholder='请输入你的问题', height=200, max_chars=200)

#侧边栏和分栏布局
#侧边栏，with将侧边栏组件放在指定位置上
with st.sidebar:
    st.write('# 侧边栏')
    st.divider()
    name = st.text_input('请输入你的姓名')

st.write('## 欢迎来到我的个人网站')
st.divider()

#分页显示
tab1, tab2, tab3 = st.tabs(['性别', '联系方式', '喜欢水果'])
with tab1:
    gender = st.radio(
        label='请选择你的性别:',
        options=['男', '女', '保密'],
        index=0,
        help='如果你不想透露你真实的性别，可以选择保密'
    )
    if gender == '男':
        st.write('男士，您好！')
    elif gender == '女':
        st.write('女士，您好！')
    else:
        st.write('您好！')
with tab2:
    contact = st.selectbox('你希望我们通过什么方式来联系你:', ['电话', '邮件', '微信'], help='如果没有期望的联系途径，请xxx')
    st.write(f'好的，我们会通过{contact}方式来联系您！')
with tab3:
    options = st.multiselect(
        label='请问你喜欢的水果是什么:',
        options=['橘子', '樱桃', '车厘子', '香蕉', '哈密瓜', '苹果'],
        default=['橘子', '车厘子'],
        help='如果没有你喜欢的水果，可以先不进行选择'
    )
    st.write(options)