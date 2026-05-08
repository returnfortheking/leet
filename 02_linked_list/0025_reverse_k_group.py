"""
LeetCode 25. Reverse Nodes in k-Group / K 个一组翻转链表  (Hard)
Link: https://leetcode.cn/problems/reverse-nodes-in-k-group/

题目描述
--------
给定单链表头 head 和正整数 k，将链表每 k 个节点为一组进行反转，返回新链表头。
若末尾不足 k 个节点，保持原顺序不动。
要求只用 O(1) 额外空间（不能创建新节点）。

约束
----
- 节点数 1 <= n <= 5000
- 0 <= Node.val <= 1000
- 1 <= k <= n

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
        (([1, 2, 3, 4, 5], 2), [2, 1, 4, 3, 5]),
        (([1, 2, 3, 4, 5], 3), [3, 2, 1, 4, 5]),
        (([1, 2, 3, 4, 5], 1), [1, 2, 3, 4, 5]),
        (([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1]),
        (([1, 2], 3), [1, 2]),
        (([1], 1), [1]),
    ]
    passed = 0
    for i, ((vals, k), expected) in enumerate(cases, 1):
        actual = to_list(sol.reverseKGroup(from_list(vals), k))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} k={k}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
