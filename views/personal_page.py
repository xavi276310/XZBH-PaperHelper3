from html import escape

import streamlit as st
import streamlit.components.v1 as components

from config import AUTHOR_IMAGE


def show_bilibili_card(title, bvid):
    """显示视频预览，点击后在新标签页打开 B 站。"""
    video_url = f"https://www.bilibili.com/video/{bvid}/"
    player_url = (
        "https://player.bilibili.com/player.html"
        f"?isOutside=true&bvid={bvid}&p=1&autoplay=0"
    )
    safe_title = escape(title, quote=True)

    with st.container(border=True):
        st.markdown(f"#### {title}")

        components.html(
            f"""
            <!DOCTYPE html>
            <html lang="zh-CN">
            <head>
                <meta charset="utf-8">
                <style>
                    body {{
                        margin: 0;
                        font-family: sans-serif;
                    }}

                    .video-card {{
                        position: relative;
                        width: 100%;
                        aspect-ratio: 16 / 9;
                        overflow: hidden;
                        border-radius: 12px;
                        background: #17202a;
                    }}

                    .video-card iframe {{
                        width: 100%;
                        height: 100%;
                        border: none;
                        pointer-events: none;
                    }}

                    .video-link {{
                        position: absolute;
                        inset: 0;
                        display: flex;
                        align-items: flex-end;
                        justify-content: flex-end;
                        padding: 14px;
                        text-decoration: none;
                        background: linear-gradient(
                            transparent 65%,
                            rgba(0, 0, 0, 0.45)
                        );
                    }}

                    .video-link:focus-visible {{
                        outline: 3px solid #5eead4;
                        outline-offset: -3px;
                    }}

                    .video-link span {{
                        padding: 8px 12px;
                        border-radius: 8px;
                        background: #fb7299;
                        color: white;
                        font-size: 13px;
                        font-weight: bold;
                    }}

                    .video-link:hover span {{
                        background: #e65e86;
                    }}
                </style>
            </head>
            <body>
                <div class="video-card">
                    <iframe
                        src="{player_url}"
                        title="{safe_title}的视频预览"
                        loading="lazy"
                        tabindex="-1"
                        aria-hidden="true"
                    ></iframe>

                    <a
                        class="video-link"
                        href="{video_url}"
                        target="_blank"
                        rel="noopener noreferrer"
                        aria-label="在 B 站观看：{safe_title}"
                    >
                        <span>点击在 B 站观看 ↗</span>
                    </a>
                </div>
            </body>
            </html>
            """,
            height=310,
            scrolling=True,
        )

        st.link_button(
            "在 B 站观看 ↗",
            video_url,
            use_container_width=True,
        )


def show_personal_page():
    st.markdown(
        '<div class="eyebrow">关于作者</div>',
        unsafe_allow_html=True,
    )

    st.title("你好，我是箫张跋扈")
    st.write("分享深度学习、模型模块与学术写作的实践经验。")

    st.markdown(
        "我将常用的学术写作提示词整理成这个工具，"
        "希望帮你更快地组织问题、优化表达，"
        "把更多精力放在研究本身。"
    )

    st.link_button(
        "访问我的 B 站空间 ↗",
        "https://space.bilibili.com/478113245",
        type="primary",
    )

    st.divider()
    st.subheader("视频与学习资源")
    st.write("精选模块融合实践视频，点击视频预览或下方按钮即可前往 B 站观看。")

    first, second = st.columns(2)

    with first:
        show_bilibili_card(
            title="模块融合实践 · 视频一",
            bvid="BV1zg4y1C7oP",
        )

    with second:
        show_bilibili_card(
            title="模块融合实践 · 视频二",
            bvid="BV1Kw411G7Rw",
        )

    st.caption("若视频预览未能加载，可直接点击“在 B 站观看”按钮。")

    st.divider()
    st.subheader("了解更多")
    st.write(
        "欢迎通过下方图片了解更多课程与学习资料，"
        "也可以先从公开分享的视频开始。"
    )

    if AUTHOR_IMAGE.is_file():
        image_col, _ = st.columns([2, 1])

        with image_col:
            st.image(
                str(AUTHOR_IMAGE),
                use_container_width=True,
                caption="课程与学习资料",
            )
    else:
        st.info("更多内容可前往上方 B 站空间查看。")
