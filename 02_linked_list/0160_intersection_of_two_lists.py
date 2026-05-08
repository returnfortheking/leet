"""
LeetCode 160. Intersection of Two Linked Lists / 相交链表  (Easy)
Link: https://leetcode.cn/problems/intersection-of-two-linked-lists/

题目描述
--------
两个单链表 headA 和 headB，可能在某个节点开始相交（共用尾部）。
找到并返回它们的第一个相交节点；若不相交，返回 None。
要求 O(m + n) 时间，O(1) 额外空间。

约束
----
- 1 <= m, n <= 3 * 10^4
- 1 <= Node.val <= 10^5

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
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        pass


def build_intersection(a_only, b_only, common):
    """
    返回 (headA, headB, expected_intersection_node)。
    - a_only: A 链表独有部分（前缀）的值
    - b_only: B 链表独有部分（前缀）的值
    - common: 共享尾部的值；空表示不相交
    """
    common_head = None
    last = None
    for v in common:
        node = ListNode(v)
        if not common_head:
            common_head = node
        else:
            last.next = node
        last = node

    def build_prefix(values):
        dummy = ListNode()
        tail = dummy
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        tail.next = common_head
        return dummy.next

    return build_prefix(a_only), build_prefix(b_only), common_head


def test():
    sol = Solution()
    cases = [
        # (a_only, b_only, common)
        ([4, 1], [5, 6, 1], [8, 4, 5]),
        ([1, 9, 1], [3], [2, 4]),
        ([2, 6, 4], [1, 5], []),                # 不相交
        ([], [], [1, 2, 3]),                    # 完全重合
        ([1], [], [3]),
    ]
    passed = 0
    for i, (a, b, c) in enumerate(cases, 1):
        headA, headB, expected = build_intersection(a, b, c)
        actual = sol.getIntersectionNode(headA, headB)
        ok = actual is expected
        status = "PASS" if ok else "FAIL"
        exp_v = expected.val if expected else None
        act_v = actual.val if actual else None
        print(f"[{status}] Case {i}: a={a} b={b} common={c}  expected_val={exp_v}  actual_val={act_v}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
