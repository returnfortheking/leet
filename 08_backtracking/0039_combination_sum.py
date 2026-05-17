"""
LeetCode 39. Combination Sum / 组合总和  (Medium)
Link: https://leetcode.cn/problems/combination-sum/

题目描述
--------
给定无重复正整数数组 candidates 和目标整数 target，返回 candidates 中所有
和为 target 的不同组合（每个数字可被无限次选择）。
组合不计顺序，解集不能含重复组合。

约束
----
- 1 <= candidates.length <= 30
- 2 <= candidates[i] <= 40
- candidates 元素互不相同
- 1 <= target <= 40

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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # TODO: 在这里写你的解法
        res = []
        tmp = []
        sum = 0

        def back(i: int):
            nonlocal sum
            if sum == target:
                res.append(list(tmp))
                return
            if sum > target:
                return
            for i in range(i, len(candidates)):
                tmp.append(candidates[i])
                sum += candidates[i]
                back(i)
                tmp.pop()
                sum -= candidates[i]

        back(0)
        return list(res)


def test():
    sol = Solution()
    cases = [
        (([2, 3, 6, 7], 7), [[2, 2, 3], [7]]),
        (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        (([2], 1), []),
        (([1], 1), [[1]]),
        (([1], 2), [[1, 1]]),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.combinationSum(*args)
        norm_a = sorted(sorted(c) for c in actual) if actual else []
        norm_e = sorted(sorted(c) for c in expected)
        ok = norm_a == norm_e
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: args={args!r}  count_e={len(expected)}  count_a={len(actual) if actual else 0}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
