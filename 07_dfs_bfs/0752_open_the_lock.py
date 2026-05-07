"""
LeetCode 752. Open the Lock / 打开转盘锁  (Medium)
Link: https://leetcode.cn/problems/open-the-lock/

题目描述
--------
有 4 个轮子的密码盘，每个轮子上是 0-9 数字（0 与 9 相邻）。
初始 "0000"，每次操作可让某个轮子向前或向后旋转一格。
给定不可经过的死亡序列 deadends 和目标 target，返回最少操作次数；不可达返回 -1。

约束
----
- 1 <= deadends.length <= 500
- deadends[i].length == 4
- target.length == 4
- target 不在 deadends 中
- target / deadends[i] 都是 4 位数字字符串

提示
----
卡住超过 25 分钟再去看 07_dfs_bfs/NOTES.md 的「BFS 状态空间」模板。
（每个状态有 8 个邻居：4 个轮子 × 上下两方向）

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
    def openLock(self, deadends: List[str], target: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((["0201", "0101", "0102", "1212", "2002"], "0202"), 6),
        ((["8888"], "0009"), 1),
        ((["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"), -1),
        (([], "0000"), 0),
        ((["0000"], "8888"), -1),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.openLock(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
