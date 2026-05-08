"""
LeetCode 206. Reverse Linked List / 反转链表  (Easy)
Link: https://leetcode.cn/problems/reverse-linked-list/

题目描述
--------
给你单链表的头结点 head，反转链表并返回新的头结点。

约束
----
- 节点数 0 <= n <= 5000
- -5000 <= Node.val <= 5000

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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        pass


# ----- 链表辅助函数（测试用，不要改） -------------------------------------
def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def from_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def test():
    s = Solution()
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([42], [42]),
    ]
    passed = 0
    for i, (input_vals, expected) in enumerate(cases, 1):
        head = from_list(input_vals)
        actual = to_list(s.reverseList(head))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: input={input_vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
