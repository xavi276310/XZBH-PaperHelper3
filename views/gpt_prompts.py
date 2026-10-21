import streamlit as st
from catalog import CATEGORIES, filter_prompts, get_prompts_content
from ui import copy_button


def select_prompt(key, prompts):
    st.session_state.selected_prompt_key = key
    st.session_state.prompt_editor = st.session_state.prompt_drafts.get(key, prompts[key]['content'])


def save_draft():
    st.session_state.prompt_drafts[st.session_state.selected_prompt_key] = st.session_state.prompt_editor


def reset_prompt(prompts):
    key = st.session_state.selected_prompt_key
    st.session_state.prompt_drafts.pop(key, None)
    st.session_state.prompt_editor = prompts[key]['content']


def show_gpt_prompts():
    prompts = get_prompts_content()
    st.session_state.setdefault('prompt_drafts', {})
    key = st.session_state.get('selected_prompt_key', next(iter(prompts)))
    if key not in prompts:
        key = next(iter(prompts))
    st.session_state.selected_prompt_key = key
    st.session_state.setdefault('prompt_editor', st.session_state.prompt_drafts.get(key, prompts[key]['content']))

    st.markdown('<div class="eyebrow">箫张跋扈 · 学术写作工具箱</div>', unsafe_allow_html=True)
    st.title('学术论文写作 GPT 提示词')
    st.write('从标题构思到投稿回复，找到合适的提问方式，让学术表达更清晰。')
    st.caption(f'{len(prompts)} 个提示词 · {len(CATEGORIES)} 类写作场景 · 支持编辑、复制与下载')
    with st.expander('使用方法 · 三步开始'):
        st.markdown('1. 按写作场景筛选，或搜索关键词。\n2. 将模板中的占位内容替换为你的研究信息；中英模板可按需保留一种语言。\n3. 复制到你使用的 AI 工具中，并核对生成内容。')
        st.caption('这里提供提示词模板；复制后在你使用的 AI 工具中完成对话。当前编辑仅在本次会话内保留，需要保存时可下载 TXT。')

    left, right = st.columns([1, 1.75], gap='large')
    with left:
        st.subheader('选择写作场景')
        category = st.selectbox('提示词分类', ['全部分类', *CATEGORIES], key='prompt_category')
        query = st.text_input('搜索提示词', placeholder='例如：摘要、润色、翻译', key='prompt_search')
        matches = filter_prompts(prompts, category, query)
        st.caption(f'找到 {len(matches)} 个提示词')
        with st.container(height=485, border=True):
            if not matches:
                st.info('没有匹配的提示词，请调整关键词或分类。')
            for candidate in matches:
                st.button(prompts[candidate]['title'], key=f'choose_{candidate}',
                          type='primary' if candidate == key else 'secondary',
                          use_container_width=True, on_click=select_prompt, args=(candidate, prompts))
    with right:
        current = prompts[key]
        with st.container(border=True):
            category_name = next(name for name, keys in CATEGORIES.items() if key in keys)
            st.caption(f'当前提示词 / {category_name}')
            st.subheader(current['title'])
            st.text_area('提示词内容', key='prompt_editor', height=420, on_change=save_draft,
                         help='可直接编辑；切换提示词后，本次会话内的草稿仍会保留。')
            st.caption('替换占位内容后，按 Ctrl+Enter 应用修改，再复制或下载。')
            copy_button(st.session_state.prompt_editor)
            download, reset = st.columns(2)
            with download:
                safe_title = current['title'].replace('/', '-')
                st.download_button('下载 TXT', data=st.session_state.prompt_editor.encode('utf-8-sig'),
                                   file_name=safe_title+'.txt', mime='text/plain', use_container_width=True)
            with reset:
                st.button('恢复原始模板', on_click=reset_prompt, args=(prompts,), use_container_width=True)
    st.divider()
    st.caption('使用建议：提供具体的研究背景、原始材料与输出要求，并自行核对事实、数据和引用。')
