"""
LeetCode 21. Merge Two Sorted Lists / 合并两个有序链表  (Easy)
Link: https://leetcode.cn/problems/merge-two-sorted-lists/

题目描述
--------
给定两个非递减链表 list1 和 list2，将它们合并为一个非递减链表，
返回合并后的链表头。

约束
----
- 节点数 0 <= n1, n2 <= 50
- -100 <= Node.val <= 100

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
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        head = ListNode(0)
        curr = head
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head.next


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
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
        (([1, 5, 9], [2, 3, 8]), [1, 2, 3, 5, 8, 9]),
        (([1, 2, 3], []), [1, 2, 3]),
    ]
    passed = 0
    for i, ((a, b), expected) in enumerate(cases, 1):
        actual = to_list(sol.mergeTwoLists(from_list(a), from_list(b)))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: a={a!r} b={b!r}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
