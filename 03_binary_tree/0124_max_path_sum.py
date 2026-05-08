"""
LeetCode 124. Binary Tree Maximum Path Sum / 二叉树中的最大路径和  (Hard)
Link: https://leetcode.cn/problems/binary-tree-maximum-path-sum/

题目描述
--------
给定二叉树根 root，找到任意一条路径使节点值之和最大并返回该最大值。
路径定义：从树中任意节点出发，沿父子边走到任意节点，每个节点至多经过一次，
路径不必经过根节点。

约束
----
- 节点数 1 <= n <= 3 * 10^4
- -1000 <= Node.val <= 1000

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # TODO: 在这里写你的解法
        pass


def build_tree(vals):
    if not vals:
        return None
    from collections import deque
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i]); q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i]); q.append(node.right)
        i += 1
    return root


def test():
    sol = Solution()
    cases = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([-3], -3),
        ([2, -1], 2),
        ([1, -2, 3], 4),
        ([-2, 1], 1),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.maxPathSum(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
