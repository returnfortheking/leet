"""
LeetCode 108. Convert Sorted Array to Binary Search Tree / 将有序数组转换为二叉搜索树  (Easy)
Link: https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/

题目描述
--------
给定升序整数数组 nums，构造一棵**高度平衡**的 BST 并返回其根节点。
高度平衡：任意节点左右子树高度差 <= 1。可能存在多种合法答案，任选一种返回。

约束
----
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums 严格升序

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # TODO: 在这里写你的解法
        pass


def inorder(root):
    out = []
    def dfs(node):
        if not node: return
        dfs(node.left); out.append(node.val); dfs(node.right)
    dfs(root)
    return out


def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
    if not root: return True
    h_diff = abs(height(root.left) - height(root.right))
    return h_diff <= 1 and is_balanced(root.left) and is_balanced(root.right)


def test():
    sol = Solution()
    # 多种合法答案 → 验证：(1) 中序 = nums (2) 是平衡 BST
    cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [0],
        [1, 2, 3, 4, 5, 6, 7],
        [-1, 0, 1, 2],
    ]
    passed = 0
    for i, nums in enumerate(cases, 1):
        root = sol.sortedArrayToBST(list(nums))
        ok = inorder(root) == sorted(nums) and is_balanced(root)
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: nums={nums!r}  inorder={inorder(root)}  balanced={is_balanced(root)}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
