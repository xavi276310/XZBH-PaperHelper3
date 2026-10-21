import json
import streamlit as st
import streamlit.components.v1 as components


def load_css():
    st.markdown('''<style>
    .block-container {max-width:1240px; padding-top:2.8rem; padding-bottom:3rem;}
    h1 {font-size:2.35rem !important; letter-spacing:-.05em; line-height:1.3 !important;}
    h2,h3 {letter-spacing:-.025em;}
    .eyebrow {color:#0f766e; font-weight:700; font-size:.82rem; letter-spacing:.12em; margin-bottom:.65rem;}
    [data-testid="stSidebar"] {border-right:1px solid rgba(128,128,128,.16);}
    [data-testid="stVerticalBlockBorderWrapper"] {border-radius:16px;}
    [data-testid="stTextArea"] textarea {line-height:1.85; font-size:.94rem;}
    .stButton button,.stDownloadButton button,.stLinkButton a {border-radius:9px; min-height:2.6rem;}
    .stButton button {text-align:left;}
    [data-testid="stCaptionContainer"] {line-height:1.65;}
    @media (max-width: 700px) {.block-container {padding-top:1.6rem;} h1 {font-size:1.8rem !important;}}
    </style>''', unsafe_allow_html=True)


def copy_button(content):
    # JSON serialization keeps quotes/newlines valid; escape HTML script terminators.
    payload = json.dumps(content, ensure_ascii=True).replace('<', r'\u003c').replace('>', r'\u003e').replace('&', r'\u0026')
    template = '''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><style>
    body {margin:0; font-family:system-ui,sans-serif;}
    button {width:100%;padding:12px;border:0;border-radius:9px;background:#0f766e;color:white;font-size:14px;font-weight:600;cursor:pointer;}
    button:hover {background:#115e59;} button:focus-visible {outline:3px solid #5eead4;outline-offset:2px;}
    #status {font-size:12px;color:#64748b;margin-top:7px;line-height:1.5;}
    </style><button id="copy" type="button">复制提示词</button><div id="status" role="status" aria-live="polite"></div><script>
    const text = __PAYLOAD__;
    const button = document.getElementById('copy');
    const status = document.getElementById('status');
    function legacyCopy() {
      const area = document.createElement('textarea'); area.value = text;
      area.style.position = 'fixed'; area.style.left = '-9999px'; document.body.appendChild(area);
      area.select(); let copied = false;
      try {copied = document.execCommand('copy');} finally {area.remove();}
      return copied;
    }
    button.addEventListener('click', async () => {
      let copied = false;
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(text); copied = true;
        } else {copied = legacyCopy();}
      } catch (error) {try {copied = legacyCopy();} catch (ignored) {copied = false;}}
      button.textContent = copied ? '已复制 ✓' : '复制未完成';
      status.textContent = copied ? '可以粘贴到你使用的 AI 工具中。' : '请在上方文本框全选复制，或下载 TXT。';
      setTimeout(() => {button.textContent = '复制提示词';}, 2400);
    });</script></html>'''
    components.html(template.replace('__PAYLOAD__', payload), height=92)
