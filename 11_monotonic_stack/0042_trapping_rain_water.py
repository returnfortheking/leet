"""
LeetCode 42. Trapping Rain Water / 接雨水  (Hard)
Link: https://leetcode.cn/problems/trapping-rain-water/

题目描述
--------
给定 n 个非负整数 height，每位代表宽度为 1 的柱子。
计算下雨之后能接多少雨水。

约束
----
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5

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
    def trap(self, height: List[int]) -> int:
        # TODO: 在这里写你的解法
        # 单调栈，每个值分 高度，位置，单调减，出现更高的，就把旧的出栈+计算储水量
        # 问题：凹进去的怎么计算(高低低高)
        stack = []
        res = 0
        for i, x in enumerate(height):
            if x == 0:
                continue
            prev = 0
            while stack and height[stack[-1]] <= x:
                j = stack.pop()
                res += (min(x, height[j]) - prev) * (i - j - 1)
                prev = min(x, height[j])
                # i,x
            if stack:
                j = stack[-1]
                res += (min(x, height[j]) - prev) * (i - j - 1)
            stack.append(i)
        return res


def test():
    sol = Solution()
    cases = [
        # 原始 6 条
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1], 0),
        ([], 0),
        ([3, 0, 0, 2, 0, 4], 10),
        ([0, 0, 0], 0),
        # 补：极简形状
        ([2, 0, 2], 2),                       # V 型最简
        ([3, 0, 3], 3),                       # 等高墙
        ([1], 0),                             # 单元素
        ([2, 5], 0),                          # 升 2
        ([5, 2], 0),                          # 降 2
        # 补：单调
        ([1, 2, 3, 4, 5], 0),                 # 严格升
        ([5, 4, 3, 2, 1], 0),                 # 严格降
        ([5, 5, 5, 5], 0),                    # 全等
        ([1, 1, 1, 1], 0),                    # 全等低
        # 补：复杂地形
        ([5, 2, 1, 2, 1, 5], 14),             # 大碗多内峰
        ([4, 1, 1, 1, 4], 9),                 # 平底锅
        ([5, 4, 3, 4, 5], 4),                 # 对称 U
        ([3, 2, 1, 2, 1], 1),                 # 阶梯+小坑
        ([3, 0, 1, 0, 3], 8),                 # 嵌套坑
        # 补：多盆 / 长零段（专门压 if x==0: continue）
        ([0, 7, 0, 7, 0, 7, 0], 14),          # 多个独立盆
        ([5, 0, 0, 0, 4], 12),                # 长零段 + 不等墙
        ([0, 5, 0, 0, 4, 0, 5, 0], 16),       # 边界 0 + 内部低峰
        # 补：边界值
        ([100000, 0, 100000], 100000),        # height 上限附近
        ([0] * 100, 0),                       # 全零
    ]
    passed = 0
    for i, (h, expected) in enumerate(cases, 1):
        actual = sol.trap(h)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: height={h!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
