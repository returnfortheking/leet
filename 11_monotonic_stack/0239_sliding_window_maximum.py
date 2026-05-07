"""
LeetCode 239. Sliding Window Maximum / 滑动窗口最大值  (Hard)
Link: https://leetcode.cn/problems/sliding-window-maximum/

题目描述
--------
给定整数数组 nums 和窗口大小 k。窗口从最左侧起以步长 1 向右滑动直到末尾。
返回每次窗口内的最大值组成的数组。

约束
----
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length

提示
----
卡住超过 25 分钟再去看 11_monotonic_stack/NOTES.md 的「单调队列」模板。
（deque 维护下标；每入队前先把比当前小的从队尾踢掉，超出窗口的从队首踢掉）

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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]),
        (([1], 1), [1]),
        (([1, -1], 1), [1, -1]),
        (([9, 11], 2), [11]),
        (([4, -2], 2), [4]),
        (([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.maxSlidingWindow(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
