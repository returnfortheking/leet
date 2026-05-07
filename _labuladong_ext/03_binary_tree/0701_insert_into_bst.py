"""
LeetCode 701. Insert into a Binary Search Tree / 二叉搜索树中的插入操作  (Medium)
Link: https://leetcode.cn/problems/insert-into-a-binary-search-tree/

题目描述
--------
给定 BST 根 root 和值 val（保证不在树中），将 val 插入 BST 后返回新的根。
任意保持 BST 性质的插入位置都可以接受。

约束
----
- 节点数 0 <= n <= 10^4
- -10^8 <= Node.val <= 10^8
- val != Node.val（保证不重复）

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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
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


def inorder(root):
    out = []
    def dfs(node):
        if not node: return
        dfs(node.left); out.append(node.val); dfs(node.right)
    dfs(root)
    return out


def test():
    sol = Solution()
    # 仅校验：插入后仍是 BST 且包含 val 与原所有值
    cases = [
        ([4, 2, 7, 1, 3], 5),
        ([40, 20, 60, 10, 30, 50, 70], 25),
        ([], 1),
        ([1], 0),
    ]
    passed = 0
    for i, (vals, val) in enumerate(cases, 1):
        root = sol.insertIntoBST(build_tree(vals), val)
        order = inorder(root)
        sorted_expected = sorted([v for v in vals if v is not None] + [val])
        ok = order == sorted_expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} val={val}  inorder={order}  expected_sorted={sorted_expected}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
