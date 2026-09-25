#!/usr/bin/env python3
"""
一个可选的轻量辅助脚本：将 JSON 形式的原始要点转换为适合进一步整理的 Markdown 骨架。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: scaffold_from_json.py <input.json>", file=sys.stderr)
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"输入文件不存在: {input_path}", file=sys.stderr)
        return 1

    try:
        data = json.loads(input_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"JSON 解析失败: {exc}", file=sys.stderr)
        return 1

    title = data.get("title", "汇报材料")
    bullets = data.get("bullets", [])

    print(f"# {title}\n")
    print("## 原始要点")
    for item in bullets:
        print(f"- {item}")
    print("\n## 建议结构")
    print("### 一句话概述")
    print("### 背景与目标")
    print("### 关键动作")
    print("### 结果与影响")
    print("### 风险或待解决问题")
    print("### 下一步计划")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
