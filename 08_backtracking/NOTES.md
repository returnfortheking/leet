# 08 回溯

## 核心思路

回溯 = **DFS + 撤销选择**。本质是在一棵"决策树"上做 DFS，到达叶子记录答案，回到父节点撤销刚才的选择。

**触发器**：题面要求「**返回所有满足条件的方案**」，关键字"全部"、"列出所有"、"组合"、"排列"、"子集"、"分割"。

## 通用模板（必背）

```python
def backtrack(path, choices):
    if is_terminal(path):
        result.append(path[:])     # ★ 必须拷贝，path 是引用
        return
    for choice in choices:
        if not valid(choice, path):
            continue
        path.append(choice)         # 做选择
        backtrack(path, next_choices(path, choice))
        path.pop()                  # 撤销选择
```

**三类问题** 的差异只在：
- **子集**：每一步都记录答案（不在叶子才记）
- **组合**：用 `start` 控制下一层从哪开始（避免重复）
- **排列**：用 `used[]` 标记已选元素

## 三大模板

### 1) 子集（#78）

```python
def subsets(nums):
    res, path = [], []
    def bt(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            bt(i + 1)
            path.pop()
    bt(0)
    return res
```

### 2) 组合（#39 组合总和，元素可重用）

```python
def combination_sum(cands, target):
    cands.sort()
    res, path = [], []
    def bt(start, rem):
        if rem == 0:
            res.append(path[:])
            return
        for i in range(start, len(cands)):
            if cands[i] > rem: break        # 剪枝
            path.append(cands[i])
            bt(i, rem - cands[i])           # i 不变 = 可重复用
            path.pop()
    bt(0, target)
    return res
```

### 3) 排列（#46 全排列）

```python
def permute(nums):
    res, path = [], []
    used = [False] * len(nums)
    def bt():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]: continue
            used[i] = True
            path.append(nums[i])
            bt()
            path.pop()
            used[i] = False
    bt()
    return res
```

## 含重复元素的去重

排序后，**同一层**跳过相同元素：

```python
# 排列去重（#47）
for i in range(len(nums)):
    if used[i]: continue
    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
        continue                 # 关键：前一个相同元素未被使用 → 跳过
    ...
```

```python
# 组合去重（#40）
for i in range(start, len(nums)):
    if i > start and nums[i] == nums[i - 1]:
        continue                 # 同一层不再选相同值
    ...
```

## 经典剪枝 / 高难

### 4) 括号生成（#22）

```python
def generate(n):
    res = []
    def bt(s, left, right):
        if len(s) == 2 * n:
            res.append(s); return
        if left < n:
            bt(s + '(', left + 1, right)
        if right < left:                # ★ 关键约束
            bt(s + ')', left, right + 1)
    bt('', 0, 0)
    return res
```

### 5) N 皇后（#51）—— 三对角线集合

```python
def solve_n_queens(n):
    res = []
    cols, diag1, diag2 = set(), set(), set()
    placement = []
    def bt(row):
        if row == n:
            res.append(['.' * c + 'Q' + '.' * (n - c - 1) for c in placement])
            return
        for c in range(n):
            if c in cols or row - c in diag1 or row + c in diag2:
                continue
            cols.add(c); diag1.add(row - c); diag2.add(row + c)
            placement.append(c)
            bt(row + 1)
            cols.remove(c); diag1.remove(row - c); diag2.remove(row + c)
            placement.pop()
    bt(0)
    return res
```

## 易错点（TS → Python）

- **`res.append(path[:])`** 必须拷贝。直接 `res.append(path)` 是引用，最后全是同一个 list。
- **`nonlocal`** 修改外层计数变量必加。
- **集合 `set()` 加减** 比 list `in` 快得多，N 皇后必用 set。
- 排列去重的"前一个相同元素未被使用"条件容易搞反，记口诀：**同层去重，跨层用过的不影响**。

## 高频题

1. #46 全排列 ★
2. #47 全排列 II（去重）★
3. #78 子集 ★
4. #90 子集 II（去重）
5. #39 组合总和 ★
6. #40 组合总和 II（去重）
7. #77 组合
8. #22 括号生成 ★
9. #17 电话号码字母组合
10. #51 N 皇后 ★（一定要刷一次，理解对角线技巧）
11. #79 单词搜索（DFS + 回溯，网格版）
12. #131 分割回文串
13. #93 复原 IP 地址
