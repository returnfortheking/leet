"""
LeetCode 322. Coin Change / 零钱兑换  (Medium)
Link: https://leetcode.cn/problems/coin-change/

题目描述
--------
给定不同面额的硬币 coins（每种无限多）和总金额 amount，
求凑成总金额所需的最少硬币个数。如果不可能，返回 -1。

约束
----
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TODO: 在这里写你的解法
        # c
        n = len(coins)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c > i:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


def test():
    sol = Solution()
    cases = [
        # LeetCode 题面 example
        (([1, 2, 5], 11), 3),                  # 5+5+1
        (([2], 3), -1),                        # 凑不出
        (([1], 0), 0),                         # amount=0
        # ★ amount=0 的多 coin 形式（dp[0] 必须 = 0，不少人会忘）
        (([1, 2, 5], 0), 0),
        # 单 coin 边界
        (([1], 2), 2),
        (([7], 7), 1),                         # 单 coin 恰好 = amount
        (([7], 14), 2),                        # 单 coin 整除 amount
        (([10], 5), -1),                       # 单 coin > amount
        # 完全背包特性（同 coin 可反复用）
        (([2], 6), 3),                         # 用 2 三次
        # 平价但凑不出（奇偶性）
        (([2, 4], 7), -1),                     # 偶数 coin 凑不出奇数 amount
        # ★ 贪心错例（必须 DP）
        (([1, 7, 10], 14), 2),                 # 7+7=2 优于 10+4*1=5
        # LeetCode 隐藏 case 风格的较复杂输入
        (([186, 419, 83, 408], 6249), 20),
        (([2, 5, 10, 1], 27), 4),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.coinChange(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()


# ============================================================================
# 复盘笔记（做完题再看；避免提前剧透）
# ============================================================================
# # 0322 零钱兑换 — 复盘
#
# > 题：[0322_coin_change.py](../09_dp/0322_coin_change.py)
# > 日期：2026-05-08
# > 套路：完全背包（详见 [09_dp/NOTES.md](../09_dp/NOTES.md)）
#
# ## 这版踩了哪些坑
#
# DP 思路（外层金额、内层硬币、转移 min）一开始就对，bug 全在 Python 语法层面。
#
# ### 致命
#
# 1. **`int("inf")` 抛 ValueError** —— Python 整数没有"无穷"概念，`int()` 只接受能解析为整数的字符串。表示无穷大用 `float('inf')`；本题更优雅是用 `amount + 1` 当哨兵（最差情况都用面值 1，最多 amount 枚），这样全程整数。
#
# 2. **`for c in coins.reverse()` 抛 TypeError** —— `reverse()` / `sort()` 都是**原地修改 + 返回 None**。这条之前在 [pitfalls.md § list API](pitfalls.md#list-api) 已经踩过，再踩一次说明肌肉记忆没建立。要反向遍历用 `reversed(coins)` 或 `coins[::-1]`。但**这道题根本不需要 reverse**——内层遍历 coins 顺序无关。
#
# 3. **漏写 `dp[0] = 0`** —— 基础情形：凑出金额 0 用 0 枚硬币。漏掉的话 `dp[i - c]` 当 `i == c` 时取的是 `dp[0] = inf`，整条递推链断在第一步，最终全是 inf。**DP 一定要给 base case 一个有意义的值**，不能依赖默认初始化。
#
# 4. **`range(1, n)` 漏算最后一个状态** —— Python `range` 是左闭右开 `[1, n)`，**不含 n**。想含端点必须写 `range(1, n + 1)`。归根结底是同切片一样的半开区间问题。详见 [pitfalls.md § 半开区间](pitfalls.md#半开区间切片--range)。
#
# 5. **凑不出时返回了 `inf` 而非 `-1`** —— 题目要求"无解返 -1"。最后一行要判断：
#    ```python
#    return dp[amount] if dp[amount] != INF else -1
#    ```
#
# ## 这次学到的
#
# - **Python 整数 vs 浮点的边界**：求最值题的 sentinel，能用整数（`amount + 1`）就别用 `float('inf')`，避免类型混用。返回值类型签名是 `-> int`，混入 inf 就破了。
# - **DP base case 别依赖初始化默认值**：`dp = [INF] * (n+1)` 之后**必须**显式 `dp[0] = 0`（或者题目意义对应的值）。这是 DP 转移的"种子"，没有种子整棵树长不出来。
# - **`range` 的半开**比切片还容易栽，因为切片很多时候"少一个字符没事"还能跑出结果，`range` 漏一个状态 DP 直接错——而且错得静默（不会报错，只是答案小）。
# - **再次确认：肌肉记忆建立的标志是 → 不再写出 reverse() 链式调用、不再用 `(int)(...)` 这种 cast 风格**。这两条踩了 ≥2 次，要刻意改。
#
# ## 修复后的关键片段
#
# ```python
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         INF = amount + 1
#         dp = [INF] * (amount + 1)
#         dp[0] = 0
#         for i in range(1, amount + 1):           # ★ +1 含端点
#             for c in coins:                      # 不需要 reverse
#                 if c <= i and dp[i - c] + 1 < dp[i]:
#                     dp[i] = dp[i - c] + 1
#         return dp[amount] if dp[amount] != INF else -1
# ```
#
# ## 触发器
#
# - 题面：「用任意数量的某些"物品"凑出某个总值」+「求最少件数 / 最多件数 / 是否可凑 / 方案数」
# - 物品**可重复用** → 完全背包，内层正序
# - 物品**只能用一次** → 0-1 背包，内层倒序
# - 求最少 → `min`，初始 `inf`，base `dp[0]=0`
# - 求方案数 → `+=`，初始 `0`，base `dp[0]=1`
