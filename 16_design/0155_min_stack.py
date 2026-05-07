"""
LeetCode 155. Min Stack / 最小栈  (Medium)
Link: https://leetcode.cn/problems/min-stack/

题目描述
--------
设计一个栈支持：
- push(val), pop(), top()
- getMin(): O(1) 返回栈中最小值

所有方法均要求 O(1) 时间。

约束
----
- -2^31 <= val <= 2^31 - 1
- pop / top / getMin 调用前栈非空
- 调用次数 <= 3 * 10^4

提示
----
卡住超过 25 分钟再去看 16_design/NOTES.md 的「最小栈」模板。
（思路：每个栈元素同时存 (值, 当前最小值)，或维护双栈）

复杂度（解完后填）
------
所有操作 O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class MinStack:
    def __init__(self):
        # TODO: 初始化你的数据结构
        pass

    def push(self, val: int) -> None:
        # TODO: 在这里写你的解法
        pass

    def pop(self) -> None:
        # TODO: 在这里写你的解法
        pass

    def top(self) -> int:
        # TODO: 在这里写你的解法
        pass

    def getMin(self) -> int:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = MinStack()
            out.append(None)
        elif name in ('push', 'pop'):
            getattr(obj, name)(*args)
            out.append(None)
        else:
            out.append(getattr(obj, name)(*args))
    return out


def test():
    cases = [
        (
            [('init', ()),
             ('push', (-2,)),
             ('push', (0,)),
             ('push', (-3,)),
             ('getMin', ()),
             ('pop', ()),
             ('top', ()),
             ('getMin', ())],
            [None, None, None, None, -3, None, 0, -2],
        ),
        (
            [('init', ()),
             ('push', (1,)),
             ('push', (2,)),
             ('top', ()),
             ('getMin', ())],
            [None, None, None, 2, 1],
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
