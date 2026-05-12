# 国内大厂算法面试刷题路线（Python）

针对字节 / 阿里 / 腾讯 / 美团 / 快手 / 京东等国内大厂面试。专题分类参考 labuladong 体系，题目优先 LeetCode Hot 100。

**题量**：~168 题 = 🔥 100 Hot 100（主刷，在 16 个专题目录里） + 📚 68 labuladong 扩展（二刷，在 [`_labuladong_ext/`](_labuladong_ext/)）。
**一刷只刷 Hot 100**，扩展放着等以后回头加深。

---

## 学习顺序与依赖

> 箭头表示「最好先掌握」。专题内部题目按难度递增，外层按依赖递进。

### 阶段一 · 数据结构基础（约 2–3 周）
- [01 数组与字符串](01_array_string/NOTES.md) → [04 双指针](04_two_pointers/NOTES.md) → [05 滑动窗口](05_sliding_window/NOTES.md)
- [02 链表](02_linked_list/NOTES.md) → [04 双指针](04_two_pointers/NOTES.md)
- [03 二叉树](03_binary_tree/NOTES.md) ★ **核心思维，必须吃透**

### 阶段二 · 算法范式（约 4–5 周）
- [06 二分查找](06_binary_search/NOTES.md)
- [07 DFS / BFS](07_dfs_bfs/NOTES.md)（建立在 03 二叉树之上）
- [08 回溯](08_backtracking/NOTES.md)（DFS 的特化）
- [09 动态规划](09_dp/NOTES.md) ★ **投入最大的专题**
- [10 贪心](10_greedy/NOTES.md)（与 09 对比理解）

### 阶段三 · 专题进阶（约 2–3 周）
- [11 单调栈 / 单调队列](11_monotonic_stack/NOTES.md)
- [12 堆与 TopK](12_heap_topk/NOTES.md)
- [13 并查集](13_union_find/NOTES.md)
- [14 图论](14_graph/NOTES.md)（拓扑 / 最短路 / MST）
- [15 前缀和 / 差分](15_prefix_sum/NOTES.md)
- [16 设计题](16_design/NOTES.md)（LRU / LFU / Trie / 跳表）

---

## 节奏建议（8–10 周方案）

| 周次 | 专题 | 目标题数 |
|---|---|---|
| 1 | 01 数组字符串 + 02 链表 | 25 |
| 2 | 03 二叉树（含 BST） | 25 |
| 3 | 04 双指针 + 05 滑动窗口 | 20 |
| 4 | 06 二分 + 07 DFS/BFS | 20 |
| 5 | 08 回溯 | 15 |
| 6 | 09 DP 第一周（一维 + 背包） | 25 |
| 7 | 09 DP 第二周（二维 + 区间 + 状压） + 10 贪心 | 25 |
| 8 | 11 单调栈 + 12 堆 + 15 前缀和 | 25 |
| 9 | 13 并查集 + 14 图论 | 20 |
| 10 | 16 设计 + 高频复盘 | 20 + 复盘 |

> 重要：**第二轮回看 > 第一轮新刷**。每周末挑出本周做错或耗时超过 30 分钟的题，重做一遍，写到肌肉记忆。

---

## 顶层索引

- [HIGH_FREQ.md](HIGH_FREQ.md) — 高频题清单（Hot 100 主刷 + labuladong 扩展）
- [TIME_TIERS.md](TIME_TIERS.md) — Hot 100 按耗时分档（从 T1 往下刷）
- [_template/](_template/README.md) — 题解模板与使用说明
- [_review/](_review/README.md) — Python 三件套：踩坑 + 简写 + 数据结构 CRUD 速查
- [_labuladong_ext/](_labuladong_ext/) — labuladong 扩展题（二刷再说，一刷别动）

---

## 目录结构

```
leetcode/
├── README.md                # 本文件
├── HIGH_FREQ.md             # 高频题清单（含两区索引）
├── _template/               # 题解模板
├── _review/                 # 踩坑 + Python 简写 + CRUD 速查
├── _labuladong_ext/         # 📚 labuladong 扩展题（二刷再说）
│   ├── 01_array_string/
│   └── ... 同样 16 专题分类
├── 01_array_string/         # 🔥 Hot 100 主刷
│   ├── NOTES.md             # 专题学习笔记（套路 + 模板）
│   └── XXXX_*.py            # Hot 100 题目文件
├── 02_linked_list/ ...
└── 16_design/ ...
```

---

## 使用流程

每个专题目录下已经预置了**一道空白种子题**（题面 + 类签名 + 测试用例都备好，方法体留空）。打开就能写。

1. 选定本周专题，先把 `NOTES.md` 通读一遍，把模板代码默写一遍。
2. 打开该专题下的种子题文件（如 `04_two_pointers/0015_three_sum.py`），直接在 `class Solution` 里写实现。**不看题解先做。** 卡住 25 分钟看 NOTES.md，再卡 10 分钟才看官方题解。
3. 跑 `python 04_two_pointers/0015_three_sum.py`：
   - 全 PASS = 通过
   - 出现 FAIL 加 `AssertionError` 是正常的，说明还没实现完；输出会展示每条用例的 `expected` / `actual` 对比
4. 做完在文件顶部 docstring 的「**复盘要点**」里写两句：哪一步卡住？这题的「触发器」是什么？
5. **新增 HIGH_FREQ.md 里的其它题**：复制 `_template/solution_template.py` 到对应专题目录，重命名为 `<4位题号>_<英文短名>.py`，填好题面 + 测试用例，按 1-4 做。
