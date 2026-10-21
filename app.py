import streamlit as st

from config import APP_CONFIG
from ui import load_css
from views.gpt_prompts import show_gpt_prompts
from views.personal_page import show_personal_page

st.set_page_config(
    page_title=APP_CONFIG['title'], page_icon='📚',
    layout='wide', initial_sidebar_state='expanded',
)
load_css()
with st.sidebar:
    st.markdown('### 📚 论文写作助手')
    st.caption('箫张跋扈 · 学术写作工具箱')
    st.divider()
    selected_page = st.radio('功能导航', ['学术写作提示词', '关于作者'], key='navigation')
    st.divider()
    st.caption('从写作到投稿，让每一次提问更清晰。')
    st.caption(f"版本 {APP_CONFIG['version']}")

if selected_page == '学术写作提示词':
    show_gpt_prompts()
else:
    show_personal_page()
