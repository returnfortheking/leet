"""
LeetCode 226. Invert Binary Tree / 翻转二叉树  (Easy)
Link: https://leetcode.cn/problems/invert-binary-tree/

题目描述
--------
将给定二叉树的每个节点的左右子树互换，返回翻转后的根。

约束
----
- 节点数 0 <= n <= 100
- -100 <= Node.val <= 100

提示
----
卡住超过 25 分钟再去看 03_binary_tree/NOTES.md。
（一行递归：交换左右后递归翻转两侧）

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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


def to_levels(root):
    """将树展开成层序列表（保留 None 占位，便于比较）"""
    if not root:
        return []
    from collections import deque
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def test():
    sol = Solution()
    cases = [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
        ([1], [1]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = to_levels(sol.invertTree(build_tree(vals)))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
