"""
LeetCode 437. Path Sum III / 路径总和 III  (Medium)
Link: https://leetcode.cn/problems/path-sum-iii/

题目描述
--------
给定二叉树根 root 和整数 targetSum，统计**和等于 targetSum 的下行路径**数量。
路径要求：从任意节点出发到任意子孙节点（必须沿父子方向，向下走），不必从根开始或到叶结束。

约束
----
- 节点数 0 <= n <= 1000
- -10^9 <= Node.val <= 10^9
- -1000 <= targetSum <= 1000

提示
----
卡住超过 25 分钟再去看 15_prefix_sum/NOTES.md 的「树上前缀和」模板。

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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
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
        (([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8), 3),
        (([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22), 3),
        (([], 0), 0),
        (([1], 1), 1),
        (([1, -2, -3], -1), 1),
    ]
    passed = 0
    for i, ((vals, t), expected) in enumerate(cases, 1):
        actual = sol.pathSum(build_tree(vals), t)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} target={t}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
