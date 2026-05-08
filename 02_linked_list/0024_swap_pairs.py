"""
LeetCode 24. Swap Nodes in Pairs / 两两交换链表中的节点  (Medium)
Link: https://leetcode.cn/problems/swap-nodes-in-pairs/

题目描述
--------
给定链表头 head，将每两个相邻节点交换位置后返回新链表头。
不能修改节点值，只能改变指针。

约束
----
- 节点数 0 <= n <= 100
- 0 <= Node.val <= 100

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        pass


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = to_list(sol.swapPairs(from_list(vals)))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
