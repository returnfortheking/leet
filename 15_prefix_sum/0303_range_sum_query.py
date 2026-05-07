"""
LeetCode 303. Range Sum Query - Immutable / 区域和检索 - 数组不可变  (Easy)
Link: https://leetcode.cn/problems/range-sum-query-immutable/

题目描述
--------
设计 NumArray 类：
- __init__(nums): 给定整数数组 nums
- sumRange(left, right): 返回 nums[left..right] 闭区间元素之和

要求多次调用 sumRange 时单次 O(1)。

约束
----
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- 调用次数 <= 10^4

提示
----
卡住超过 25 分钟再去看 15_prefix_sum/NOTES.md 的「一维前缀和」模板。

复杂度（解完后填）
------
init：O(?)    query：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class NumArray:
    def __init__(self, nums: List[int]):
        # TODO: 在这里初始化数据结构
        pass

    def sumRange(self, left: int, right: int) -> int:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = NumArray(*args)
            out.append(None)
        elif name == 'sumRange':
            out.append(obj.sumRange(*args))
    return out


def test():
    cases = [
        (
            [('init', ([-2, 0, 3, -5, 2, -1],)),
             ('sumRange', (0, 2)),
             ('sumRange', (2, 5)),
             ('sumRange', (0, 5))],
            [None, 1, -1, -3],
        ),
        (
            [('init', ([1],)),
             ('sumRange', (0, 0))],
            [None, 1],
        ),
    ]
    passed = 0
    for i, (ops, expected) in enumerate(cases, 1):
        actual = run_ops(ops)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
