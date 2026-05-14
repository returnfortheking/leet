"""
LeetCode 2. Add Two Numbers / 两数相加  (Medium)
Link: https://leetcode.cn/problems/add-two-numbers/

题目描述
--------
两个非空链表，分别表示两个非负整数（**逆序**存储，每个节点一位数字）。
将两数相加，结果同样以逆序链表返回。

约束
----
- 节点数 1 <= n1, n2 <= 100
- 0 <= Node.val <= 9
- 输入数无前导零（除了数字 0 本身）

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
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        hair = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry > 0:
            v1 = 0 if not l1 else l1.val
            v2 = 0 if not l2 else l2.val
            tmp = carry + v1 + v2
            carry, num = divmod(tmp, 10)
            curr = ListNode(num)
            tail.next = curr
            tail = curr
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return hair.next


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
        (([2, 4, 3], [5, 6, 4]), [7, 0, 8]),  # 342 + 465 = 807
        (([0], [0]), [0]),
        (([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        (([1], [9, 9, 9, 9]), [0, 0, 0, 0, 1]),
        (([5], [5]), [0, 1]),
    ]
    passed = 0
    for i, ((a, b), expected) in enumerate(cases, 1):
        actual = to_list(sol.addTwoNumbers(from_list(a), from_list(b)))
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
