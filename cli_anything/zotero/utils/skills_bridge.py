"""Skills Bridge —— 将 27个 Academic Research Skills 集成到 Zotero 工作流中。

映射关系:
  Zotero操作 → Academic Skill
  - 文献搜索/发现 → lit-review, scientific-literature-search
  - 文献管理/引用 → citation-management
  - 论文写作 → academic-paper, scientific-manuscript-writing
  - 论文审稿 → academic-paper-reviewer, peer-review-methodology, seven-pass-review
  - 研究设计 → hypothesis-generation, scientific-brainstorming
  - 数据分析 → exploratory-data-analysis, statistical-analysis
  - 可视化 → scientific-slides, scientific-schematics, nature-figure-guide 等
  - 完整性验证 → audit-reproducibility, verify-claims
"""

SKILL_MAP = {
    # ===== 文献检索 =====
    "search": {
        "lit-review": {
            "name": "快速文献检索",
            "skill": "lit-review",
            "trigger": "find papers on {query}",
            "description": "快速检索指定主题的学术文献"
        },
        "systematic-review": {
            "name": "系统评价",
            "skill": "literature-review",
            "trigger": "conduct a systematic review on {query}",
            "description": "PRISMA 协议系统评价，含 Boolean/MeSH 搜索策略"
        },
        "deep-search": {
            "name": "深度文献搜索",
            "skill": "scientific-literature-search",
            "trigger": "search literature with PICO framework for {query}",
            "description": "PICO 框架 + 三级搜索（数据库/AI辅助/内容提取）"
        },
    },
    # ===== 研究设计 =====
    "research": {
        "ideation": {
            "name": "研究创意生成",
            "skill": "research-ideation",
            "trigger": "give me research ideas on {topic}",
            "description": "根据主题生成创新研究思路"
        },
        "brainstorming": {
            "name": "科学头脑风暴",
            "skill": "scientific-brainstorming",
            "trigger": "brainstorm research approaches for {topic}",
            "description": "SCAMPER/六顶思考帽/形态分析/TRIZ 方法"
        },
        "hypothesis": {
            "name": "假设生成",
            "skill": "hypothesis-generation",
            "trigger": "formulate testable hypotheses for {topic}",
            "description": "观察→可检验假设→预测→机制→实验设计"
        },
        "deep-research": {
            "name": "深度研究",
            "skill": "deep-research",
            "trigger": "deep research on {topic}",
            "description": "13智能体流水线，7种模式，含系统评价+Meta分析"
        },
    },
    # ===== 论文写作 =====
    "writing": {
        "write-paper": {
            "name": "撰写论文",
            "skill": "academic-paper",
            "trigger": "write academic paper on {topic}",
            "description": "12智能体写作流水线，10种模式，6种论文类型"
        },
        "manuscript": {
            "name": "标准稿件写作",
            "skill": "scientific-manuscript-writing",
            "trigger": "write manuscript following IMRAD for {topic}",
            "description": "IMRAD结构，APA/AMA/Vancouver/IEEE引用"
        },
        "citation": {
            "name": "引用管理",
            "skill": "citation-management",
            "trigger": "manage citations for my paper",
            "description": "Zotero/Mendeley/EndNote + APA/Vancouver/ACS/Nature格式"
        },
        "outline": {
            "name": "论文大纲",
            "skill": "academic-paper",
            "trigger": "write paper outline on {topic} at /outline",
            "description": "生成论文大纲和章节规划"
        },
        "revision": {
            "name": "论文修改",
            "skill": "academic-paper",
            "trigger": "revise my paper on {topic} at /revision",
            "description": "修改润色 + 去AI痕迹 + 风格校准"
        },
    },
    # ===== 论文审稿 =====
    "review": {
        "full-review": {
            "name": "完整审稿",
            "skill": "academic-paper-reviewer",
            "trigger": "review my paper",
            "description": "5人独立审稿（EIC+3同行+魔鬼代言人）"
        },
        "peer-review": {
            "name": "同行评审",
            "skill": "peer-review-methodology",
            "trigger": "peer review this manuscript",
            "description": "7阶段评估体系"
        },
        "seven-pass": {
            "name": "七轮对抗审稿",
            "skill": "seven-pass-review",
            "trigger": "seven pass review of my paper",
            "description": "7并行子智能体对抗性审稿"
        },
        "verify-citations": {
            "name": "引用验证",
            "skill": "verify-claims",
            "trigger": "verify these citations",
            "description": "验证引用真实性和准确性"
        },
        "audit-data": {
            "name": "数据审计",
            "skill": "audit-reproducibility",
            "trigger": "audit reproducibility of my paper",
            "description": "数值声明 vs R/Stata/Python 输出交叉检查"
        },
    },
    # ===== 可视化 =====
    "visualization": {
        "slides": {
            "name": "学术幻灯片",
            "skill": "scientific-slides",
            "trigger": "create presentation slides for my paper",
            "description": "会议/答辩/基金演讲，PowerPoint+Beamer"
        },
        "schematics": {
            "name": "科学示意图",
            "skill": "scientific-schematics",
            "trigger": "design scientific diagram for {topic}",
            "description": "图形摘要/机制图/通路图，BioRender/Inkscape"
        },
        "poster": {
            "name": "学术海报",
            "skill": "latex-research-posters",
            "trigger": "create research poster",
            "description": "LaTeX 海报 (beamerposter/tikzposter/baposter)"
        },
        "nature-fig": {
            "name": "Nature 图表",
            "skill": "nature-figure-guide",
            "trigger": "prepare figures for Nature submission",
            "description": "Nature 期刊图表规范（300+DPI, Helvetica/Arial）"
        },
    },
    # ===== 数据分析 =====
    "analysis": {
        "eda": {
            "name": "探索性分析",
            "skill": "exploratory-data-analysis",
            "trigger": "exploratory data analysis on {data}",
            "description": "数据探索、分布检查、异常检测"
        },
        "statistics": {
            "name": "统计分析",
            "skill": "statistical-analysis",
            "trigger": "statistical analysis of {data}",
            "description": "假设检验、回归分析、效应量计算"
        },
        "critical-thinking": {
            "name": "证据评估",
            "skill": "scientific-critical-thinking",
            "trigger": "evaluate the evidence for {claim}",
            "description": "GRADE评级、偏倚评估、效应量解读"
        },
    },
    # ===== 完整流水线 =====
    "pipeline": {
        "full-pipeline": {
            "name": "完整学术流水线",
            "skill": "academic-pipeline",
            "trigger": "run full academic pipeline on {topic}",
            "description": "研究→写作→审稿→修改→再审→定稿，10阶段全自动"
        },
        "research-to-paper": {
            "name": "研究到论文",
            "skill": "academic-pipeline",
            "trigger": "research to paper on {topic}",
            "description": "深度研究 + 论文写作一站式"
        },
    },
}

# 期刊图表规范映射
JOURNAL_FIGURE_GUIDES = {
    "nature": "nature-figure-guide",
    "science": "science-figure-guide",
    "lancet": "lancet-figure-guide",
    "nejm": "nejm-figure-guide",
    "cancer research": "cancer-research-figure-guide",
    "cell": "nature-figure-guide",
}


def get_skill(category, key):
    """获取指定 Skill 的配置。"""
    return SKILL_MAP.get(category, {}).get(key)


def list_categories():
    """列出所有 Skill 分类。"""
    return list(SKILL_MAP.keys())


def list_skills(category=None):
    """列出所有（或指定分类的）Skill。"""
    if category:
        return SKILL_MAP.get(category, {})
    result = {}
    for cat, skills in SKILL_MAP.items():
        result[cat] = list(skills.keys())
    return result


def get_pipeline_for_task(task_type):
    """根据任务类型推荐 Skill 流水线。

    Args:
        task_type: "literature_review" | "original_article" | "case_report"
                   | "meta_analysis" | "grant_proposal" | "thesis"
    """
    pipelines = {
        "literature_review": [
            "search.systematic-review",
            "analysis.critical-thinking",
            "writing.write-paper",
            "review.seven-pass",
        ],
        "original_article": [
            "research.hypothesis",
            "analysis.statistics",
            "writing.manuscript",
            "visualization.schematics",
            "visualization.slides",
            "review.full-review",
        ],
        "meta_analysis": [
            "search.deep-search",
            "research.deep-research",
            "analysis.statistics",
            "writing.write-paper",
            "review.peer-review",
        ],
        "grant_proposal": [
            "research.ideation",
            "research.brainstorming",
            "writing.outline",
            "visualization.schematics",
        ],
        "thesis": [
            "pipeline.full-pipeline",
            "review.seven-pass",
            "visualization.slides",
            "visualization.poster",
        ],
    }
    return pipelines.get(task_type, [])


def get_journal_guide(journal_name):
    """根据期刊名获取图表规范 Skill。

    Args:
        journal_name: 期刊名（如 "Nature", "Cancer Research"）
    """
    for key, skill in JOURNAL_FIGURE_GUIDES.items():
        if key in journal_name.lower():
            return skill
    return "nature-figure-guide"  # 默认
