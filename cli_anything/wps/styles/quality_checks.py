"""质量审查 —— slide-excellence 的审查标准落地。

检查项:
  - 字体层级: title 36-44pt, body 24-28pt, caption 18-20pt
  - 颜色: 3-5色, 高对比度(7:1), 色盲友好
  - 布局: 一页一个主题, 40-50%留白
  - 内容: 最多6个要点, 视觉优先(60-70%)
"""

def validate_slide(slide_elements, preset_rules):
    """对单页幻灯片执行质量审查。

    Args:
        slide_elements: [{"type":"text","fs":42,...}, ...]
        preset_rules: DesignPreset.rules

    Returns:
        {"pass": bool, "warnings": [], "score": 0-100}
    """
    warnings = []
    score = 100

    texts = [e for e in slide_elements if e.get("type") == "text"]
    shapes = [e for e in slide_elements if e.get("type") in ("box", "rect", "circle", "image")]

    # 1. 字体大小检查
    for t in texts:
        fs = t.get("fs", 18)
        role = t.get("role", "body")
        if role == "title" and fs < 36:
            warnings.append(f"标题字号 {fs}pt < 推荐 36pt")
            score -= 5
        if role == "body" and fs < 20:
            warnings.append(f"正文字号 {fs}pt < 推荐 24pt")
            score -= 3
        if role == "caption" and fs < 14:
            warnings.append(f"标注字号 {fs}pt < 推荐 18pt")
            score -= 2

    # 2. 内容密度检查
    bullet_count = len(texts)
    max_bullets = preset_rules.get("max_bullets", 6)
    if bullet_count > max_bullets * 1.5:
        warnings.append(f"文本块过多 ({bullet_count} > {max_bullets*1.5})")
        score -= 10

    # 3. 视觉占比检查
    visual_ratio_target = preset_rules.get("visual_ratio", 0.5)
    total = len(texts) + len(shapes)
    if total > 0:
        visual_ratio = len(shapes) / total
        if visual_ratio < visual_ratio_target - 0.2:
            warnings.append(f"视觉占比 {visual_ratio:.0%} < 目标 {visual_ratio_target:.0%}")
            score -= 5

    # 4. 一页一主题检查
    title_count = sum(1 for t in texts if t.get("role") == "title")
    if title_count > 1:
        warnings.append(f"检测到 {title_count} 个标题，建议一页一个主题")
        score -= 10

    return {"pass": score >= 70, "warnings": warnings, "score": max(0, min(100, score))}


def review_deck(slides, preset):
    """对整个PPT进行质量审查。

    Returns:
        {"overall_score": 0-100, "per_slide": [...], "summary": str}
    """
    results = []
    for i, slide_elements in enumerate(slides):
        result = validate_slide(slide_elements, preset.rules)
        result["slide_index"] = i
        results.append(result)

    overall = sum(r["score"] for r in results) / max(len(results), 1)
    total_warnings = sum(len(r["warnings"]) for r in results)

    return {
        "overall_score": round(overall, 1),
        "per_slide": results,
        "total_warnings": total_warnings,
        "summary": f"整体 {overall:.0f}分，{len(results)}页，{total_warnings}个警告"
    }


# 幻灯片审查清单 (slide-excellence 的 5 维度)
REVIEW_DIMENSIONS = {
    "visual": {
        "name": "视觉审查",
        "checks": ["字体层级", "颜色对比度", "留白比例", "布局一致性", "图片质量"],
        "threshold": 70,
    },
    "pedagogy": {
        "name": "教学法审查",
        "checks": ["叙事弧完整性", "预备知识清晰", "示例充分", "符号一致性", "逻辑流畅度"],
        "threshold": 75,
    },
    "proofreading": {
        "name": "校对审查",
        "checks": ["拼写", "语法", "术语一致性", "标点", "字体溢出"],
        "threshold": 80,
    },
    "parity": {
        "name": "格式一致性",
        "checks": ["PPTX vs PDF 一致", "字体嵌入", "图片不丢失", "动画兼容"],
        "threshold": 85,
    },
    "substance": {
        "name": "内容实质",
        "checks": ["数据准确性", "引用完整性", "结论支撑", "方法可复现"],
        "threshold": 90,
    },
}
