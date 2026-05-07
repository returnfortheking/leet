"""
LeetCode 134. Gas Station / 加油站  (Medium)
Link: https://leetcode.cn/problems/gas-station/

题目描述
--------
环形路上有 n 个加油站。第 i 个加油站有 gas[i] 升油，从第 i 站到第 i+1 站消耗 cost[i] 升油。
你有一辆油箱无限的汽车，从某站出发顺时针绕一圈。
返回能完成一圈的起点下标；不存在则返回 -1。若存在，保证唯一。

约束
----
- n == gas.length == cost.length
- 1 <= n <= 10^5
- 0 <= gas[i], cost[i] <= 10^4

提示
----
卡住超过 25 分钟再去看 10_greedy/NOTES.md 的「加油站」模板。
（O(n) 单次扫描：tank 一旦为负就把起点设为 i+1）

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
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3),
        (([2, 3, 4], [3, 4, 3]), -1),
        (([5], [4]), 0),
        (([5], [6]), -1),
        (([4, 5, 2, 6, 5, 3], [3, 2, 7, 3, 2, 9]), -1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.canCompleteCircuit(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
