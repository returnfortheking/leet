# 03 二叉树（核心专题，必须吃透）

## 核心思路

二叉树是所有递归题的"母题"。掌握以下两个**思维框架**，半数 DP / 回溯 / DFS 都能照搬：

### 框架 1：遍历思维（外部维护答案）

把树跑一遍，用全局变量收集结果。适合"统计/输出所有节点"。

```python
def traverse(root):
    if not root:
        return
    # 前序：到达节点时操作
    traverse(root.left)
    # 中序：左子树处理完时操作
    traverse(root.right)
    # 后序：左右子树都处理完时操作
```

### 框架 2：分治思维（递归函数有返回值）

子问题独立解出来，父问题用左右子问题的答案合并。适合"求最大/最小/能否/路径长度"。

```python
def solve(root):
    if not root:
        return base_case
    left = solve(root.left)
    right = solve(root.right)
    return combine(root.val, left, right)
```

**判断用哪个**：你能否用"左子问题答案 + 右子问题答案 + 当前节点信息"合并出当前答案？能 → 分治；不能（需要全局历史信息）→ 遍历 + 全局变量。

---

## 必背模板

### 1) 三种遍历（递归）

```python
def preorder(root):
    if not root: return
    out.append(root.val)
    preorder(root.left); preorder(root.right)

def inorder(root):     # BST 中序 = 升序
    if not root: return
    inorder(root.left)
    out.append(root.val)
    inorder(root.right)

def postorder(root):
    if not root: return
    postorder(root.left); postorder(root.right)
    out.append(root.val)
```

### 2) 三种遍历（迭代，统一栈模板）

```python
# 中序为例
def inorder_iter(root):
    out, stack, cur = [], [], root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        out.append(cur.val)
        cur = cur.right
    return out
```

### 3) 层序遍历（BFS）

```python
from collections import deque

def level_order(root):
    if not root: return []
    out, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):     # 关键：先取本层长度
            node = q.popleft()
            level.append(node.val)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
        out.append(level)
    return out
```

### 4) 后序"返回值"模板（解决一切"路径/深度/直径"）

```python
def diameter(root):
    ans = 0
    def depth(node):
        nonlocal ans
        if not node: return 0
        l = depth(node.left)
        r = depth(node.right)
        ans = max(ans, l + r)         # 经过当前节点的路径
        return 1 + max(l, r)          # 返回给上层用
    depth(root)
    return ans
```

这个模板能解：#543 直径、#124 最大路径和、#687 最长同值路径、#110 平衡判断…… **必须会默写**。

### 5) BST 关键操作

```python
def search(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root

def insert(root, val):
    if not root: return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root
```

### 6) 最近公共祖先 LCA（万能模板）

```python
def lowest_common_ancestor(root, p, q):
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right: return root      # p, q 分居两侧
    return left or right                # 都在一侧或一个就是祖先
```

---

## 易错点（TS → Python）

- **`nonlocal ans`**：内层函数修改外层变量必须声明，否则会 UnboundLocalError。这是树题踩坑 #1。
- **递归深度**：默认上限约 1000；深树要 `sys.setrecursionlimit(10**6)`。
- **节点判等**：用 `is` 不是 `==`（如 LCA 模板里）。
- **BFS 用 `deque`** 不是 `list`：`list.popleft` 不存在，`list.pop(0)` 是 O(n)。

## 高频题

1. #144/94/145 三种遍历 ★
2. #102 层序遍历 ★
3. #104 最大深度
4. #110 平衡二叉树
5. #226 翻转二叉树
6. #101 对称二叉树
7. #543 直径 ★（后序返回值模板）
8. #124 最大路径和 ★
9. #236 最近公共祖先 ★
10. #105/106 前序+中序 / 后序+中序 构造 ★
11. #297 序列化与反序列化 ★
12. #98 验证 BST
13. #230 BST 第 K 小（中序）
14. #700/701/450 BST 增删查
15. #199 右视图
16. #114 展开为链表
