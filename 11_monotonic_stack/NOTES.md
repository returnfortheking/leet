# 11 单调栈 / 单调队列

## 核心思路

### 单调栈

**触发器**：题面问「**下一个更大 / 下一个更小**」、「**柱状图最大矩形**」、「**接雨水**」、「**每个元素左右第一个比它大/小的位置**」。

栈里维护**单调序列**：扫到新元素时，把破坏单调性的栈顶弹出（弹出时正好结算它的答案），再把新元素入栈。

### 单调队列

**触发器**：「**滑动窗口的最大值 / 最小值**」。

一边出栈尾保持单调（同单调栈），一边出队首处理超出窗口的旧元素。这就是为什么用 deque。

## 必背模板

### 1) 下一个更大元素（单调递减栈）

```python
def next_greater(nums):
    n = len(nums)
    res = [-1] * n
    stack = []                                  # 存下标，栈底到栈顶 nums 递减
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:    # 破坏递减性 → 出栈
            res[stack.pop()] = x                # 当前 x 就是被弹出元素的"下一个更大"
        stack.append(i)
    return res
```

口诀：求"下一个**更大**"用单调**递减**栈；求"下一个**更小**"用单调**递增**栈。

### 2) 柱状图最大矩形 #84

```python
def largest_rectangle(heights):
    heights = [0] + heights + [0]              # 哨兵：左 0 让一切入栈，右 0 把所有栈中元素结算
    stack = []
    ans = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            left = stack[-1]                    # 弹出 top 后的新栈顶 = top 的左边界
            ans = max(ans, heights[top] * (i - left - 1))
        stack.append(i)
    return ans
```

### 3) 接雨水（单调栈解法 #42）

```python
def trap(height):
    stack = []
    ans = 0
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            mid = stack.pop()
            if not stack: break
            left = stack[-1]
            width = i - left - 1
            depth = min(h, height[left]) - height[mid]
            ans += width * depth
        stack.append(i)
    return ans
```

### 4) 单调队列：滑动窗口最大值 #239

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()      # 存下标，nums[q] 单调递减
    res = []
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()                       # 比 x 小的都没用了
        q.append(i)
        if q[0] <= i - k:
            q.popleft()                   # 窗口左边界已超过 q[0]
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

## 易错点

- **栈里存下标还是值**：下标更通用（可以反推宽度），值只在简单场景够用。
- **哨兵**：柱状图最大矩形必须加左右哨兵 `[0]` 简化代码；接雨水可加可不加。
- **`<` vs `<=`**：影响是否会"压住等高的"。柱状图问题里 `>` / `>=` 都能 AC，但接雨水只有 `<` 是对的。
- **单调队列必须 `deque`**：两端 O(1) 操作。

## 高频题

1. #496 下一个更大元素 I ★（模板）
2. #503 下一个更大元素 II（循环数组：扫两遍）
3. #739 每日温度 ★
4. #84 柱状图最大矩形 ★
5. #85 最大矩形（85 = 84 × m）
6. #42 接雨水 ★（单调栈解法）
7. #239 滑动窗口最大值 ★（单调队列）
8. #316 去除重复字母（单调栈 + 字典序）
9. #402 移掉 K 位数字（单调栈 + 字典序）
10. #901 股票价格跨度
