# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

---

## 用户环境配置 (User Environment)

| 配置项 | 值 | 说明 |
|--------|-----|------|



## 语言要求
- 所有回答、思考、代码注释、文档、分析都必须使用中文
- 代码中的变量名、函数名可以使用英文，但注释和文档字符串必须用中文
- 如果用户输入英文，回答仍用中文

---

## 1. Think Before Coding (三思而后码)

**不要假设。不要隐藏困惑。暴露权衡。**

实施前：
- 明确陈述假设。如果不确定，**提问**。
- 如果存在多种解释，**全部呈现**——不要默默选择。
- 如果存在更简单的方法，**说出来**。必要时提出反对意见。
- 如果有不清楚的地方，**停下来**。指出困惑之处。**提问**。

### 科研场景特殊要求
- **数据敏感性**：处理 UKB、TCGA 等人类遗传数据时，注意隐私合规与数据使用协议
- **结果可复现性**：随机种子固定、版本号记录、环境导出（`pip freeze > requirements.txt`）
- **统计严谨性**：P值、置信区间、多重检验校正（FDR/Bonferroni）必须明确标注
- **临床相关性**：生物信息学结果必须关联临床意义，避免纯算法炫技

---

## 2. Simplicity First (极简优先)

**最小代码解决问题。不臆测。**

- 不添加超出要求的特性。
- 单次使用代码不做抽象。
- 不添加未被要求的"灵活性"或"可配置性"。
- 不为不可能的场景写错误处理。
- 如果写了200行但可以50行解决，**重写**。

问自己："资深工程师会说这过度复杂吗？" 如果是，简化。

### 科研代码规范
- **Python 绘图**：使用 `plt.rcParams` 统一字体设置，中文用 SimHei/Arial，不修改系统字体配置
- **R 脚本**：开头设置 `options(encoding = "UTF-8")`，保存时选择 UTF-8 编码
- **文件路径**：使用 `os.path.join()` 或 `pathlib.Path`，避免硬编码 Windows 反斜杠
- **批量处理**：CSV 文件用循环 + 函数封装，拒绝复制粘贴重复代码
- **输出格式**：图表保存为 `.svg` 或 `.pdf`（矢量），PPT/Word 用 `python-pptx`/`python-docx` 直接生成

---

## 3. Surgical Changes (精准手术)

**只碰必须碰的。只清理自己制造的混乱。**

编辑现有代码时：
- 不要"改进"相邻代码、注释或格式。
- 不要重构没坏的东西。
- 匹配现有风格，即使你倾向不同做法。
- 如果发现无关的死代码，**提及它**——但不要删除。

当你的改动产生孤儿代码时：
- 删除**你的改动**导致未使用的 import/变量/函数。
- 不要删除预先存在的死代码，除非被要求。

检验标准：每一行改动都应直接追溯到用户的请求。

### 科研代码编辑纪律
- **TCGA/GEO 分析脚本**：修改差异表达分析部分时，不动数据预处理管道
- **可视化代码**：调整 Figure 1 的配色方案时，不改动 Figure 2-6 的代码结构
- **UKB 数据清洗**：修正某一字段提取逻辑时，不影响其他 1128 例患者的处理流程
- **R 与 Python 混用**：保持各自语言习惯，R 用 `<-` 赋值，Python 用 `=`，不混用风格

---

## 4. Goal-Driven Execution (目标驱动执行)

**定义成功标准。循环验证直到通过。**

将任务转化为可验证目标：
- "添加验证" → "为无效输入编写测试，然后使其通过"
- "修复 bug" → "编写复现 bug 的测试，然后使其通过"
- "重构 X" → "确保重构前后测试都通过"

多步骤任务时，陈述简要计划：
```
1. [步骤] → 验证: [检查点]
2. [步骤] → 验证: [检查点]
3. [步骤] → 验证: [检查点]
```

强成功标准让你能独立循环。弱标准（"让它工作"）需要不断澄清。

### 科研任务验证清单
| 任务类型 | 验证标准 |
|---------|---------|
| **TCGA 数据下载** | 样本数匹配（如 STAD 449 例），基因数 19938，文件编码 UTF-8 |
| **差异表达分析** | 火山图显著基因数合理，热图聚类与临床分组一致，GO/KEGG 富集有意义 |
| **生存分析** | Kaplan-Meier 曲线分离明显，Log-rank P < 0.05，C-index > 0.6 |
| **免疫分析** | 免疫检查点表达趋势与文献一致，TIDE/MSI 评分分布合理 |
| **药物敏感性** | oncoPredict 输出矩阵维度正确，IC50 值范围合理 |
| **可视化输出** | 矢量图放大不模糊，字体 ≥ 8pt，符合 Cancer Cell 投稿要求 |
| **Word/PPT 生成** | 文件可直接打开，格式正确，图片嵌入成功，无需二次转化 |
| **UKB 数据提取** | 字段编码与 UKB Showcase 一致，缺失值比例合理，数据类型正确 |

---

## 5. 中文与编码规范 (Encoding Standards)

**所有文本输出必须正确处理中文。**

- **RStudio**：`Tools → Global Options → Code → Saving → Default text encoding → UTF-8`
- **Python**：文件头添加 `# -*- coding: utf-8 -*-`，open() 函数指定 `encoding='utf-8'`
- **CSV 文件**：读写时显式指定 `encoding='utf-8-sig'`（带 BOM，Excel 兼容）
- **PowerShell/Bash**：Windows 中文环境注意 GBK/UTF-8 转换，必要时使用 `chcp 65001`
- **Claude Code 终端**：如遇编码乱码，优先检查终端编码设置，不盲目重试

---

## 6. 科研数据安全 (Data Safety)

**数据是科研生命线，宁可慢不可丢。**

- **原始数据**：永远保留只读副本，分析输出到独立目录
- **中间结果**：定期备份，重要节点（如差异表达结果）保存为 `.rds` 或 `.pkl`
- **代码版本**：使用 Git 管理，关键分析节点打 tag
- **随机性控制**：设置 `random_state` / `set.seed()`，确保结果可复现
- **大文件处理**：UKB 等大数据用分块读取（`pandas.read_csv(chunksize=...)`），避免内存溢出

---

## 7. 可视化质量标准 (Visualization Quality)

**Cancer Cell / Cancer Discovery 级别的图。**

- **分辨率**：矢量格式（SVG/PDF/EPS），位图至少 300 DPI
- **字体**：Arial 或 Helvetica，中文用 SimHei，字号 ≥ 8pt（图中），≥ 12pt（图注）
- **配色**：使用专业配色方案（如 Nature/Science 推荐色板），避免默认彩虹色
- **图层**：使用 BioRender 或 Python 分层绘制，确保可编辑性
- **标注**：统计显著性标记清晰（* P<0.05, ** P<0.01, *** P<0.001），误差线明确
- **一致性**：Figure 1-6 风格统一，坐标轴、图例、标题格式一致

---

## 8. 文档输出规范 (Document Output)

**直接可用的文件，拒绝中间格式。**

- **Word 文档**：使用 `python-docx` 生成，包含标题样式、页眉页脚、参考文献格式
- **PPT 演示**：使用 `python-pptx` 生成，每页布局清晰，加入南方科技大学 + 中国医学科学院肿瘤医院标识
- **PDF 输出**：Word/PPT 直接导出，或 Python 用 `reportlab` 生成
- **CSV/Excel**：使用 `pandas.to_csv()` / `openpyxl`，表头中文注释，数据类型正确
- **拒绝**：Markdown 中间文件、需要二次转化的格式、无法直接打开的附件

---

## 9. 错误处理与调试 (Error Handling)

**报错时先定位，不盲目重试。**

- **Python 报错**：从上到下阅读 Traceback，定位最后一行实际错误，不只看最后一行
- **R 报错**：检查包版本兼容性，特别是 Bioconductor 包与 R 版本匹配
- **编码错误**：先确认文件实际编码（用 `file -i` 或 Python `chardet`），再决定如何读取
- **内存错误**：大数据分块处理，或使用南方科技大学超算中心资源
- **ModuleNotFoundError**：确认包名拼写正确（如 `oncoPredict` 不是 `oncopredict`），优先用 `pip install`
- **权限错误**：Windows 下以管理员运行 PowerShell，或修改文件夹权限

---

## 10. 与 AI 协作规范 (AI Collaboration)

**明确需求，迭代优化，保持主导。**

- **需求描述**：提供完整上下文（数据维度、目标期刊、时间要求），避免"帮我分析一下"这类模糊指令
- **迭代模式**：生成 → 检查 → 修正 → 扩展，用"继续"推进长文本生成
- **代码审查**：AI 生成的代码必须人工检查，特别是文件路径、数据索引、统计方法
- **事实核查**：文献引用、数据集样本数、基因名等精确信息必须人工核对原始材料
- **记忆使用**：AI 记忆功能可在设置中关闭（设置 → 个性化 → 记忆空间），用户完全可控
- **角色设定**：可要求 AI 扮演"20年经验资深科学家"、"专业简历顾问"等角色，但需明确边界

---

## 11. 公众号文章排版工作流 (WeChat Article Formatting Workflow)

**触发条件：** 用户要求写公众号推文、微信排版、公众号文章，或提到"排版""公众号格式""微信格式"。

### 强制流程

每次公众号文章任务，**必须依次执行以下全部步骤**：

#### 第 1 步：撰写文章 Markdown
- 先搜索调研（如需），再撰写完整 Markdown 文章
- 文章结构清晰：`##` 大标题 + `###` 小标题 + 表格 + 列表 + callout 提示框
- 保存为 `.md` 文件到目标文件夹

#### 第 2 步：生成 Gallery 模式（自动调节风格）

**这是核心步骤。必须使用 `--gallery` 模式。**

```bash
PYTHONIOENCODING=utf-8 "D:/A-ryuyanwenku/Python/python.exe" \
  "C:/Users/杨兵/.claude/skills/xiaohu-wechat-format-main/scripts/format.py" \
  --input "文章.md" \
  --gallery \
  --output "输出目录/gallery" \
  --no-open \
  --format wechat \
  --recommend <根据内容推荐2-4个主题>
```

**⚠️ 关键：Windows 中文环境必须加 `PYTHONIOENCODING=utf-8` 前缀，否则脚本 GBK 编码报错。**

#### 第 2.5 步（可选）：生成单独主题精排版
如果用户明确只需要某个主题，跳过 gallery：
```bash
PYTHONIOENCODING=utf-8 "D:/A-ryuyanwenku/Python/python.exe" \
  "C:/Users/杨兵/.claude/skills/xiaohu-wechat-format-main/scripts/format.py" \
  --input "文章.md" \
  --theme <主题名> \
  --output "输出目录/<主题名>" \
  --no-open \
  --format wechat
```

### 主题推荐规则

| 文章类型 | 推荐主题（--recommend） |
|---------|----------------------|
| AI工具/科技教程 | github bytedance sspai |
| 深度分析/综述 | newspaper magazine ink |
| 科研/学术 | sspai newspaper bytedance |
| 开发者/编程 | github bytedance midnight |
| 访谈/对话 | terracotta coffee-house mint-fresh |
| 文艺/随笔 | terracotta sunset-amber lavender-dream |

### Gallery 输出结构

脚本生成后，**必须把 gallery.html 复制到文章根目录**（方便直接找到）：
```
文章所在文件夹/
├── 文章名.md                          ← 原始 Markdown
├── 文章名-Gallery主题选择.html         ← 23 主题实时切换预览页（根目录）
└── output/
    ├── gallery/.../gallery.html       ← 脚本原始输出（保留）
    ├── github/.../preview.html        ← 单独主题精排版
    └── ...
```

### 使用方式
1. 浏览器打开 `gallery.html`
2. 顶部点主题按钮实时切换预览
3. 选中满意主题后，点「用这个风格排版」
4. 一键复制到剪贴板
5. 粘贴到公众号后台编辑器

### 技能位置
- Skill 目录：`C:\Users\杨兵\.claude\skills\xiaohu-wechat-format-main\`
- 排版脚本：`scripts/format.py`
- 配置文件：`config.json`（output_dir, vault_root, wechat 等）
- 已有依赖：`markdown` Python 包已安装

---

## 12. WPS PPT 自动生成工作流 (WPS PPT Automation)

**触发条件：** 用户要求制作 PPT、生成演示文稿、做幻灯片，且明确提到"操作WPS"或"打开WPS"。

### 核心架构

通过 **WPS COM 自动化**（`win32com.client.Dispatch("KWPP.Application")`）直接操控 WPS 演示，满版大字体设计。

```
搜索资料 → 整理内容结构 → Python COM 脚本 → WPS 可见生成 → 保存 PPTX + PDF
```

### 强制模板代码

每次生成 PPT 必须使用以下模板，只需替换**幻灯片内容**部分：

```python
# -*- coding: utf-8 -*-
"""PPT生成脚本 —— WPS COM 自动化。"""
import os, pythoncom, win32com.client

OUT = r"D:\A-资料\A-claudewenjian\PPT制作"
W, H = 960, 540  # 16:9 画布

# 品牌色（根据主题调整）
BLUE  = 0x954801   # #015495
RED   = 0x3333CC
WHITE = 0xFFFFFF; DARK = 0x2D2D30; GRAY = 0x999999; LGRAY = 0xF2F4F7

def c(r,g,b): return (b<<16)|(g<<8)|r

def run():
    pythoncom.CoInitialize()
    app = win32com.client.Dispatch("KWPP.Application")
    app.Visible = True   # 可见模式
    ppt = app.Presentations.Add()
    idx = [1]

    def slide():
        s = ppt.Slides.Add(idx[0], 12)  # ppLayoutBlank=12
        idx[0] += 1; return s

    def bg(s, color):
        try: s.FollowMasterBackground = False
        except: pass
        s.Background.Fill.ForeColor.RGB = color
        s.Background.Fill.Visible = True

    def box(s, x, y, w, h, color, text="", fs=18, tc=WHITE, bold=True, align=2):
        """圆角矩形 + 文字"""
        r = s.Shapes.AddShape(5, x, y, w, h)  # 5=圆角矩形
        r.Fill.ForeColor.RGB = color; r.Fill.Visible = True
        r.Line.Visible = False
        if text:
            t2 = r.TextFrame.TextRange; t2.Text = text
            t2.Font.Size = fs; t2.Font.Color = tc; t2.Font.Name = "微软雅黑"
            t2.Font.Bold = bold; t2.ParagraphFormat.Alignment = align
        return r

    def txt(s, x, y, w, h, text, fs=18, color=DARK, bold=False, align=1, font="微软雅黑"):
        """文本框。align: 1=左 2=中 3=右"""
        t = s.Shapes.AddTextbox(1, x, y, w, h)
        tr = t.TextFrame.TextRange; tr.Text = text; tr.Font.Size = fs
        tr.Font.Color = color; tr.Font.Name = font; tr.Font.Bold = bold
        tr.ParagraphFormat.Alignment = align
        return t

    def line(s, x, y, w, h, color):
        r = s.Shapes.AddShape(1, x, y, w, h)
        r.Fill.ForeColor.RGB = color; r.Fill.Visible = True
        r.Line.Visible = False; return r

    # ═══════════════ 幻灯片内容（替换此部分） ═══════════════
    # S1 封面示例
    s1 = slide(); bg(s1, c(26,60,139))  # 深蓝全屏
    line(s1, 0, 0, W, 18, c(230,119,51))  # 顶部装饰线
    txt(s1, 0, 100, W, 150, "标题大字\n副标题", fs=72, color=WHITE, bold=True, align=2)
    line(s1, 280, 270, 400, 5, WHITE)  # 分隔线
    txt(s1, 0, 365, W, 60, "校训/标语", fs=32, color=c(230,180,140), bold=True, align=2)
    # ... 更多幻灯片 ...

    # ═══════════════ 保存 ═══════════════
    pptx = os.path.join(OUT, "演示文稿.pptx")
    os.makedirs(OUT, exist_ok=True)
    ppt.SaveAs(pptx)
    print(f"PPTX: {os.path.getsize(pptx):,} 字节")
    pdf = os.path.join(OUT, "演示文稿.pdf")
    ppt.SaveAs(pdf, 32)  # 32=ppSaveAsPDF
    print(f"PDF: {os.path.getsize(pdf):,} 字节")
    ppt.Close(); app.Quit()
    print("完成")

if __name__ == "__main__":
    run()
```

### 设计规范（满版大字体风格）

| 元素 | 规范 |
|------|------|
| **画布** | 960×540 pt (16:9)，所有坐标以此为基准 |
| **封面标题** | 72pt，居中，白色粗体 |
| **页面标题** | 40-48pt，深色粗体，顶部居中 |
| **正文** | 16-20pt，深灰色 #333 |
| **卡片标题** | 22-26pt，白色粗体 |
| **装饰线** | 3-5pt 高，品牌色或白色 |
| **最小字号** | 12pt（脚注），14pt（说明文字） |
| **内容密度** | 每页 3-6 个信息块，留白充足 |
| **配色** | 1 主色 + 1 辅色 + 白/深灰，不超过 4 色 |

### 14 页标准结构

```
S1  封面（深色全屏 + 大字标题 + 装饰线）
S2  目录（编号圆角方块 + 6 项导航）
S3  概览（信息卡片 + 荣誉侧栏）
S4-7 核心内容（时间轴/卡片/对比布局）
S8  特色亮点（图文卡片网格）
S9-10 数据展示（数字统计 + 排名表）
S11-12 深度内容（四象限/流程图）
S13 特色模式详解
S14 结语（深色全屏 + 总结 + 校训）
```

### 常用布局模式

```python
# 模式1：时间轴（左侧圆点+竖线+右侧事件）
for i, (date, event) in enumerate(events):
    y = 168 + i * 65
    box(s, 40, y, 20, 20, BLUE)
    if i < len(events)-1: line(s, 49, y+20, 2, 45, BLUE)
    txt(s, 75, y-5, 140, 30, date, fs=18, color=BLUE, bold=True)
    txt(s, 230, y-5, 500, 30, event, fs=18, color=DARK)

# 模式2：四象限卡片
for i, (title, desc, color) in enumerate(quads):
    x = 25 + (i%2)*470; y = 95 + (i//2)*210
    box(s, x, y, 440, 52, color, title, fs=24, tc=WHITE)
    txt(s, x+15, y+60, 410, 130, desc, fs=17, color=DARK)

# 模式3：6 大数字统计
for i, (num, label) in enumerate(numbers):
    x = 20 + i*155
    box(s, x, 135, 140, 110, BLUE)
    txt(s, x, 145, 140, 50, num, fs=34, color=WHITE, bold=True, align=2)
    txt(s, x, 200, 140, 30, label, fs=15, color=c(160,200,240), align=2)

# 模式4：名人卡片（头像圆+名字+简介）
for i, (name, period, desc, color) in enumerate(people):
    x = 25 + (i%4)*232; y = 110 + (i//4)*200
    box(s, x, y, 210, 180, c(245,248,252))
    box(s, x+65, y+15, 80, 80, color, name[0], fs=36, tc=WHITE)
    txt(s, x, y+95, 210, 35, name, fs=20, color=color, bold=True, align=2)
    txt(s, x, y+148, 210, 30, desc, fs=11, color=DARK, align=2)
```

### 执行步骤

1. **搜索资料**：`WebSearch` 搜索主题资料，提取关键时间/人物/数据
2. **规划结构**：列出 14 页标题和每页内容要点
3. **编写脚本**：基于上述模板，替换幻灯片内容部分
4. **清理进程**：`taskkill //F //IM wps.exe //T 2>nul; taskkill //F //IM wpp.exe //T 2>nul`
5. **运行脚本**：`"D:/A-ryuyanwenku/Python/python.exe" "脚本.py"`
6. **验证输出**：确认 PPTX 和 PDF 文件大小合理（PPTX 100-150KB, PDF 350-500KB）

### COM 常见坑

| 问题 | 原因 | 解决 |
|------|------|------|
| `Fill.ForeColor = color` 报错 | WPS 需要 `.RGB` 属性 | 改用 `Fill.ForeColor.RGB = color` |
| `SetStyle` 报错 | WPS 不支持 Word 的 SetStyle | 用 `OutlineLevel` + 手动字体格式 |
| `ExportAsFixedFormat` 失败 | 第二个参数类型不匹配 | 用 `SaveAs(path, 32)` 代替 |
| `app.Quit()` 报错 | COM 对象已释放 | 忽略，不影响文件保存 |
| 中文输出乱码 | GBK 编码问题 | 脚本内不输出中文 emoji |
| PS 进程残留 | 上次未正常退出 | 每次运行前 `taskkill` |

### 输出规范

- **PPTX**：直接可编辑，保留所有形状和文本框
- **PDF**：便于预览和分享
- 文件命名：`{主题}-{副标题}.pptx`
- 同时生成 PPTX + PDF 双格式

### 触发词映射

| 用户输入 | 对应主题色 |
|---------|----------|
| 华中科技大学 | 蓝 #015495 + 红 #CC3333 |
| 南方科技大学 | 深蓝 #1A3C8B + 橙 #E67733 |
| 其他学校/机构 | 搜索其官方 VI 色或使用深蓝+金 |

---

**这些指南有效的标志：** diff 中不必要的改动更少，因过度复杂导致的重写更少，澄清问题出现在实施前而非犯错后。
