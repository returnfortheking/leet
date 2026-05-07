"""
LeetCode 138. Copy List with Random Pointer / 随机链表的复制  (Medium)
Link: https://leetcode.cn/problems/copy-list-with-random-pointer/

题目描述
--------
给定一个链表，每个节点除了 next 指针外还有一个 random 指针，可以指向任意节点或 None。
返回该链表的**深拷贝**（节点对象互相独立，且 next、random 关系一致）。

约束
----
- 节点数 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- random 指向链表中某节点或 None

提示
----
卡住超过 25 分钟再去看 02_linked_list/NOTES.md。
（两种解法：哈希表 O(n) 空间；原地穿插 + 拆分 O(1) 空间）

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, nxt: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = nxt
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # TODO: 在这里写你的解法
        pass


def build(pairs):
    """pairs: [(val, random_index_or_None), ...]"""
    nodes = [Node(v) for v, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, ri) in enumerate(pairs):
        nodes[i].random = nodes[ri] if ri is not None else None
    return nodes[0] if nodes else None


def to_pairs(head):
    """把节点链转成 [(val, random_index_or_None)] 用于比较。"""
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    idx = {id(n): i for i, n in enumerate(nodes)}
    return [(n.val, idx.get(id(n.random))) for n in nodes]


def test():
    sol = Solution()
    cases = [
        # 用 (val, random_index) 描述：random 指向节点的下标，None 表示 random=None
        [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)],
        [(1, 1), (2, 1)],
        [(3, None), (3, 0), (3, None)],
        [],
        [(1, 0)],            # random 自指
    ]
    passed = 0
    for i, pairs in enumerate(cases, 1):
        head = build(pairs)
        copy = sol.copyRandomList(head)
        # 验证：(1) 结构与值一致 (2) 节点对象不共用
        ok_struct = to_pairs(copy) == pairs
        ok_no_share = True
        a, b = head, copy
        while a and b:
            if a is b:
                ok_no_share = False
                break
            a, b = a.next, b.next
        ok = ok_struct and ok_no_share
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: pairs={pairs!r}  expected={pairs!r}  actual={to_pairs(copy)!r}  no_share={ok_no_share}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
