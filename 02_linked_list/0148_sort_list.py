"""
LeetCode 148. Sort List / 排序链表  (Medium)
Link: https://leetcode.cn/problems/sort-list/

题目描述
--------
给定链表头结点 head，将链表按升序排序后返回。
进阶：要求 O(n log n) 时间且 O(1) 额外空间（自底向上归并）。

约束
----
- 节点数 0 <= n <= 5 * 10^4
- -10^5 <= Node.val <= 10^5

提示
----
卡住超过 25 分钟再去看 02_linked_list/NOTES.md。
（思路：归并排序——快慢指针找中点 + 合并两个有序链表）

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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([5, 5, 5], [5, 5, 5]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = to_list(sol.sortList(from_list(vals)))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
