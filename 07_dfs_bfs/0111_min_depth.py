"""
LeetCode 111. Minimum Depth of Binary Tree / 二叉树的最小深度  (Easy)
Link: https://leetcode.cn/problems/minimum-depth-of-binary-tree/

题目描述
--------
最小深度 = 从根到最近**叶子节点**的最短路径上的节点数。空树深度为 0。
注意叶子的定义：同时没有左右子节点的节点。

约束
----
- 节点数 0 <= n <= 10^5
- -1000 <= Node.val <= 1000

提示
----
卡住超过 25 分钟再去看 07_dfs_bfs/NOTES.md。
（BFS 解最优：第一次遇到叶子时答案就是当前层；DFS 也行但需要小心：单边为空时不能取 min）

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
    def minDepth(self, root: Optional[TreeNode]) -> int:
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
        ([3, 9, 20, None, None, 15, 7], 2),
        ([2, None, 3, None, 4, None, 5, None, 6], 5),    # 单边链
        ([], 0),
        ([1], 1),
        ([1, 2], 2),
    ]
    passed = 0
    for i, (vals, expected) in enumerate(cases, 1):
        actual = sol.minDepth(build_tree(vals))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: tree={vals!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
