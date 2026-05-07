# 04 双指针

## 核心思路

双指针不是一种算法，而是**两个移动指针**的几种使用形态：

| 形态 | 用途 | 典型题 |
|---|---|---|
| 左右对撞 | 已排序数组找配对 / 两端逼近 | #15 三数之和、#11 容器、#42 接雨水 |
| 快慢指针 | 原地修改 / 链表中点判环 | #26、#283、#141 |
| 同向滑动 | 子数组/子串问题 | → 滑动窗口（05 专题） |

**触发器**：题面里出现「**已排序**」或题面允许「**可以排序**」+「找配对/三元组/区间」→ 优先想左右双指针。

## 必背模板

### 1) 左右对撞（两数之和 II）

```python
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target:   return [l, r]
        if s < target:    l += 1     # 太小，左侧前进
        else:             r -= 1     # 太大，右侧后退
    return []
```

### 2) 三数之和（双指针 + 去重）

```python
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0: break                       # 剪枝
        if i > 0 and nums[i] == nums[i - 1]: continue  # 去重 i
        l, r = i + 1, n - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]: l += 1   # 去重 l
                while l < r and nums[r] == nums[r - 1]: r -= 1   # 去重 r
                l += 1; r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
```

### 3) 接雨水（双指针 O(1) 空间）

```python
def trap(height):
    l, r = 0, len(height) - 1
    lmax = rmax = ans = 0
    while l < r:
        if height[l] < height[r]:
            lmax = max(lmax, height[l])
            ans += lmax - height[l]
            l += 1
        else:
            rmax = max(rmax, height[r])
            ans += rmax - height[r]
            r -= 1
    return ans
```

### 4) 三色排序 / 荷兰国旗

```python
def sort_colors(nums):
    l, mid, r = 0, 0, len(nums) - 1
    while mid <= r:
        if nums[mid] == 0:
            nums[l], nums[mid] = nums[mid], nums[l]
            l += 1; mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[r] = nums[r], nums[mid]
            r -= 1                  # 注意：mid 不动，新换来的还要再判
        else:
            mid += 1
```

## 易错点

- **去重**：三数之和的去重要分别在 i / l / r 三层做。
- **三色排序**：换到 `r` 之后 `mid` **不要前进**，新元素值未知。
- **左右对撞为何不漏**：每一步都排除掉了一个边界元素的所有可能配对（必经的剪枝证明）。

## 高频题

1. #167 两数之和 II（有序）
2. #15 三数之和 ★
3. #16 最接近三数之和
4. #18 四数之和
5. #11 盛最多水的容器 ★
6. #42 接雨水 ★（双指针 / 单调栈两种解都要会）
7. #75 颜色分类（三指针）
8. #283 移动零
9. #26 删除有序数组重复项
10. #88 合并两个有序数组（倒序双指针）
