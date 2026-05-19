"""
LeetCode 230. Kth Smallest Element in a BST / 二叉搜索树中第 K 小的元素  (Medium)
Link: https://leetcode.cn/problems/kth-smallest-element-in-a-bst/

题目描述
--------
给定 BST 根 root 和正整数 k，返回 BST 中所有节点值升序排列后的第 k 个数。

约束
----
- 节点数 1 <= n <= 10^4
- 1 <= k <= n
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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # TODO: 在这里写你的解法
        res = []

        def travel(root: Optional[TreeNode]):
            if not root:
                return
            travel(root.left)
            res.append(root.val)
            travel(root.right)

        travel(root)
        return res[k - 1]


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
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root


def test():
    sol = Solution()
    cases = [
        (([3, 1, 4, None, 2], 1), 1),
        (([5, 3, 6, 2, 4, None, None, 1], 3), 3),
        (([1], 1), 1),
        (([2, 1], 2), 2),
    ]
    passed = 0
    for i, ((vals, k), expected) in enumerate(cases, 1):
        actual = sol.kthSmallest(build_tree(vals), k)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: tree={vals!r} k={k}  expected={expected!r}  actual={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
