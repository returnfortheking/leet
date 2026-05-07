"""
LeetCode 210. Course Schedule II / 课程表 II  (Medium)
Link: https://leetcode.cn/problems/course-schedule-ii/

题目描述
--------
共有 numCourses 门课，prerequisites[i] = [a, b] 表示修课 a 前必须先修 b。
返回一个合法的修课顺序（如果有多种，任意一种即可）；若无法完成全部课程，返回空数组。

约束
----
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= numCourses * (numCourses - 1)

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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def is_valid_order(n: int, prerequisites: List[List[int]], order: List[int]) -> bool:
    if not isinstance(order, list) or len(order) != n or sorted(order) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[a] > pos[b] for a, b in prerequisites)


def test():
    sol = Solution()
    cases = [
        (2, [[1, 0]], True),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (1, [], True),
        (2, [[0, 1], [1, 0]], False),     # 有环
    ]
    passed = 0
    for i, (n, prereq, has_solution) in enumerate(cases, 1):
        actual = sol.findOrder(n, [row[:] for row in prereq])
        if has_solution:
            ok = is_valid_order(n, prereq, actual)
        else:
            ok = actual == [] or actual is None or len(actual) == 0
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: n={n} prereq={prereq!r}  actual={actual!r}  valid={ok}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
