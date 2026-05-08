"""
LeetCode 337. House Robber III / 打家劫舍 III  (Medium)
Link: https://leetcode.cn/problems/house-robber-iii/

题目描述
--------
小偷的"街道"是一棵二叉树。除根节点外，每个节点都恰有一个父节点。
若同时偷一对父子节点，会触发警报。求能偷到的最大金额。

约束
----
- 节点数 1 <= n <= 10^4
- 0 <= Node.val <= 10^4

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
    def rob(self, root: Optional[TreeNode]) -> int:
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
        ([3, 2, 3, None, 3, None, 1], 7),
        ([3, 4, 5, 1, 3, None, 1], 9),
        ([1], 1),
        ([], 0),
        ([2, 1, 3, None, 4], 7),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.rob(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
