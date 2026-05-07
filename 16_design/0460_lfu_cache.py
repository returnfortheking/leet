"""
LeetCode 460. LFU Cache / LFU 缓存  (Hard)
Link: https://leetcode.cn/problems/lfu-cache/

题目描述
--------
设计 LFU (Least Frequently Used) 缓存：
- get(key)：存在则返回 value 并使该 key 频次 +1；不存在返回 -1
- put(key, value)：插入或更新；超出容量时淘汰**频次最低**的 key；
  若多个 key 频次相同，则淘汰其中**最久未使用**的那个

要求 get / put **均 O(1)**。

约束
----
- 0 <= capacity <= 10^4
- 0 <= key <= 10^5
- 0 <= value <= 10^9
- 调用次数 <= 2 * 10^5

提示
----
卡住超过 25 分钟再去看 16_design/NOTES.md。
（思路：两层哈希——freq → 该频次的双向链表（按使用时间）；key → 节点；
  维护 min_freq，淘汰时去 freq=min_freq 链表的尾部摘）

复杂度（解完后填）
------
get / put：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class LFUCache:
    def __init__(self, capacity: int):
        # TODO: 初始化数据结构
        pass

    def get(self, key: int) -> int:
        # TODO: 在这里写你的解法
        pass

    def put(self, key: int, value: int) -> None:
        # TODO: 在这里写你的解法
        pass


def run_ops(cap: int, ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = LFUCache(cap)
    for name, args in ops:
        if name == 'get':
            out.append(obj.get(*args))
        else:
            obj.put(*args)
            out.append(None)
    return out


def test():
    cases = [
        (
            2,
            [('put', (1, 1)), ('put', (2, 2)), ('get', (1,)),
             ('put', (3, 3)), ('get', (2,)), ('get', (3,)),
             ('put', (4, 4)), ('get', (1,)), ('get', (3,)), ('get', (4,))],
            [None, None, 1, None, -1, 3, None, -1, 3, 4],
        ),
        (
            0,
            [('put', (0, 0)), ('get', (0,))],
            [None, -1],
        ),
    ]
    passed = 0
    for i, (cap, ops, expected) in enumerate(cases, 1):
        actual = run_ops(cap, ops)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
