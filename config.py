from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
APP_CONFIG = {
    'title': '论文写作助手 · 箫张跋扈',
    'description': '精选学术写作提示词，覆盖论文撰写、润色、翻译与投稿。',
    'version': '1.1.0',
}
PROMPTS_FILE = BASE_DIR / 'data' / 'prompts.json'
AUTHOR_IMAGE = BASE_DIR / 'tupian.jpg'
