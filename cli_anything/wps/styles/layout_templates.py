"""布局模板 —— 整合 pptx-from-layouts 59种布局 + scientific-slides 演讲结构。

14页标准PPT结构，每页对应一种布局模式。
来源:
  pptx-from-layouts: Cover/Column/Grid/Image/Contact 布局索引
  scientific-slides: Hook→Context→Problem→Approach→Results→Implications→Closure 叙事弧
"""

class LayoutTemplate:
    """单页布局模板。"""

    def __init__(self, name, category, description, elements, structural_rules=None):
        self.name = name
        self.category = category       # cover/content/column/grid/image/close
        self.description = description
        self.elements = elements       # [{"type":"title","x":0,"y":30,"w":960,"h":60,"fs":42}, ...]
        self.structural_rules = structural_rules or {}

    def to_dict(self):
        return {"name": self.name, "category": self.category,
                "description": self.description, "elements": self.elements}


# ============================================
# 14 页标准叙事结构 (scientific-slides 叙事弧)
# ============================================

LAYOUTS = {}

# --- 封面 ---
LAYOUTS["cover"] = LayoutTemplate(
    name="封面", category="cover",
    description="深色全屏 + 72pt大字标题 + 装饰线 + 副标题/日期",
    elements=[
        {"type": "bg", "color": "primary"},
        {"type": "line", "x": 0, "y": 0, "w": 960, "h": 18, "color": "secondary"},
        {"type": "text", "x": 0, "y": 100, "w": 960, "h": 150, "text": "{title}", "fs": 72, "color": "white", "bold": True, "align": 2},
        {"type": "line", "x": 280, "y": 270, "w": 400, "h": 5, "color": "white"},
        {"type": "text", "x": 0, "y": 365, "w": 960, "h": 60, "text": "{subtitle}", "fs": 32, "color": "accent_light", "bold": True, "align": 2},
        {"type": "line", "x": 0, "y": 530, "w": 960, "h": 8, "color": "secondary"},
    ]
)

# --- 目录（演讲总览）---
LAYOUTS["toc"] = LayoutTemplate(
    name="目录", category="content",
    description="左侧蓝色装饰条 + 编号圆角方块 + 6项导航",
    elements=[
        {"type": "line", "x": 0, "y": 0, "w": 22, "h": 540, "color": "primary"},
        {"type": "text", "x": 60, "y": 25, "w": 400, "h": 65, "text": "目  录", "fs": 50, "color": "primary", "bold": True},
        {"type": "line", "x": 60, "y": 100, "w": 120, "h": 5, "color": "secondary"},
        {"type": "grid_items", "x": 60, "y": 140, "cols": 1, "rows": 6, "gap": 63, "item_w": 840, "item_h": 56,
         "fields": ["{num}", "{title}", "{desc}"],
         "styles": [{"fs": 24, "color": "white", "bold": True, "bg": "primary", "w": 56},
                    {"fs": 28, "color": "dark", "bold": True},
                    {"fs": 14, "color": "gray"}]},
    ]
)

# --- 概述/背景 ---
LAYOUTS["overview"] = LayoutTemplate(
    name="概览", category="content",
    description="顶部深色横幅 + 信息卡片矩阵 + 侧边荣誉栏",
    elements=[
        {"type": "line", "x": 0, "y": 0, "w": 960, "h": 100, "color": "primary"},
        {"type": "text", "x": 0, "y": 15, "w": 960, "h": 50, "text": "{title}", "fs": 42, "color": "white", "bold": True, "align": 2},
        {"type": "grid_cards", "x": 35, "y": 120, "cols": 2, "rows": 4, "gap_x": 20, "gap_y": 88, "item_w": 430, "item_h": 80,
         "fields": ["{label}", "{value}"],
         "styles": [{"fs": 16, "color": "white", "bold": True, "bg": "primary", "h": 38},
                    {"fs": 19, "color": "dark", "bold": True}]},
        {"type": "sidebar", "x": 720, "y": 120, "w": 200, "h": 360, "color": "light", "text": "{sidebar}"},
    ]
)

# --- 时间轴（历史/发展）---
LAYOUTS["timeline"] = LayoutTemplate(
    name="时间轴", category="column",
    description="左侧圆点+竖线+右侧事件，适合历史/发展内容",
    elements=[
        {"type": "text", "x": 35, "y": 30, "w": 800, "h": 50, "text": "{title}", "fs": 38, "color": "primary", "bold": True},
        {"type": "line", "x": 35, "y": 85, "w": 150, "h": 3, "color": "secondary"},
        {"type": "timeline_items", "x": 40, "start_y": 120, "count": 6, "gap": 55,
         "fields": ["{date}", "{event}"],
         "styles": [{"fs": 16, "color": "primary", "bold": True, "w": 110},
                    {"fs": 16, "color": "dark", "w": 550}]},
        {"type": "sidebar", "x": 650, "y": 120, "w": 280, "h": 360, "color": "light", "text": "{sidebar}"},
    ]
)

# --- 卡片网格（多人物/多地标/多产品）---
LAYOUTS["grid_cards"] = LayoutTemplate(
    name="卡片网格", category="grid",
    description="2-4列卡片网格，适合展示并行信息（人物/地标/产品/特征）",
    elements=[
        {"type": "text", "x": 0, "y": 15, "w": 960, "h": 55, "text": "{title}", "fs": 44, "color": "primary", "bold": True, "align": 2},
        {"type": "line", "x": 350, "y": 72, "w": 260, "h": 3, "color": "secondary"},
        {"type": "grid_cards", "x": 25, "y": 100, "cols": 4, "rows": 2, "gap_x": 20, "gap_y": 200, "item_w": 220, "item_h": 190,
         "fields": ["{name}", "{period}", "{desc}"],
         "styles": [{"fs": 22, "color": "primary", "bold": True, "align": 2},
                    {"fs": 12, "color": "gray", "align": 2},
                    {"fs": 12, "color": "dark", "align": 2}],
         "decorations": [{"type": "circle_avatar", "x_offset": 70, "y_offset": 15, "size": 80}]},
    ]
)

# --- 四象限（对比/分类）---
LAYOUTS["quadrant"] = LayoutTemplate(
    name="四象限", category="grid",
    description="2x2 四象限对比布局，适合分类展示",
    elements=[
        {"type": "text", "x": 0, "y": 10, "w": 960, "h": 55, "text": "{title}", "fs": 44, "color": "primary", "bold": True, "align": 2},
        {"type": "line", "x": 350, "y": 68, "w": 260, "h": 4, "color": "secondary"},
        {"type": "grid_cards", "x": 25, "y": 95, "cols": 2, "rows": 2, "gap_x": 20, "gap_y": 210, "item_w": 440, "item_h": 195,
         "fields": ["{subtitle}", "{content}"],
         "styles": [{"fs": 24, "color": "white", "bold": True, "bg": "{color}", "h": 52},
                    {"fs": 17, "color": "dark", "y_offset": 60}]},
    ]
)

# --- 数字统计 ---
LAYOUTS["stats"] = LayoutTemplate(
    name="数字统计", category="content",
    description="6大数字统计卡片 + 底部荣誉/说明",
    elements=[
        {"type": "text", "x": 0, "y": 10, "w": 960, "h": 55, "text": "{title}", "fs": 44, "color": "primary", "bold": True, "align": 2},
        {"type": "line", "x": 350, "y": 68, "w": 260, "h": 4, "color": "secondary"},
        {"type": "grid_cards", "x": 20, "y": 120, "cols": 6, "rows": 1, "gap_x": 15, "gap_y": 0, "item_w": 140, "item_h": 120,
         "fields": ["{num}", "{label}"],
         "styles": [{"fs": 34, "color": "white", "bold": True, "align": 2, "bg": "primary"},
                    {"fs": 15, "color": "accent_light", "align": 2}]},
        {"type": "box", "x": 30, "y": 270, "w": 900, "h": 240, "color": "light", "text": "{summary}"},
    ]
)

# --- 三列对比 ---
LAYOUTS["three_col"] = LayoutTemplate(
    name="三列对比", category="column",
    description="三列并排对比，适合三种方案/三个时期/三个角度",
    elements=[
        {"type": "text", "x": 0, "y": 20, "w": 960, "h": 50, "text": "{title}", "fs": 40, "color": "white", "bold": True, "align": 2},
        {"type": "bg", "color": "primary"},
        {"type": "grid_cards", "x": 25, "y": 120, "cols": 3, "rows": 1, "gap_x": 20, "gap_y": 0, "item_w": 290, "item_h": 360,
         "fields": ["{col_title}", "{col_subtitle}", "{col_content}"],
         "styles": [{"fs": 24, "color": "white", "bold": True, "align": 2, "bg": "accent"},
                    {"fs": 16, "color": "accent_light", "align": 2},
                    {"fs": 15, "color": "light_text", "align": 2, "y_offset": 60}]},
    ]
)

# --- 流程/管道 ---
LAYOUTS["pipeline"] = LayoutTemplate(
    name="流程图", category="content",
    description="水平管道流程，带有彩色模块和连接箭头",
    elements=[
        {"type": "text", "x": 0, "y": 15, "w": 960, "h": 55, "text": "{title}", "fs": 42, "color": "primary", "bold": True, "align": 2},
        {"type": "line", "x": 350, "y": 72, "w": 260, "h": 4, "color": "secondary"},
        {"type": "pipeline_items", "x": 35, "y": 100, "count": 6, "gap": 20, "item_w": 140, "item_h": 320,
         "fields": ["{step_num}", "{step_name}", "{step_detail}"],
         "styles": [{"fs": 16, "color": "white", "bold": True, "bg": "{color}", "h": 55},
                    {"fs": 12, "color": "dark", "y_offset": 65, "w": 128, "h": 240}]},
        {"type": "box", "x": 30, "y": 450, "w": 900, "h": 60, "color": "light", "text": "{pipeline_summary}"},
    ]
)

# --- 表格/数据 ---
LAYOUTS["data_table"] = LayoutTemplate(
    name="数据表格", category="content",
    description="左表格 + 右解读，适合排名/对比/指标",
    elements=[
        {"type": "text", "x": 30, "y": 10, "w": 500, "h": 50, "text": "{title}", "fs": 40, "color": "primary", "bold": True},
        {"type": "line", "x": 30, "y": 65, "w": 200, "h": 4, "color": "secondary"},
        {"type": "table", "x": 30, "y": 90, "rows": 7, "cols": 2, "row_h": 42, "col_w": [180, 280],
         "header": ["{col1_name}", "{col2_name}"], "data": "{table_data}"},
        {"type": "box", "x": 530, "y": 90, "w": 400, "h": 410, "color": "light", "text": "{interpretation}"},
    ]
)

# --- 内容+图片 ---
LAYOUTS["content_image"] = LayoutTemplate(
    name="内容+图片", category="image",
    description="左文右图 / 左图右文，图文并茂",
    elements=[
        {"type": "text", "x": 40, "y": 20, "w": 450, "h": 55, "text": "{title}", "fs": 38, "color": "primary", "bold": True},
        {"type": "line", "x": 40, "y": 80, "w": 120, "h": 3, "color": "secondary"},
        {"type": "text", "x": 40, "y": 100, "w": 440, "h": 400, "text": "{content}", "fs": 18, "color": "dark"},
        {"type": "image_placeholder", "x": 510, "y": 60, "w": 420, "h": 440, "text": "{image_label}"},
    ]
)

# --- 结语 ---
LAYOUTS["closing"] = LayoutTemplate(
    name="结语", category="close",
    description="深色全屏 + 总结 + 联系方式/校训",
    elements=[
        {"type": "bg", "color": "primary"},
        {"type": "line", "x": 0, "y": 0, "w": 960, "h": 15, "color": "secondary"},
        {"type": "text", "x": 0, "y": 80, "w": 960, "h": 100, "text": "{summary_title}", "fs": 52, "color": "white", "bold": True, "align": 2},
        {"type": "line", "x": 280, "y": 200, "w": 400, "h": 4, "color": "white"},
        {"type": "text", "x": 60, "y": 230, "w": 840, "h": 200, "text": "{summary_text}", "fs": 18, "color": "light_text", "align": 2},
        {"type": "line", "x": 280, "y": 450, "w": 400, "h": 4, "color": "white"},
        {"type": "text", "x": 0, "y": 470, "w": 960, "h": 50, "text": "{motto}", "fs": 30, "color": "accent_light", "bold": True, "align": 2},
        {"type": "line", "x": 0, "y": 530, "w": 960, "h": 8, "color": "secondary"},
    ]
)


# ============================================
# 演讲类型 → 推荐页面序列
# ============================================

TALK_PRESETS = {
    "conference": {  # 学术会议 12-20 页
        "name": "学术会议",
        "slides": ["cover", "toc", "overview", "timeline", "quadrant",
                    "grid_cards", "stats", "pipeline", "data_table",
                    "content_image", "quadrant", "timeline", "stats", "closing"],
        "rules": {"max_slides": 20, "visual_ratio": 0.65, "key_findings": 2}
    },
    "business": {  # 商务汇报
        "name": "商务汇报",
        "slides": ["cover", "toc", "overview", "stats", "three_col",
                    "pipeline", "grid_cards", "data_table", "closing"],
        "rules": {"max_slides": 15, "visual_ratio": 0.5}
    },
    "defense": {  # 论文答辩 45-65 页
        "name": "论文答辩",
        "slides": ["cover", "toc", "overview", "timeline", "quadrant",
                    "content_image", "pipeline", "data_table", "stats",
                    "quadrant", "timeline", "stats", "closing"],
        "rules": {"max_slides": 65, "visual_ratio": 0.6}
    },
    "school": {  # 学校/机构介绍
        "name": "学校介绍",
        "slides": ["cover", "toc", "overview", "timeline", "three_col",
                    "grid_cards", "quadrant", "stats", "closing"],
        "rules": {"max_slides": 14, "visual_ratio": 0.55}
    },
}
