"""
LeetCode 347. Top K Frequent Elements / 前 K 个高频元素  (Medium)
Link: https://leetcode.cn/problems/top-k-frequent-elements/

题目描述
--------
给定整数数组 nums 和整数 k，返回出现频率前 k 高的元素（任意顺序）。
要求时间复杂度优于 O(n log n)。

约束
----
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k 在 [1, 数组中不重复元素的个数] 范围
- 答案唯一

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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 1, 1, 2, 2, 3], 2), [1, 2]),
        (([1], 1), [1]),
        (([4, 1, -1, 2, -1, 2, 3], 2), [-1, 2]),
        (([1, 2], 2), [1, 2]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.topKFrequent(*args)
        ok = actual is not None and sorted(actual) == sorted(expected)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
