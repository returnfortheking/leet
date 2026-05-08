"""
LeetCode 543. Diameter of Binary Tree / 二叉树的直径  (Easy)
Link: https://leetcode.cn/problems/diameter-of-binary-tree/

题目描述
--------
给定一棵二叉树，返回任意两节点之间最长路径的长度（用边数计）。
路径不一定经过根节点。

约束
----
- 节点数 1 <= n <= 10^4
- -100 <= Node.val <= 100

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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # TODO: 在这里写你的解法
        pass


# ----- 树辅助：根据 LeetCode 风格的 list 构建（None 占位，测试用，不要改） -----
def build_tree(vals: List[Optional[int]]) -> Optional[TreeNode]:
    if not vals:
        return None
    from collections import deque
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    while q and i < len(vals):
        node = q.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def test():
    s = Solution()
    cases = [
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
        ([1], 0),
        # 树形：6-4-2-1-3-5-7，最长路径 6 条边
        ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], 6),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        root = build_tree(vals)
        actual = s.diameterOfBinaryTree(root)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
