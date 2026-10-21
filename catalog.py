import json
from config import PROMPTS_FILE

CATEGORIES = {
    '学术角色': ['学术角色', '论文评审专家'],
    '论文撰写': ['写标题', '写英文标题', '写摘要', '写英文摘要', '缩写名称', '论文续写', '论文致谢', '论文大纲'],
    '学术润色': ['英文润色1', '英文润色2', '中文润色', 'SCI论文润色', '期刊会议风格', '润色英文段落结构和句子逻辑', '直接润色段落', '多版本参考', '错误纠正', '重新回答', '语法检查/查找语法错误', '语法校正', '语法句法', '润色定位', '修改建议', '修改意见', '封装基本事实/原理/背景', '逻辑论证辅助', '个性化润色'],
    '中英翻译': ['论文翻译', '中译英1', '中译英2', '中译英3', '中英互译'],
    '表达改写': ['内容降重', '改写降重', '同义词替换降重', '避免连续相同', '缩写扩写降重', '关键词汇替换降重', '句式变换降重', '逻辑重组', '综合改写', '概念解释降重'],
    '参考文献': ['检查参考文献格式', 'APA格式校正'],
    '投稿与审稿': ['撰写Cover letter', '解释审稿人反馈'],
}


def get_prompts_content():
    with PROMPTS_FILE.open(encoding='utf-8') as handle:
        return json.load(handle)


def filter_prompts(prompts, category='全部分类', query=''):
    candidates = prompts if category == '全部分类' else CATEGORIES[category]
    terms = query.casefold().split()
    return [key for key in candidates if all(
        term in (key + ' ' + prompts[key]['title'] + ' ' + prompts[key]['content']).casefold()
        for term in terms
    )]
