"""
LeetCode 406. Queue Reconstruction by Height / 根据身高重建队列  (Medium)
Link: https://leetcode.cn/problems/queue-reconstruction-by-height/

题目描述
--------
给定数组 people，people[i] = [h_i, k_i] 表示第 i 个人身高 h_i，且前面恰有 k_i 个人
身高 >= h_i。请重新排列 people 使其符合每个人的 k 值约束，返回重排后的数组。

约束
----
- 1 <= people.length <= 2000
- 0 <= h_i <= 10^6
- 0 <= k_i < people.length

提示
----
卡住超过 25 分钟再去看 10_greedy/NOTES.md 的「重建队列」模板。
（思路：按 (-h, k) 排序后逐个 insert(k, p)；高的先排好，矮的插进去不影响高的人 k 值）

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
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
         [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]),
        ([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
         [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]),
        ([[1, 0]], [[1, 0]]),
    ]
    passed = 0
    for i, (people, expected) in enumerate(cases, 1):
        actual = sol.reconstructQueue([row[:] for row in people])
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
