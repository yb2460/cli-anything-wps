# cli-anything-wps

<h3 align="center">AI Agent 工具集 —— WPS Office 操控 + Zotero 学术研究</h3>

<p align="center">
  <img src="https://img.shields.io/badge/平台-Windows-blue?logo=windows" alt="Platform">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/协议-MIT-green" alt="License">
</p>

---

## 包含项目

### 1. cli-anything-wps — WPS / Microsoft Office 操控

47 个 CLI 命令，通过 COM 自动化接口操控 WPS Office 或 Microsoft Office（Word/Excel/PowerPoint）。

```bash
pip install git+https://github.com/yb2460/cli-anything-wps.git
```

- **Writer**: 段落/标题/列表/表格/图片/查找替换/字体样式
- **Calc**: 工作表管理/单元格读写/公式/合并/批量填充
- **Impress**: 幻灯片增删改/文本框/形状/背景/导出
- **导出**: DOCX/XLSX/PPTX/PDF/TXT/HTML/CSV/RTF
- **PPT 设计系统**: 4 套预设 + 14 种布局 + 5 维度质量审查

### 2. cli-anything-zotero — 学术研究智能体

文献管理 + 27 个学术 Skill 集成。写综述、写论文、审稿、做图表一站式。

```bash
cli-anything-zotero skills list                    # 列出所有学术 Skill
cli-anything-zotero skills pipeline original_article  # 论著推荐流程
cli-anything-zotero skills pipeline meta_analysis     # Meta分析流程
cli-anything-zotero skills journal "Nature"           # 期刊图表规范
```

**7 大 Skill 分类:**

| 分类 | Skill 数 | 能力 |
|------|---------|------|
| search | 3 | 快速检索 / 系统评价 / 深度文献搜索 |
| research | 4 | 创意生成 / 头脑风暴 / 假设 / 深度研究 |
| writing | 5 | 写论文 / IMRAD稿件 / 引用 / 大纲 / 修改 |
| review | 5 | 5人审稿 / 同行评审 / 七轮对抗 / 引用验证 |
| visualization | 4 | 幻灯片 / 示意图 / 海报 / 期刊图表 |
| analysis | 3 | 探索分析 / 统计 / 证据评估 |
| pipeline | 2 | 完整学术流水线 / 研究到论文 |

---

## 快速上手

```bash
# WPS 办公
cli-anything-wps document new --type impress --name "演示"
cli-anything-wps preset apply academic --talk-type defense
cli-anything-wps export render output.pptx -p pptx

# Zotero 学术
cli-anything-zotero skills pipeline thesis
cli-anything-zotero catalog search "machine learning"
```

## 系统要求

- Windows 10/11
- WPS Office 2019+ 或 Microsoft Office 2016+ / Zotero 7+
- Python 3.10+
- pywin32

> COM 接口与 Microsoft Office VBA 兼容。如需操控 MS Office，将 ProgID 改为 `PowerPoint.Application` / `Word.Application` / `Excel.Application` 即可。

## 许可证

MIT
