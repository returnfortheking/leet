"""
LeetCode 146. LRU Cache / LRU 缓存  (Medium)
Link: https://leetcode.cn/problems/lru-cache/

题目描述
--------
设计一个 LRU (Least Recently Used) 缓存，支持：
  - get(key)：存在则返回值（O(1)），并标记为最新使用；不存在返回 -1
  - put(key, value)：插入；超出容量时弹出最久未使用的键

约束
----
- 1 <= capacity <= 3000
- 调用次数 <= 2 * 10^5
- 必须 O(1) 平均时间

提示
----
卡住超过 25 分钟再去看 16_design/NOTES.md 的「LRU 缓存」模板。
（推荐先用 collections.OrderedDict 写出方案 A，被追问后再写方案 B：哈希 + 双向链表）

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class LRUCache:
    def __init__(self, capacity: int):
        # TODO: 初始化你的数据结构
        pass

    def get(self, key: int) -> int:
        # TODO: 在这里写你的解法
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: 在这里写你的解法
        pass


# ---------------------------------------------------------------------------
# 测试：用 LeetCode 的 [methods, args] 风格驱动（不要改）
# ---------------------------------------------------------------------------
def run_ops(cls, capacity: int, ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = cls(capacity)
    for name, args in ops:
        if name == 'get':
            out.append(obj.get(*args))
        else:
            obj.put(*args)
            out.append(None)
    return out


def test():
    cases = [
        # (cap, ops, expected_outputs)
        (
            2,
            [('put', (1, 1)), ('put', (2, 2)), ('get', (1,)),
             ('put', (3, 3)), ('get', (2,)),
             ('put', (4, 4)), ('get', (1,)), ('get', (3,)), ('get', (4,))],
            [None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            1,
            [('put', (2, 1)), ('get', (2,)), ('put', (3, 2)),
             ('get', (2,)), ('get', (3,))],
            [None, 1, None, -1, 2],
        ),
    ]
    passed = 0
    for i, (cap, ops, expected) in enumerate(cases, 1):
        actual = run_ops(LRUCache, cap, ops)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
