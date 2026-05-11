import streamlit as st

# 页面配置
st.set_page_config(
    page_title="陆雪琪 | 数字媒体设计师",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        font-family: 'Microsoft YaHei', sans-serif;
    }
    h1 {
        color: #1e3a8a;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    h2 {
        color: #1e40af;
        border-bottom: 3px solid #3b82f6;
        padding-bottom: 0.5rem;
    }
    .section-header {
        color: #1e3a8a;
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-text {
        color: #374151;
        line-height: 1.7;
    }
    .skill-pill {
        background-color: #dbeafe;
        color: #1e40af;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin: 4px;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏
with st.sidebar:
    st.image(
        "../1.png",
        caption="陆雪琪",
        use_column_width=True
    )

    st.markdown("### 基本信息")
    st.write("**性别**：女")
    st.write("**年龄**：22")
    st.write("**所在地**：成都")
    st.write("**电话**：138-XXXX-XXXX")
    st.write("**邮箱**：yizhan.zhang@email.com")

    st.divider()
    st.markdown("### 社交链接")
    st.markdown("[GitHub](https://github.com) | [小红书](https://xiaohongshu.com) | [Behance](https://behance.net)")

    st.divider()
    st.caption("© 2026 陆雪琪 | 成都理工大学")

# 主界面
col1, col2 = st.columns([3, 1])

with col1:
    st.title("陆雪琪")
    st.markdown("<h3 style='color:#64748b;margin-top:-15px;'>数字媒体 · UI/UX设计师 · 独立创作者</h3>",
                unsafe_allow_html=True)

    st.markdown("""
    <div class='info-text'>
        成都理工大学数字媒体技术专业大三学生，热爱视觉设计与交互体验。<br>
        擅长品牌视觉、UI界面设计与短视频内容创作，具备良好的审美能力和执行力。
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric("GPA", "3.7/5.0")
    st.metric("项目经验", "12+")

st.divider()

# 教育背景
st.markdown('<p class="section-header">教育背景</p>', unsafe_allow_html=True)

col_edu1, col_edu2 = st.columns(2)
with col_edu1:
    st.subheader("成都理工大学")
    st.write("**数字媒体技术** | 本科")
    st.write("2023.09 - 2027.06")
    st.write("• 专业排名前15%")
    st.write("• 获得校级优秀学生奖学金两次")

with col_edu2:
    st.subheader("相关课程")
    st.write("• UI/UX设计原理")
    st.write("• 数字影像处理")
    st.write("• 交互设计")
    st.write("• 品牌视觉设计")

st.divider()

# 专业技能
st.markdown('<p class="section-header">专业技能</p>', unsafe_allow_html=True)

skills = {
    "设计工具": ["Figma", "Photoshop", "Illustrator", "After Effects", "Premiere"],
    "编程与开发": ["HTML/CSS", "Python", "Streamlit", "JavaScript基础"],
    "其他能力": ["品牌VI设计", "短视频剪辑", "用户研究", "团队协作"]
}

for category, skill_list in skills.items():
    st.write(f"**{category}**")
    skill_html = " ".join([f'<span class="skill-pill">{skill}</span>' for skill in skill_list])
    st.markdown(skill_html, unsafe_allow_html=True)

st.divider()

# 项目经历
st.markdown('<p class="section-header">项目经历</p>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["品牌重塑项目", "校园APP设计", "短视频内容创作"])

with tab1:
    st.subheader("「知行」教育品牌视觉升级")
    st.write("**2025.03 - 2025.06** | 团队项目（负责人）")
    st.write("• 为教育机构设计全新VI系统，包含Logo、标准色、宣传物料")
    st.write("• 使用Figma完成全套设计，最终交付物获得甲方高度认可")
    st.image("https://picsum.photos/id/201/800/400", use_column_width=True)

with tab2:
    st.subheader("「理工助手」校园移动端UI设计")
    st.write("**2024.09 - 2025.01**")
    st.write("• 负责校园信息查询、课程表、失物招领等核心页面设计")
    st.write("• 采用Material Design风格，注重简洁与可用性")
    st.write("• 项目已进入开发阶段")

with tab3:
    st.subheader("B站/小红书 数字媒体内容创作")
    st.write("**2023至今**")
    st.write("• 累计发布设计教程与生活Vlog 50+条")
    st.write("• 粉丝数 1.2w+，单条最高播放量 35w")
    st.write("• 内容方向：UI设计分享、校园生活记录")

st.divider()

# 校园经历与荣誉
st.markdown('<p class="section-header">校园经历与荣誉</p>', unsafe_allow_html=True)

col_h1, col_h2 = st.columns(2)
with col_h1:
    st.write("**2025** 数字媒体作品展 一等奖")
    st.write("**2024** 校级创新创业大赛 银奖")

with col_h2:
    st.write("**2024** 数字媒体社团 视觉设计部部长")
    st.write("**2023** 迎新晚会舞台视觉设计负责人")

st.divider()

# 自我评价
st.markdown('<p class="section-header">关于我</p>', unsafe_allow_html=True)
st.info("""
    始终保持对设计的热情，相信好的设计能真正改善人们的生活体验。
    注重细节，同时具备较强的学习能力和抗压能力。
    期待在设计领域持续深耕，成为一名有温度、有思考的设计师。
""")

# 页脚
st.divider()
st.markdown(
    "<p style='text-align:center;color:#64748b;font-size:0.9rem;'>感谢观看 · 期待与您交流</p>",
    unsafe_allow_html=True
)