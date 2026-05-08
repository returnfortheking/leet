"""
LeetCode 199. Binary Tree Right Side View / 二叉树的右视图  (Medium)
Link: https://leetcode.cn/problems/binary-tree-right-side-view/

题目描述
--------
给定二叉树根 root，假想你站在树的**右侧**，从上到下依次返回能看到的节点值。
即每层最右边那个节点的值。

约束
----
- 节点数 0 <= n <= 100
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
        ([1, None, 3], [1, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4], [1, 3, 4]),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.rightSideView(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
