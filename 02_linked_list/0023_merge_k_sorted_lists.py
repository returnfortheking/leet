"""
LeetCode 23. Merge k Sorted Lists / 合并 K 个升序链表  (Hard)
Link: https://leetcode.cn/problems/merge-k-sorted-lists/

题目描述
--------
给定一个长度为 k 的链表数组 lists，每个链表都已按升序排列。
将所有链表合并成一个升序链表后返回。

约束
----
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] 按升序排列
- 总节点数 <= 10^4

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[-1, 0, 1], [-2, 2]], [-2, -1, 0, 1, 2]),
    ]
    passed = 0
    for i, (lists_vals, expected) in enumerate(cases, 1):
        lists = [from_list(v) for v in lists_vals]
        actual = to_list(sol.mergeKLists(lists))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: lists={lists_vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
