"""
LeetCode 98. Validate Binary Search Tree / 验证二叉搜索树  (Medium)
Link: https://leetcode.cn/problems/validate-binary-search-tree/

题目描述
--------
判断给定二叉树是否是合法的二叉搜索树（BST）：
- 任意节点的左子树**所有**节点值都严格小于该节点
- 任意节点的右子树**所有**节点值都严格大于该节点
- 左右子树本身也是 BST

约束
----
- 节点数 1 <= n <= 10^4
- -2^31 <= Node.val <= 2^31 - 1

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
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
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([5, 4, 6, None, None, 3, 7], False),    # 经典坑：3 在 6 的左子树但 < 5
        ([2, 2, 2], False),
        ([1, 1], False),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.isValidBST(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
