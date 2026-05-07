# 05 滑动窗口

## 核心思路

**触发器**：题面包含「**子数组 / 子串**」（连续）+ 「最长 / 最短 / 满足某条件」→ 直接套滑动窗口。

整体框架是一个**双指针同向移动**的循环：
- right 不断右移，扩大窗口（吸纳新字符 / 元素）
- 当窗口"违反约束"时，left 收缩，直到约束恢复
- 在每个合法窗口处更新答案

关键问题是：**如何 O(1) 维护窗口状态**？通常用：
- 哈希表 / Counter（窗口内字符计数）
- 一个整数（窗口和、不同字符数）
- 单调队列（窗口最大/最小值）

## 通用模板（必背）

```python
def sliding_window(s, t):
    from collections import Counter
    need = Counter(t)
    have: dict[str, int] = {}
    valid = 0           # 满足 need 中字符的种数
    left = 0
    ans = ...
    for right, ch in enumerate(s):
        # 1. 把 ch 加入窗口
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            valid += 1

        # 2. 当窗口违反约束（或可以收缩取最优时），收缩左边界
        while window_should_shrink():
            # 在收缩前，对"恰好合法的窗口"更新答案（最短型）
            ans = update_min(ans, right - left + 1)
            lch = s[left]
            if lch in need and have[lch] == need[lch]:
                valid -= 1
            have[lch] -= 1
            left += 1

        # 3. 对"扩张时合法的窗口"更新答案（最长型）
        ans = update_max(ans, right - left + 1)
    return ans
```

**最长型 vs 最短型** 的关键区别在更新答案的时机：
- **最长**：窗口合法时更新（收缩之后更新）
- **最短**：窗口刚刚开始合法（一收缩就违反）时更新

## 三种典型形态

### 1) 最长无重复子串（最长型，char 种类约束）

```python
def length_of_longest_substring(s: str) -> int:
    last = {}            # ch -> last seen index
    left = ans = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        ans = max(ans, right - left + 1)
    return ans
```

### 2) 最小覆盖子串（最短型，覆盖 t 的所有字符）

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    need = Counter(t)
    have = {}
    valid = 0
    left = 0
    best_l, best_len = 0, float('inf')
    for right, ch in enumerate(s):
        have[ch] = have.get(ch, 0) + 1
        if ch in need and have[ch] == need[ch]:
            valid += 1
        while valid == len(need):
            if right - left + 1 < best_len:
                best_l, best_len = left, right - left + 1
            lch = s[left]
            if lch in need and have[lch] == need[lch]:
                valid -= 1
            have[lch] -= 1
            left += 1
    return "" if best_len == float('inf') else s[best_l:best_l + best_len]
```

### 3) 定长窗口（找异位词）

```python
def find_anagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p): return []
    need = [0] * 26
    have = [0] * 26
    for ch in p:
        need[ord(ch) - ord('a')] += 1
    res = []
    for i, ch in enumerate(s):
        have[ord(ch) - ord('a')] += 1
        if i >= len(p):                                   # 窗口超长，左端弹出
            have[ord(s[i - len(p)]) - ord('a')] -= 1
        if have == need:
            res.append(i - len(p) + 1)
    return res
```

## 易错点

- **`Counter` 比较**：`Counter(a) == Counter(b)` 可以直接判等；但 26 数组对比更快。
- **滑动方向**：left 永远只前进、不后退（这是 O(n) 的来源）。
- **valid 计数语义**：是「**满足 need 的字符种数**」，不是字符总数。
- **最短型循环条件**：`while valid == len(need)`（恰好覆盖时持续收缩）。

## 高频题

1. #3 无重复字符的最长子串 ★
2. #76 最小覆盖子串 ★（最短型模板）
3. #438 找到字符串中所有字母异位词 ★（定长）
4. #567 字符串的排列（定长）
5. #209 长度最小的子数组（最短型，数值和约束）
6. #239 滑动窗口最大值 ★（→ 单调队列）
7. #1004 最大连续 1 的个数 III（最多 K 个 0）
8. #1052 爱生气的书店老板（定长）
