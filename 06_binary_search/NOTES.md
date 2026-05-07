# 06 二分查找

## 核心思路

二分的难点不是写循环，而是**写对边界**。三个常被搞错的细节：
1. `while l < r` vs `while l <= r`
2. `r = mid` vs `r = mid - 1`
3. 退出后返回 `l` / `r` / 还是 `mid`

我推荐**统一用半开区间 `[l, r)`** 一种风格，所有题都不变形：

```python
l, r = 0, len(nums)        # 半开
while l < r:
    mid = (l + r) // 2
    if check(mid):         # mid 满足某性质
        r = mid            # 答案在左半（含 mid）
    else:
        l = mid + 1        # 答案在右半（不含 mid）
return l                   # l == r, 第一个满足 check 的位置
```

把题目转成「**找第一个满足 P(x) 的 x**」，所有二分都同款。

## 三类二分

### 1) 普通二分（找等值）

```python
def search(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l if l < len(nums) and nums[l] == target else -1
```

### 2) 左右边界（找范围）

```python
def left_bound(nums, target):     # 第一个 >= target 的下标
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] >= target: r = mid
        else: l = mid + 1
    return l

def right_bound(nums, target):    # 第一个 > target 的下标 - 1
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > target: r = mid
        else: l = mid + 1
    return l - 1
```

或直接用标准库：`bisect.bisect_left` / `bisect.bisect_right`。

### 3) 二分答案（求最值）

题面常见：「**最小化最大值**」/「**最大化最小值**」/「**最小化某速度/容量满足约束**」。

模板：先确定答案的可行区间 `[lo, hi]`，写一个 `feasible(x) -> bool`，然后二分找最小/最大可行 x。

```python
def min_speed_eat_bananas(piles, h):       # #875 爱吃香蕉的珂珂
    def feasible(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h
    l, r = 1, max(piles) + 1
    while l < r:
        mid = (l + r) // 2
        if feasible(mid): r = mid
        else: l = mid + 1
    return l
```

## 旋转数组

```python
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        if nums[l] <= nums[mid]:                 # 左半有序
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:                                     # 右半有序
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1
```

## 易错点

- **整数溢出**：Python 没有溢出，`(l + r) // 2` 安全。但 TS/Java 习惯写 `l + (r - l) // 2` 也行。
- **mid 偏向**：`(l + r) // 2` 是下取整。**要避免死循环**：`r = mid - 1` 时下取整安全；`l = mid` 时必须 `mid = (l + r + 1) // 2` 上取整。
- **二分答案套路**：把检查写成单调的 `feasible(x)`，注意单调方向（feasible 从 false → true 还是 true → false）。

## 高频题

1. #704 二分查找 ★
2. #34 排序数组中元素的第一和最后位置 ★
3. #35 搜索插入位置
4. #33 搜索旋转排序数组 ★
5. #81 搜索旋转排序数组 II（含重复）
6. #153 寻找旋转数组的最小值
7. #162 寻找峰值
8. #4 寻找两个正序数组的中位数
9. #875 爱吃香蕉的珂珂 ★（二分答案）
10. #1011 在 D 天内送达包裹的能力（二分答案）
11. #410 分割数组的最大值（二分答案）
12. #69 x 的平方根
