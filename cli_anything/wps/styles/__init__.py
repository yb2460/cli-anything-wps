"""WPS PPT 风格系统 —— 整合 4 个 Skill 的设计精华。

来源：
  - pptx: 大纲→PPT生成、图表表格、自定义母版
  - pptx-from-layouts: 59种布局模板、咨询级排版
  - scientific-slides: 学术风格、视觉优先、演讲类型适配
  - slide-excellence: 质量审查、多维度评分

用法:
  from cli_anything.wps.styles import DesignPreset, LayoutTemplate, apply_style
  preset = DesignPreset("academic")
  template = LayoutTemplate("conference")
  apply_style(slide, preset, template)
"""
from .design_presets import DesignPreset, PRESETS
from .layout_templates import LayoutTemplate, LAYOUTS
from .quality_checks import validate_slide
