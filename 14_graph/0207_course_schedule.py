"""
LeetCode 207. Course Schedule / 课程表  (Medium)
Link: https://leetcode.cn/problems/course-schedule/

题目描述
--------
共有 numCourses 门课，要修课程 a 必须先修课程 b（用 prerequisites[i] = [a, b] 给出）。
判断是否能修完所有课程。

约束
----
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000

提示
----
卡住超过 25 分钟再去看 14_graph/NOTES.md 的「拓扑排序」模板。

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
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ((2, [[1, 0]]), True),
        ((2, [[1, 0], [0, 1]]), False),
        ((4, [[1, 0], [2, 1], [3, 2]]), True),
        ((3, [[0, 1], [1, 2], [2, 0]]), False),
        ((1, []), True),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.canFinish(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
