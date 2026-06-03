"""
LeetCode 297. Serialize and Deserialize Binary Tree / 二叉树的序列化与反序列化  (Hard)
Link: https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/

题目描述
--------
设计一对方法 serialize / deserialize，能将任意二叉树编码为字符串，
再从该字符串完整还原出原树（结构与值一致）。
编码格式可以自定，只要互逆即可。

约束
----
- 节点数 0 <= n <= 10^4
- -1000 <= Node.val <= 1000

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        val = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                val.append("n")
                return
            val.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(val)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        l = data.split(",")
        it = iter(l)

        def dfs():
            tmp = next(it)
            if tmp == "n":
                return None
            node = TreeNode(int(tmp))
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


class Codec2:
    def serialize(self, root: Optional[TreeNode]) -> str:
        # TODO: 在这里写你的解法
        if not root:
            return ""
        d = deque()
        d.append(root)
        ans = []
        while d:
            tmp = d.popleft()
            if tmp == "n":
                ans.append("n")
                ans.append(",")
                continue  # ★ 修死循环："n" 没有孩子，记完直接跳过
            ans.append(str(tmp.val))  # ★ val 转 str（否则 join 报错）
            ans.append(",")
            d.append(tmp.left if tmp.left else "n")  # 孩子为空就 push "n"
            d.append(tmp.right if tmp.right else "n")
        return "".join(ans)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        # TODO: 在这里写你的解法
        if len(data) == 0:
            return None
        dataList = data.split(",")
        root = TreeNode(int(dataList[0]))
        d = deque()
        d.append(root)
        i = 1  # ★ 线性指针扫 dataList，不用 2^level 堆编号
        while d and i < len(dataList):
            tmp = d.popleft()
            # 左孩子 = dataList[i]
            if dataList[i] != "n":
                tmp.left = TreeNode(int(dataList[i]))
                d.append(tmp.left)  # ★ 真节点入队（它还要配自己的两个孩子）
            i += 1
            # 右孩子 = dataList[i]
            if i < len(dataList) and dataList[i] != "n":
                tmp.right = TreeNode(int(dataList[i]))
                d.append(tmp.right)
            i += 1
        return root


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


def to_levels(root):
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
    cases = [
        [1, 2, 3, None, None, 4, 5],
        [],
        [1],
        [1, 2, 3, 4, 5, 6, 7],
        [-1, -2, -3],
    ]
    passed = 0
    for i, vals in enumerate(cases, 1):
        codec1 = Codec()
        codec2 = Codec()
        root = build_tree(vals)
        s = codec1.serialize(root)
        restored = codec2.deserialize(s)
        actual = to_levels(restored)
        ok = actual == vals
        status = "PASS" if ok else "FAIL"
        print(
            f"[{status}] Case {i}: tree={vals!r}  serialized={s!r}  restored={actual!r}"
        )
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
