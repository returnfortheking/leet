"""
LeetCode 743. Network Delay Time / 网络延迟时间  (Medium)
Link: https://leetcode.cn/problems/network-delay-time/

题目描述
--------
n 个网络节点（编号 1..n），times[i] = [u, v, w] 表示从 u 到 v 单向传播耗时 w。
从 k 出发广播信号，返回所有节点都收到信号所需的最短时间；
若有节点不可达则返回 -1。

约束
----
- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i] = [u, v, w]
- 1 <= u, v <= n; u != v
- 0 <= w <= 100
- 节点对 (u, v) 不重复

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
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2),
        (([[1, 2, 1]], 2, 1), 1),
        (([[1, 2, 1]], 2, 2), -1),     # 2 到 1 没有边
        (([[1, 2, 1], [2, 1, 3]], 2, 2), 3),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.networkDelayTime(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
