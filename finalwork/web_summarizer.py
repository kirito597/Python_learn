from openai import OpenAI
import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import json


def get_llm_response(client, *, system_prompt='', few_shot_prompt='',
                     user_prompt='', model='qwen3-max', stream=False, temperature=0.7):
    """调用大语言模型的通用函数"""
    messages = []

    if system_prompt:
        messages.append({'role': 'system', 'content': system_prompt})

    if few_shot_prompt:
        few_shot_data = json.loads(few_shot_prompt)
        if isinstance(few_shot_data, list):
            messages += few_shot_data

    if user_prompt:
        messages.append({'role': 'user', 'content': user_prompt})

    resp = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=stream,
        temperature=temperature
    )

    if not stream:
        return resp.choices[0].message.content
    return resp


# ========== 页面配置 ==========
st.set_page_config(page_title="网页摘要智能体", page_icon="📄", layout="wide")

st.title("网页摘要智能体")

# ========== 侧边栏配置 ==========
with st.sidebar:
    st.header("配置")

    # 模型提供商选择
    api_vendor = st.radio(
        "模型提供商",
        options=["通义千问", "DeepSeek"]
    )

    if api_vendor == "通义千问":
        base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
        model_options = ["qwen3-max", "qwen-plus", "qwen-turbo"]
    else:
        base_url = "https://api.deepseek.com"
        model_options = ["deepseek-chat", "deepseek-reasoner"]

    # 模型选择
    model_name = st.selectbox("模型", options=model_options)

    # 温度调节
    temperature = st.slider(
        "温度",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.05
    )

    # 摘要长短选择
    summary_length = st.select_slider(
        "摘要长短",
        options=["极短", "短", "中等", "长"],
        value="中等"
    )

    # 原文处理策略
    st.header("原文处理")
    truncate_strategy = st.radio(
        "原文处理策略",
        options=["完整保留", "截断（5000字符）"],
        help="完整保留：AI看到完整原文，消耗更多token；截断：AI只看到前5000字符，节省token"
    )

    # API Key
    api_key = st.text_input("API Key", type="password")


# 网页内容爬取
def extract_web_content(url: str, truncate: bool = False, max_length: int = 5000):
    """提取网页核心内容"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, 'html.parser')

        # 移除无关元素
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()

        # 提取标题
        title = soup.title.string if soup.title else "无标题"

        # 提取正文
        content_selectors = ["article", "main", ".content", ".post-content", "#content"]
        main_content = None
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break

        if not main_content:
            main_content = soup.body

        text = main_content.get_text(separator='\n', strip=True)
        text = re.sub(r'\n\s*\n', '\n\n', text)

        # 完整内容
        full_content = text

        # 根据策略决定AI用的内容
        if truncate and len(text) > max_length:
            ai_content = text[:max_length] + "...\n[内容已截断]"
        else:
            ai_content = text

        return {
            "success": True,
            "title": title,
            "content_for_ai": ai_content,
            "content_full": full_content,
            "url": url,
            "truncated": truncate and len(text) > max_length,
            "original_length": len(text)
        }

    except Exception as e:
        return {"success": False, "error": str(e)}


# 生成摘要
def generate_summary(web_data: dict, model: str, temp: float, length: str, api_key: str, base_url: str):
    """调用API生成摘要"""
    try:
        client = OpenAI(base_url=base_url, api_key=api_key)

        # 根据摘要长短设置字数要求
        length_map = {
            "极短": "150字以内",
            "短": "300字以内",
            "中等": "500字左右",
            "长": "800字左右"
        }

        # 提示AI内容是否被截断
        truncate_note = ""
        if web_data.get("truncated"):
            truncate_note = "\n注意：原文内容较长，已截断处理，你只看到了前5000字符。"

        system_prompt = f"""
        你是专业的网页摘要助手。请根据用户提供的网页内容生成简洁、准确的摘要。
        要求：
        1. 先用一句话概括网页的核心内容
        2. 然后用3-5个要点列出关键信息
        3. 保持客观，只提取原文中的信息，不添加个人评论
        4. 如果内容包含数据，请提取重要数据
        5. 摘要总字数控制在{length_map[length]}
        6. 输出格式使用Markdown{truncate_note}"""

        user_content = f"""
        标题：{web_data['title']}
        
        正文内容：
        {web_data['content_for_ai']}
        
        请根据以上内容生成{length_map[length]}的摘要。
        """

        stream = get_llm_response(
            client=client,
            model=model,
            system_prompt=system_prompt,
            user_prompt=user_content,
            stream=True,
            temperature=temp
        )

        for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    except Exception as e:
        yield f"错误：{str(e)}"


# 主界面
# 显示当前配置
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.write(f"**当前模型：** {model_name}")
with col2:
    st.write(f"**温度：** {temperature:.2f}")
with col3:
    st.write(f"**摘要长短：** {summary_length}")
with col4:
    strategy_display = "完整" if truncate_strategy == "完整保留" else "截断"
    st.write(f"**原文策略：** {strategy_display}")

st.divider()

# 输入区域
url = st.text_input("网页地址", placeholder="https://example.com/article")
submit = st.button("开始摘要", type="primary")

# 处理摘要请求
if submit and url:
    if not api_key:
        st.error("请先在侧边栏输入 API Key")
    elif not url.startswith(("http://", "https://")):
        st.error("请输入有效的网页地址（以 http:// 或 https:// 开头）")
    else:
        # 判断是否截断
        truncate = (truncate_strategy == "截断（5000字符）")

        # 提取网页内容
        with st.spinner("正在提取网页内容..."):
            web_data = extract_web_content(url, truncate=truncate)

        if not web_data["success"]:
            st.error(f"提取失败：{web_data.get('error', '未知错误')}")
        else:
            # 显示网页信息
            st.success(f"成功提取：{web_data['title']}")

            # 显示内容长度信息
            if web_data["truncated"]:
                st.info(f"原文长度：{web_data['original_length']} 字符，已截断至5000字符用于AI处理")
            else:
                st.info(f"原文长度：{web_data['original_length']} 字符，完整保留")

            # 生成并显示摘要
            st.subheader("摘要结果")
            summary_stream = generate_summary(
                web_data, model_name, temperature, summary_length, api_key, base_url
            )
            st.write_stream(summary_stream)

            # 原文预览（折叠）- 显示完整内容
            with st.expander("查看原文"):
                st.text(web_data['content_full'])

elif submit and not url:
    st.warning("请输入网页地址")