"""
LeetCode 234. Palindrome Linked List / 回文链表  (Easy)
Link: https://leetcode.cn/problems/palindrome-linked-list/

题目描述
--------
给定单链表头 head，判断该链表的值序列是否为回文。
进阶：要求 O(n) 时间，O(1) 额外空间。

约束
----
- 节点数 1 <= n <= 10^5
- 0 <= Node.val <= 9

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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # TODO: 在这里写你的解法
        pass


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
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 1], True),
        ([1, 0, 0, 1], True),
        ([1, 2, 3, 4], False),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.isPalindrome(from_list(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
