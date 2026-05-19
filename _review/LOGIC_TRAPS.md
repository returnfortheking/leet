# 算法思路陷阱

> 不是 Python 语法/API 错，是**思路本身想偏了**。
> 每条陷阱 = 现象 + 错例题号 + 修正 + 触发器。下次写新题前扫一眼，避免重蹈覆辙。

**和其他三件套的关系**：
- [pitfalls.md](pitfalls.md) — 我写错过的 **Python 语法/语义**
- [PYTHON_SHORTCUTS.md](PYTHON_SHORTCUTS.md) — 我不知道的 **Python 简写**
- [PYTHON_CHEATSHEET.md](PYTHON_CHEATSHEET.md) — Python **标准 API 速查**
- **本文件** — 我**算法思路**栽过的坑（语法都对，但答案错或越界）

---

## 通用（跨题型的反复出现）

### 1. 终止条件命中后**必须 return**

递归 / 回溯里 base case 命中后忘 return，会继续往下执行，**污染上层状态或重复收集**。

```python
def backtrack(pos):
    if pos == len(digits):
        res.append("".join(tmp))      # 收集
        return                         # ★ 必须 return，否则继续往下走
    for ch in dic[digits[pos]]:
        ...
```

**错例**：#0017 第一版 — `if pos == len(digits) - 1: res.append(...)` 没 return，且时机错（应该 `== len`），导致永远收集不到完整组合。

### 2. 增 / 撤必须 **1:1 配对**

回溯：`tmp.append(x)` 之后 backtrack 后必须**只撤 1 个**。

```python
tmp.append(x)
backtrack(...)
tmp.pop()                              # ✓ 撤 1 个
# tmp = tmp[:-2]                       # ❌ 一次撤 2 个，状态全错
```

**错例**：#0017 第一版 — `tmp = tmp[:-2]` 多撤一个。

### 3. **拷贝**陷阱：append 引用 vs 值

`res.append(path)` 把 path 的**引用**塞进 res，后续 path 修改会污染所有 res 元素。

```python
res.append(path)                       # ❌ 后续 path.pop() 会改 res 里的元素
res.append(path[:])                    # ✓ 拷贝
res.append(list(path))                 # ✓ 同上
res.append("".join(path))              # ✓ join 天然新串（字符 path 专用）
```

适用：所有回溯收集 / 路径记录题。

### 4. 哨兵头节点（dummy）省特判

链表创建 / 修改头部时，没用 dummy 就要特判第一个节点。

```python
dummy = tail = ListNode()              # 哨兵不存数据
while ...:
    tail.next = ListNode(...)
    tail = tail.next
return dummy.next                      # 跳过哨兵
```

**适用题**：0002 / 0021 / 0023 / 0148 等所有"返回新链表"。

---

## 回溯（backtracking）

### T1. 入口函数定义了忘调

```python
def backtrack(pos): ...
return res                             # ❌ 没 backtrack(0)，res 永远 []
```

**错例**：#0017 第一版 — backtrack 写了但没启动，所有非空输入都返 `[]`。

**修**：`return res` 前加 `backtrack(0)`。

### T2. 组合题忘了 `start` 起点 → 退化成全排列

组合 pick 模板（Flavor A）的灵魂是 **`for i in range(start, n)`**——靠 `start` 单调递增防止 [a,b] 和 [b,a] 都被收集。

```python
def back(start, ...):
    for i in range(start, len(candidates)):    # ✓ 防重
        tmp.append(candidates[i])
        back(i, remaining - ...)               # 0039 允许复用：back(i)
        # back(i + 1, ...)                     # 0040 不许重复：back(i+1)
        tmp.pop()
```

**错版**：

```python
for i in range(len(candidates)):               # ❌ 每次从 0 开始 → 出现重复组合
```

去掉 start 起点等于退化到 **Flavor D（全排列）** 的语义——[2, 3] 和 [3, 2] 会被当成两组。

**错例**：#0039 组合总和 第一版

**辨别口诀**：

| 题 | 防重机制 |
|---|---|
| Flavor A 组合 / 子集 | `for i in range(start, n)` —— start 单调递增 |
| Flavor D 全排列 | `for i in range(n) if not used[i]` —— visited 集合 |

两个模板**外壳都是 for i**，灵魂全在 **`start` 还是 `used`**。看到组合题先认 start，看到排列题先认 used。

### T3. 选项遍历多套了一层

当前位的选项 = `dic[digits[pos]]`，直接对它遍历。如果先 `cur = digits[pos]` 再 `for c in cur`，cur 是单字符，外层循环只跑一次纯属冗余。

```python
# ❌ 多余的外层
cur = digits[pos]
for c in cur:                          # cur 是单字符 str，迭代 1 次
    for ch in dic[c]:
        ...

# ✓ 直接一层
for ch in dic[digits[pos]]:
    ...
```

**错例**：#0017 第一版

---

## BFS / 队列

### B1. 用 stack（LIFO）当 queue（FIFO）→ 层结构散架

BFS 必须**先进先出**，用 `list.pop()` 是后进先出，新孩子混进同一 list 末尾，**本层和下层节点交错**。

```python
# ❌ stack
stack = [root]
while stack:
    tmp = stack.pop()                   # LIFO，弹的是最新加的（已是下层）
    if tmp.left: stack.append(tmp.left)
    if tmp.right: stack.append(tmp.right)

# ✓ deque
from collections import deque
q = deque([root])
while q:
    tmp = q.popleft()                   # FIFO
    if tmp.left: q.append(tmp.left)
    if tmp.right: q.append(tmp.right)
```

**错例**：#0102 第一版 — 用 stack 当 queue，跑 `[3, 9, 20, null, null, 15, 7]` 得 `[[3], [20, 7], [15, 9]]`，期望 `[[3], [9, 20], [15, 7]]`。

**触发器**：题面带"按层 / 一层一层 / 最短步数 / 离起点最近" → 条件反射 `deque` + `popleft()`。

---

## 二分查找

### S1. 闭区间 / 半开区间**混用** → 越界

二分有两套模板，三处必须整套一致：

| 模板 | `r` 初始化 | 循环条件 | `r` 更新 |
|---|---|---|---|
| 闭区间 `[l, r]` | `len - 1` | `l <= r` | `r = mid - 1` |
| 半开 `[l, r)` | `len` | `l < r` | `r = mid` |

混用必越界。常见错配：`r = len(nums)` 但 `while l <= r`、`r = mid - 1`。

**错例**：#0035 第一版 — `r = len(nums)` + `while l <= r`，遇到 target 比所有元素大时 `mid` 摸到 `len(nums)` → IndexError。

**触发器**：写二分先决定"闭还是半开"，**三处保持一致**。

---

## DP

### D1. base case **漏初始化**

```python
dp = [INF] * (amount + 1)
# 漏了 dp[0] = 0
for i in range(1, amount + 1):
    for c in coins:
        dp[i] = min(dp[i], dp[i - c] + 1)
```

`dp[i - c]` 当 `i == c` 时取 `dp[0]`，还是 INF——整条递推链断在第一步，永远算不出有效值。

**错例**：#0322 零钱兑换

**修**：`dp = [INF] * (...); dp[0] = 0`（显式设种子）。

### D2. `range` 半开**漏最后一位**

`range(1, n)` 是 `[1, n)`，**不含 n**。DP 题外层循环要含 `dp[n]` 必须 `range(1, n + 1)`。

**错例**：#0322 — `for v in range(1, amount)` 漏算 `dp[amount]`，结果偏小。

**触发器**：DP 写完前先回头看终态下标——`dp[i]` 的最大 i 在 range 范围里吗？

### D3. 哨兵返回**未还原**

求"不可达返 -1"，但用 `INF` 当哨兵起步，**最后必须判一下**：

```python
return dp[amount] if dp[amount] != INF else -1
```

**错例**：#0322 — 直接 `return dp[amount]`，凑不出时返了 INF，类型签名都破了（`-> int` 却混入 inf）。

### D4. 2D DP **过度设计**

"每位置二选一 + 依赖前 k 步" 这类**单点决策**题，1D 滚动够。2D 是冗余且容易边界出错。

```python
# 0198 打家劫舍
# ❌ 2D 用 dp[i][0]=偷, dp[i][1]=不偷，要特判 i==1
# ✓ 1D：dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# ✓✓ 滚动变量：prev2, prev1 = prev1, max(prev1, prev2 + x)
```

**错例**：#0198 — 2D 能跑但 9 行变 3 行。

**判定**：状态只依赖前 1-2 步 + 每步二选一 → 1D 即可。

---

## 滑动窗口

### W1. 窗口长度计算和初始化**不统一**

`[l, r]` 闭区间长度 = `r - l + 1`，初始化 `min_len = len(s) + 1` 作占位。两者必须用同一个长度公式。

**错例**：#0076 第一版 — 更新最优解用 `r - l`（少 1），跟初始化 `len(s) + 1` 比，永远偏小。

### W2. 右指针扩展**时机**

标准滑窗模板：

```python
for r in range(len(s)):
    dic_s[s[r]] += 1                   # ★ 先把 s[r] 纳入窗口
    while 满足条件:                     # 再判断是否收缩
        更新最优
        dic_s[s[l]] -= 1
        l += 1
```

**关键**：先加右端，再判收缩。**别**把"加入"放进 if/else 分支——容易漏 `l == r == 0` 的初始位。

**错例**：#0076 第一版 — `l = r = 0` 时窗口空，进入 else 分支直接 `r += 1`，跳过仅含 `s[0]` 的窗口，导致 `s="a", t="a"` 返回空串。

---

## 树 / 闭包

### C1. 半 self 半闭包**混用变量名**

```python
res = 0                                # 局部
def depth(node):
    ...
    self.res = max(res, l + r)         # ❌ 写 self.res，读 res
return res                             # 永远 0
```

`self.res` 和 `res` 是**两个完全不同的变量**——属性 vs 局部。混着写**两边都不工作**。

**错例**：#0543 二叉树直径 第一版

**修**：纯走闭包，`nonlocal res` + `res = max(res, l + r)`。

### C2. 闭包重新赋值**漏 nonlocal**

```python
res = 0
def dfs(node):
    res = max(res, ...)                # ❌ 没 nonlocal，悄悄新建局部 res
```

Python 默认把 `x = ...` 当作"新建 Local"，外层 res 没被改。

**错例**：#0543 — 修了 self.res 后忘加 nonlocal。

**修**：函数顶 `nonlocal res`。详见 [SHORTCUTS § 闭包替代 self.xxx](PYTHON_SHORTCUTS.md)。

### C4. BST 验证：约束没传递到深层（只看父孙不够）

BST 的定义**不是**"每个节点的左孩子小、右孩子大"——是**整个左子树所有节点 < 当前**，**整个右子树所有节点 > 当前**。

错例（只查父子 + 父孙）：

```python
def isValidBST(self, root):
    if not root: return True
    if not (left.val < root.val < right.val): return False      # 只查直接孩子
    if not (left.right.val < root.val < right.left.val): return False   # 只查孙
    return isValidBST(left) and isValidBST(right)
```

**漏洞**：递归到 `left` 时，把"必须 < root"这个约束**丢了**——左子树深处可能出现 > root 的值不被发现。

反例（深度 3 违规漏检）：

```
       10
      /  \
     5    15
         /  \
        12   20
        /
       6     ← 6 在 10 的右子树（违法），但只查父孙查不到
```

修法：**每层显式传递上下界**：

```python
def valid(node, lo, hi):
    if not node: return True
    if not (lo < node.val < hi): return False
    return (valid(node.left, lo, node.val) and
            valid(node.right, node.val, hi))
return valid(root, float('-inf'), float('inf'))
```

**心法**：递归里**祖先约束**必须**显式传给后代**。"只看父孙"等价于丢弃祖先信息——树越深越漏。

也可用中序升序判定（BST 中序 = 严格升序），同 [SHORTCUTS § 闭包 模式 C](PYTHON_SHORTCUTS.md)。

错例：#0098 验证 BST 初版

---

### C3. 把临时状态挂 `self.xxx`

```python
class Solution:
    def inorderTraversal(self, root):
        self.res = []                   # ❌ 跨调用残留，必须手动重置
        self.travel(root)               # ❌ 工具方法不该挂 Solution
        return self.res
```

**错例**：#0094 中序遍历 第一版

**修**：闭包 + 局部 res，详见 [SHORTCUTS § 闭包替代 self.xxx](PYTHON_SHORTCUTS.md)。

---

## 数组 / 矩阵

### M1. `list(list(x))` ≠ `[[x]]`

```python
pre = [1]
list(list(pre))                        # = [1]，不是 [[1]]！
[pre]                                  # ✓ [[1]]
[pre[:]]                               # ✓ 拷贝版
```

`list(x)` 是"把 x **展开**成 list"——一维进一维出。**包装成嵌套**用 `[x]`。

**错例**：#0118 杨辉三角 第一版 — `res = list(list(pre))` 期望 `[[1]]`，实际 `[1]`。

---

## 双指针

### P1. `for i in range()` 里改 `i` 是**反模式**

```python
for i in range(n):
    i += 1                             # ❌ 不影响下一轮，下一轮 i 被 range 重置
```

Python `for` 不是 C 的 `for(i++)`——序列由 range 决定，循环内改 i 只影响本轮后续语句，下一轮被覆盖。

想"跳跃前进"用 `while` 手动控制下标。

**错例**：#0283 移动零 第一版 — for 循环里 `i += 1` 想跳过零，碰巧因为下轮 for 重置后还能匹配条件而跑对，但**逻辑绕**。

---

### P2. 数组找重复 + O(1) 空间 → 当链表用 Floyd 找环

"数组里找重复值"的直觉是 **hashmap 或 set 计数**——O(n) 空间。题目限定 **O(1) 空间** 时这条死路。

**抽象跳跃**：

把 `nums[i]` 当作"指针"——下标 i 的"下一节点"是下标 `nums[i]`。整个数组等价于一个**链表**。

```
nums = [1, 3, 4, 2, 2]
0 → 1 → 3 → 2 → 4 → 2 → 4 → ...  （从下标 2 起进入环）
```

由**抽屉原理**（n+1 个数 / 值都在 [1, n]）必有重复值——**重复值就是环入口的下标**，因为两个不同下标都指向那里。

代码 = **0142 链表找环入口** 改 4 处字符：

| 0142 | 0287 |
|---|---|
| `slow = head` | `slow = 0` |
| `slow = slow.next` | `slow = nums[slow]` |
| `fast = fast.next.next` | `fast = nums[nums[fast]]` |
| 终止 `fast and fast.next` | 不需要（永远有环）|

**触发器**：题面 = "**数组 + 值在 [1, n] + 找重复 + O(1) 空间**" → 数组当链表 + Floyd。

错例：#0287 寻找重复数（卡壳：不会建模成链表）

---

## 怎么用本文件

1. **每做完一道踩坑的题**，找到对应分类，**一句话**记下根因（不是题解）
2. 写新题**前**扫一眼相关分类——比如要写二分前看一眼 § 二分
3. 一周翻一遍，识别反复出现的模式（如"忘 return"、"边界 ±1"、"copy vs 引用"）
4. 同一类陷阱栽 2 次以上 → 是模板没建立，去 [HIGH_FREQ.md](../HIGH_FREQ.md) 找该套路的代表题强化

## 待累积

按主题预留，新题碰到坑直接归类抄入：

- 单调栈：维护方向 / 弹栈时机
- 并查集：路径压缩 / 按秩合并漏
- Trie：is_end 标志 vs 节点存在
- 拓扑排序：入度初始化 / 环判定
- 贪心：何时贪心不成立（反例构造）
- 字符串 KMP / 滚动哈希
