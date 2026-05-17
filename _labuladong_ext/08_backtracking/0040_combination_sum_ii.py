"""
LeetCode 40. Combination Sum II / 组合总和 II  (Medium)
Link: https://leetcode.cn/problems/combination-sum-ii/

题目描述
--------
给定可能含重复正整数的数组 candidates 和目标 target，返回所有和等于 target 的不同组合
（每个数字在每个组合中**只能用一次**）。解集中不能含重复组合。

约束
----
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30

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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # TODO: 在这里写你的解法
        res = []
        tmp = []
        sum = 0
        candidates.sort()

        def back(pos: int):
            nonlocal sum
            if sum == target:
                res.append(list(tmp))
                return

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if sum > target:
                    break
                tmp.append(candidates[i])
                sum += candidates[i]
                back(i + 1)
                sum -= candidates[i]
                tmp.pop()

        back(0)
        return res


def test():
    sol = Solution()
    cases = [
        (([10, 1, 2, 7, 6, 1, 5], 8), [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        (([2, 5, 2, 1, 2], 5), [[1, 2, 2], [5]]),
        (([1, 1, 1], 2), [[1, 1]]),
        (([1], 2), []),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.combinationSum2(*args)
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
