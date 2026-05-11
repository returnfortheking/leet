# 复盘 & 速查

三份持续累积的笔记，按使用目的分工：

## 结构

```
_review/
├── README.md              # 本文件，索引
├── pitfalls.md            # ★ 踩过的坑（我写错过的，按主题归类）
├── PYTHON_SHORTCUTS.md    # ★ Python 简便写法（TS 里没有 / 反直觉的语法糖）
└── PYTHON_CHEATSHEET.md   # ★ 数据结构 CRUD 速查（list / dict / set / deque / heap / bisect 等标准操作）
```

三份各司其职：

| 文档 | 回答的问题 | 何时翻 |
|---|---|---|
| `pitfalls.md` | 我**写错**过什么？ | 写到类似场景前回顾，避免再栽 |
| `PYTHON_SHORTCUTS.md` | 我**不知道**有什么简写？ | 想"这段能不能更短"时翻 |
| `PYTHON_CHEATSHEET.md` | 这个**操作怎么写**？ | 忘了 deque/heap/bisect 的 API 时翻 |

## 单题复盘放哪？

不再单独建 `<题号>.md`——会污染题目文件搜索结果。每道题的具体踩坑追加到**该题 `.py` 文件末尾的 `#` 注释块**里，做完题再翻看，避免提前剧透。

## 用法

刷题遇到问题时：

1. **当下**：在该题 `.py` 末尾的注释块里简记现象 + 根因 + 改法。
2. **当周末**：把新根因归类抄进对应文档：
   - 写错 / bug → `pitfalls.md`
   - 不知道的简写技巧 → `PYTHON_SHORTCUTS.md`
   - 新发现的标准 API → `PYTHON_CHEATSHEET.md`
3. **复盘**：翻这三份比翻原题文件高效——同类问题会反复出现，集中归档后才能识别模式。
