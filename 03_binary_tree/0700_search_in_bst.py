"""
LeetCode 700. Search in a Binary Search Tree / 二叉搜索树中的搜索  (Easy)
Link: https://leetcode.cn/problems/search-in-a-binary-search-tree/

题目描述
--------
给定 BST 根 root 和值 val，返回值为 val 的子树根；不存在返回 None。

约束
----
- 节点数 1 <= n <= 5000
- 1 <= Node.val, val <= 10^7

提示
----
卡住超过 25 分钟再去看 03_binary_tree/NOTES.md 的「BST 关键操作」模板。

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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
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
    if not root: return []
    from collections import deque
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node is None: out.append(None)
        else:
            out.append(node.val); q.append(node.left); q.append(node.right)
    while out and out[-1] is None: out.pop()
    return out


def test():
    sol = Solution()
    cases = [
        (([4, 2, 7, 1, 3], 2), [2, 1, 3]),
        (([4, 2, 7, 1, 3], 5), []),
        (([5, 3, 6, 2, 4, None, 7], 7), [7]),
        (([1], 1), [1]),
        (([1], 2), []),
    ]
    passed = 0
    for i, ((vals, val), expected) in enumerate(cases, 1):
        actual = to_levels(sol.searchBST(build_tree(vals), val))
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} val={val}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
