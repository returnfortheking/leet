"""
LeetCode 92. Reverse Linked List II / 反转链表 II  (Medium)
Link: https://leetcode.cn/problems/reverse-linked-list-ii/

题目描述
--------
给定单链表头 head 和两个正整数 left, right (1-indexed, left <= right)，
将链表中位置 left 到 right 之间的节点反转后返回链表头。

约束
----
- 节点数 1 <= n <= 500
- -500 <= Node.val <= 500
- 1 <= left <= right <= n

提示
----
卡住超过 25 分钟再去看 02_linked_list/NOTES.md。
（思路：dummy 头 + 找到 left 前驱 + 局部反转 right - left + 1 个节点 + 接回）

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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
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
        (([1, 2, 3, 4, 5], 2, 4), [1, 4, 3, 2, 5]),
        (([5], 1, 1), [5]),
        (([1, 2], 1, 2), [2, 1]),
        (([1, 2, 3], 1, 3), [3, 2, 1]),
        (([1, 2, 3, 4, 5], 1, 1), [1, 2, 3, 4, 5]),
        (([3, 5], 1, 2), [5, 3]),
    ]
    passed = 0
    for i, ((vals, l, r), expected) in enumerate(cases, 1):
        actual = to_list(sol.reverseBetween(from_list(vals), l, r))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} left={l} right={r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
