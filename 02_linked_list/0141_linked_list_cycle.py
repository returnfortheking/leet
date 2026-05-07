"""
LeetCode 141. Linked List Cycle / 环形链表  (Easy)
Link: https://leetcode.cn/problems/linked-list-cycle/

题目描述
--------
给定单链表头 head，判断链表中是否存在环。
存在环：链表中某节点的 next 指针又指向了前面已经出现过的节点。

约束
----
- 节点数 0 <= n <= 10^4
- -10^5 <= Node.val <= 10^5
- pos = -1 或 0 <= pos < n（pos 是构造测试用的，函数本身看不到）

提示
----
卡住超过 25 分钟再去看 02_linked_list/NOTES.md 的「快慢指针」模板。
（哈希集合也能做但用了 O(n) 空间）

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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # TODO: 在这里写你的解法
        pass


def from_list_with_cycle(values, pos):
    """构造尾部连到 values[pos] 的环；pos = -1 表示无环。"""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


def test():
    sol = Solution()
    cases = [
        # (values, pos, expected)
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1, 2, 3], -1, False),
        ([1], 0, True),
    ]
    passed = 0
    for i, (vals, pos, expected) in enumerate(cases, 1):
        head = from_list_with_cycle(vals, pos)
        actual = sol.hasCycle(head)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} pos={pos}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
