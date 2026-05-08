"""
LeetCode 380. Insert Delete GetRandom O(1) / O(1) 时间插入、删除和获取随机元素  (Medium)
Link: https://leetcode.cn/problems/insert-delete-getrandom-o1/

题目描述
--------
设计 RandomizedSet 类：
- insert(val): 不存在则插入，返回是否插入成功
- remove(val): 存在则移除，返回是否移除成功
- getRandom(): 等概率返回当前集合内任意元素（保证此时非空）

要求所有方法**期望 O(1)**。

约束
----
- -2^31 <= val <= 2^31 - 1
- getRandom 调用前集合非空
- 调用次数 <= 2 * 10^5

复杂度（解完后填）
------
所有操作 期望 O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class RandomizedSet:
    def __init__(self):
        # TODO: 初始化数据结构
        pass

    def insert(self, val: int) -> bool:
        # TODO: 在这里写你的解法
        pass

    def remove(self, val: int) -> bool:
        # TODO: 在这里写你的解法
        pass

    def getRandom(self) -> int:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = RandomizedSet()
            out.append(None)
        else:
            out.append(getattr(obj, name)(*args))
    return out


def test():
    cases = [
        # 注意 getRandom 的输出是不确定的，下面用占位 'ANY' 表示
        (
            [('init', ()),
             ('insert', (1,)),
             ('remove', (2,)),
             ('insert', (2,)),
             ('getRandom', ()),
             ('remove', (1,)),
             ('insert', (2,)),
             ('getRandom', ())],
            [None, True, False, True, 'ANY_IN_{1,2}', True, False, 2],
        ),
    ]
    passed = 0
    for i, (ops, expected) in enumerate(cases, 1):
        actual = run_ops(ops)
        ok = True
        for j, (a, e) in enumerate(zip(actual, expected)):
            if e == 'ANY_IN_{1,2}':
                if a not in (1, 2):
                    ok = False; break
            else:
                if a != e:
                    ok = False; break
        if len(actual) != len(expected):
            ok = False
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
