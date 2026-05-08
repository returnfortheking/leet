"""
LeetCode 19. Remove Nth Node From End / 删除链表的倒数第 N 个节点  (Medium)
Link: https://leetcode.cn/problems/remove-nth-node-from-end-of-list/

题目描述
--------
给定单链表的头结点 head 和正整数 n，删除链表中倒数第 n 个节点，返回链表头。
要求一次扫描完成。

约束
----
- 链表节点数为 sz
- 1 <= sz <= 30
- 1 <= n <= sz
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
        (([1, 2, 3, 4, 5], 2), [1, 2, 3, 5]),
        (([1], 1), []),
        (([1, 2], 1), [1]),
        (([1, 2], 2), [2]),
        (([1, 2, 3], 3), [2, 3]),
    ]
    passed = 0
    for i, ((vals, n), expected) in enumerate(cases, 1):
        actual = to_list(sol.removeNthFromEnd(from_list(vals), n))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} n={n}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
