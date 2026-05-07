# 01 数组与字符串

## 核心思路

数组/字符串题不是一种"算法"，而是一组**触发条件触发不同套路**的容器：

| 看到题面这种特征 | 立刻想到 |
|---|---|
| 已排序 / 部分有序 | 二分、双指针 |
| 找子数组（连续） | 滑动窗口 / 前缀和 / Kadane |
| 找子序列（不连续） | DP |
| 求 max / min / 第 K | 动态维护 + 单调结构 / 堆 |
| "原地" / "O(1) 空间" | 双指针、两次反转、原地哈希 |
| 字符 ASCII 26 / 128 | 用定长数组当哈希（比 dict 快 3-5 倍）|

## 必背模板

### 1) 原地修改：快慢指针

```python
def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

### 2) 三次反转（轮转数组）

```python
def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k %= n
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
```

### 3) Kadane（最大子数组和）

```python
def max_subarray(nums: list[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)   # 接上 vs 重新开始
        best = max(best, cur)
    return best
```

### 4) 中心扩展（最长回文子串）

```python
def longest_palindrome(s: str) -> str:
    def expand(l: int, r: int) -> tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1
    res = (0, 0)
    for i in range(len(s)):
        for l, r in (expand(i, i), expand(i, i + 1)):  # 奇/偶两种中心
            if r - l > res[1] - res[0]:
                res = (l, r)
    return s[res[0]:res[1] + 1]
```

## 易错点（TS → Python）

- **`a.sort()` 返回 `None`**，链式调用会爆。要新列表用 `sorted(a)`。
- **二维初始化别写 `[[0]*n]*m`**（共享引用），用 `[[0]*n for _ in range(m)]`。
- **字符串拼接**别用 `+=`，用 `"".join(parts)`。
- **字符是否数字字母**：`s.isdigit()` / `s.isalpha()` / `s.isalnum()`，不是 `Number.isNaN`。
- **负索引**：`a[-1]` 直接拿最后一个，比 TS 简洁。

## 高频题（按学习顺序）

1. #1 两数之和（哈希入门）
2. #26 删除有序数组重复项（快慢指针）
3. #88 合并两个有序数组（倒序双指针）
4. #189 轮转数组（三次反转）
5. #53 最大子数组和（Kadane / DP）
6. #56 合并区间（排序+扫描）
7. #5 最长回文子串（中心扩展）
8. #14 最长公共前缀
9. #11 盛最多水的容器（→ 双指针专题）
10. #15 三数之和（→ 双指针专题）
