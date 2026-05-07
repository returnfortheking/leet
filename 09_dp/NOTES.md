# 09 动态规划（投入最大的专题）

## 核心思路

DP 题的本质：**带记忆化的递归**。把"暴力递归 → 记忆化 → 自底向上 DP"按需推进就能解。

### 解题三步走

1. **定义状态**：`dp[i]` 或 `dp[i][j]` 代表什么？必须是**一个明确的子问题答案**，不是"从 0 到 i 的某种值"。
2. **写状态转移**：`dp[i]` 怎么由比它"更小"的状态推出？
3. **确定 base case 和遍历方向**：哪些状态是初始已知的？外层循环顺序是什么（保证用到的子状态已经算好）？

### 触发器

| 题面特征 | 立刻想到 |
|---|---|
| 求方案数 / 求 max/min 长度 / 求"是否能" | DP |
| 「**子序列**」（不连续） | 区间型 / LIS 型 / LCS 型 DP |
| 「**子串**」（连续） | 子串型 DP（dp 含「以 i 结尾」语义） |
| 多组状态切换（持有/不持有） | 状态机 DP |
| 数轴上分组 / 容器装填 | 背包 DP |
| 区间合并 / 戳气球 | 区间 DP |
| 棋盘 / 网格 | 二维 DP |

## 七大模板

### 1) 一维线性 DP（爬楼梯 / 打家劫舍）

```python
# 打家劫舍 #198
def rob(nums):
    prev2, prev1 = 0, 0
    for x in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1
```

### 2) "以 i 结尾" 子串型 DP（最大子数组和）

```python
# Kadane #53
def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)         # 接上前面 vs 重新开始
        best = max(best, cur)
    return best
```

### 3) LIS（最长递增子序列）

```python
# O(n log n) 解法：维护 tails[]，tails[k] = 长度为 k+1 的递增子序列尾部最小值
import bisect
def length_of_lis(nums):
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

### 4) LCS（最长公共子序列）

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

### 5) 编辑距离

```python
def edit_distance(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],     # 删
                    dp[i][j - 1],     # 插
                    dp[i - 1][j - 1], # 改
                )
    return dp[m][n]
```

### 6) 0-1 背包

```python
def knapsack_01(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for j in range(W, w - 1, -1):    # ★ 倒序，保证每个物品只用一次
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[W]
```

完全背包：内层正序。

### 7) 状态机 DP（股票系列）

```python
# 至多 K 次交易 #188
def max_profit(k, prices):
    if not prices: return 0
    n = len(prices)
    k = min(k, n // 2)
    if k == 0: return 0
    # buy[i][j] / sell[i][j]: 第 i 天，已完成 j 次买入/卖出 的最大收益
    buy = [[-float('inf')] * (k + 1) for _ in range(n)]
    sell = [[0] * (k + 1) for _ in range(n)]
    for j in range(1, k + 1):
        buy[0][j] = -prices[0]
    for i in range(1, n):
        for j in range(1, k + 1):
            buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
            sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
    return sell[n - 1][k]
```

### 8) 区间 DP（戳气球 #312 模板）

```python
def max_coins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):                # 区间长度从小到大
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):         # 最后戳的气球是 k
                dp[i][j] = max(dp[i][j],
                               dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    return dp[0][n - 1]
```

### 9) 树形 DP（打家劫舍 III #337）

```python
def rob_tree(root):
    def f(node):
        if not node: return (0, 0)            # (不偷, 偷)
        l_no, l_yes = f(node.left)
        r_no, r_yes = f(node.right)
        no  = max(l_no, l_yes) + max(r_no, r_yes)
        yes = node.val + l_no + r_no
        return (no, yes)
    return max(f(root))
```

## 易错点

- **0-1 背包内层倒序**，完全背包内层正序，记反就 WA。
- **状态定义模糊**："前 i 个" vs "以 i 结尾"是两套体系，混用必错。
- **滚动数组优化**：能省空间但容易写错，第一遍先用二维稳妥，AC 后再压维。
- **初始化 `-float('inf')`** 表示"不可达"，最终答案取 max 时要排除掉。

## 高频题（按学习顺序）

**入门**
1. #70 爬楼梯 ★
2. #198 打家劫舍 ★
3. #213 打家劫舍 II
4. #53 最大子数组和（Kadane）
5. #152 乘积最大子数组

**经典子序列**
6. #300 最长递增子序列 ★
7. #1143 最长公共子序列 ★
8. #72 编辑距离 ★

**网格**
9. #62 不同路径
10. #64 最小路径和
11. #221 最大正方形
12. #931 下降路径最小和

**背包**
13. #322 零钱兑换 ★（完全背包）
14. #518 零钱兑换 II
15. #416 分割等和子集 ★（0-1 背包）
16. #494 目标和

**股票系列**
17. #121 买卖股票 I ★
18. #122 买卖股票 II
19. #188 买卖股票 IV ★（状态机）
20. #309 含冷冻期

**区间 DP**
21. #5 / #516 最长回文（子串/子序列）
22. #312 戳气球 ★

**树形**
23. #337 打家劫舍 III
24. #124 二叉树最大路径和
