"""
LeetCode 142. Linked List Cycle II / 环形链表 II  (Medium)
Link: https://leetcode.cn/problems/linked-list-cycle-ii/

题目描述
--------
给定单链表头 head，若存在环，返回环的入口节点；不存在则返回 None。
要求 O(1) 额外空间。

约束
----
- 节点数 0 <= n <= 10^4
- -10^5 <= Node.val <= 10^5

提示
----
卡住超过 25 分钟再去看 02_linked_list/NOTES.md 的「Floyd 判圈」模板。

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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # TODO: 在这里写你的解法
        pass


def build_with_cycle(values, pos):
    """构造尾部连到 values[pos] 的环；返回 (head, expected_entry_node_or_None)。"""
    if not values:
        return None, None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
        return nodes[0], nodes[pos]
    return nodes[0], None


def test():
    sol = Solution()
    cases = [
        ([3, 2, 0, -4], 1),
        ([1, 2], 0),
        ([1], -1),
        ([], -1),
        ([1, 2, 3, 4], 2),
        ([1, 2, 3], -1),
    ]
    passed = 0
    for i, (vals, pos) in enumerate(cases, 1):
        head, expected = build_with_cycle(vals, pos)
        actual = sol.detectCycle(head)
        ok = actual is expected     # 比较节点对象而非值
        status = "PASS" if ok else "FAIL"
        exp_val = expected.val if expected else None
        act_val = actual.val if actual else None
        print(f"[{status}] Case {i}: vals={vals!r} pos={pos}  expected_val={exp_val}  actual_val={act_val}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
