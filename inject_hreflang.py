#!/usr/bin/env python3
"""给所有英文 HTML 页面注入 hreflang 标签"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

HREFLANG = """  <link rel="alternate" hreflang="en" href="https://monkeymarthub.com/" />
  <link rel="alternate" hreflang="es" href="https://monkeymarthub.com/es/" />
  <link rel="alternate" hreflang="pt" href="https://monkeymarthub.com/pt/" />
  <link rel="alternate" hreflang="fr" href="https://monkeymarthub.com/fr/" />
  <link rel="alternate" hreflang="de" href="https://monkeymarthub.com/de/" />
  <link rel="alternate" hreflang="x-default" href="https://monkeymarthub.com/" />"""

# 只处理根目录下的英文 HTML 文件
EN_FILES = [
    "index.html",
    "how-to-play-monkey-mart.html",
    "monkey-mart-tips.html",
    "monkey-mart-unblocked.html",
    "monkey-mart-unblocked-6x.html",
    "monkey-mart-unblocked-76.html",
    "monkey-mart-2.html",
    "monkey-mart-cheats.html",
    "monkey-mart-all-items.html",
    "monkey-mart-how-to-get-more-monkeys.html",
]

updated = []
skipped = []

for fname in EN_FILES:
    path = os.path.join(BASE, fname)
    if not os.path.exists(path):
        skipped.append(fname)
        continue
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    # 已有 hreflang 则跳过
    if 'hreflang' in content:
        skipped.append(f"{fname} (already has hreflang)")
        continue
    # 在 </head> 前插入
    new_content = content.replace("</head>", f"{HREFLANG}\n</head>", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated.append(fname)

print(f"✅ 注入完成！更新 {len(updated)} 个文件：")
for f in updated:
    print(f"  {f}")
if skipped:
    print(f"\n⏭ 跳过 {len(skipped)} 个：")
    for f in skipped:
        print(f"  {f}")
