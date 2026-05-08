"""
LeetCode 450. Delete Node in a BST / 删除二叉搜索树中的节点  (Medium)
Link: https://leetcode.cn/problems/delete-node-in-a-bst/

题目描述
--------
给定 BST 根 root 和键 key，从 BST 中删除值等于 key 的节点（如果存在），
返回更新后 BST 的根。删除后必须仍是合法 BST。
要求时间复杂度 O(h)，h 为树高。

约束
----
- 节点数 0 <= n <= 10^4
- -10^5 <= Node.val, key <= 10^5
- 节点值各不相同

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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
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
    # 仅校验：删除后仍是 BST 且 key 不在中
    cases = [
        ([5, 3, 6, 2, 4, None, 7], 3),
        ([5, 3, 6, 2, 4, None, 7], 0),    # key 不存在
        ([], 0),
        ([1], 1),
        ([1, None, 2], 1),
    ]
    passed = 0
    for i, (vals, key) in enumerate(cases, 1):
        root = sol.deleteNode(build_tree(vals), key)
        order = inorder(root)
        original = sorted([v for v in vals if v is not None])
        if key in original:
            original.remove(key)
        ok = order == original
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: vals={vals!r} key={key}  inorder={order}  expected={original}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
