# Python 简便写法速查

> 刷题中反复出现的 Python 简写，TS 里没有或写法相反。标 ★ 的是高频必会。

---

## ★ 链式比较 `0 <= x < n`

```python
if 0 <= nr < m and 0 <= nc < n:    # 网格越界检查
    ...
```

TS 必须写两段：`nr >= 0 && nr < m`。Python 直接夹逼。任意比较都能链：`a < b < c <= d`。

---

## ★ 链式赋值 `a = b = c = 0`

```python
r = c = di = 0          # 三个变量同时初始化为 0
left = right = head     # 双指针起点
```

注意：链式赋值给的是**同一个对象**。用于不可变值（int/str）没问题；用于 list 等可变对象会共享引用：

```python
a = b = []      # 危险：a 和 b 是同一个 list
a.append(1)     # b 也变了
```

---

## ★ 三元运算符（语序跟 TS 反！）

```python
x = a if cond else b             # Python：值-条件-备选
# TS:  x = cond ? a : b          # 条件-值-备选
```

**记住 Python 的"先说想要的，再说何时要"**。

---

## ★ `_` 当占位符

```python
for _ in range(n):       # 不需要循环变量值，明示"我不用 i"
    do_something()

a, _, c = (1, 2, 3)      # 解包时丢弃中间元素

prev2, _ = prev2, prev1  # 不在乎右侧某项
```

TS 里只能写 `for (let i = 0; i < n; i++)` 然后假装 i 不存在。

---

## ★ `enumerate` — 同时拿下标和值

```python
for i, x in enumerate(height):       # i 是下标，x 是值
    if x > height[i - 1]:
        ...

# 起始值可改（默认 0）
for line_no, line in enumerate(file, start=1):   # line_no 从 1 开始
    print(f"Line {line_no}: {line}")
```

刷题里巨高频——网格、双指针、单调栈，几乎都靠 `enumerate(arr)` 一行同时拿到 index + value。

**TS 也能做，但写法都很别扭**：

```typescript
// 方式 1：entries() — 跟 Python 最像，但要解构
for (const [i, x] of height.entries()) { ... }

// 方式 2：forEach — 回调风格，break/continue 用不了
height.forEach((x, i) => { ... });

// 方式 3：传统 C 风格（最常见但啰嗦）
for (let i = 0; i < height.length; i++) {
    const x = height[i];
    ...
}
```

Python `enumerate` 的优势：
- 跟 `for ... in` 直接配，break / continue / for-else 都能用
- 一行解包，不用先 `arr[i]` 再用
- 内置 `start` 参数处理 1-indexed 场景，TS 要 `i + 1`

### 配套小动作

```python
# 反向带下标
for i, x in enumerate(reversed(arr)):   # 但 i 是从 0 起的"反向 index"
    ...
# 想要"原数组下标"的反向遍历：
for i in range(len(arr) - 1, -1, -1):
    x = arr[i]

# 同时遍历两个数组（不需要 enumerate）
for a, b in zip(arr1, arr2):
    ...

# 三个一起
for i, (a, b) in enumerate(zip(arr1, arr2)):
    ...
```

---

## ★ 列表推导一维 / 二维

```python
# 一维
squares = [x * x for x in range(10)]
evens = [x for x in nums if x % 2 == 0]

# 二维（每行独立一份）
visited = [[False] * n for _ in range(m)]

# ⚠ 经典坑：[[False] * n] * m 是 m 个相同引用
bad = [[False] * 3] * 4
bad[0][0] = True         # 4 行第 0 列全变 True
```

带条件的推导：`[expr for x in iter if cond]`。也可以嵌套：`[(i, j) for i in range(m) for j in range(n)]`。

---

## ★ `[x] * n` 序列重复

```python
[0] * 100             # 100 个 0
[-1] * (n + 1)        # DP 数组初始化常用
[None] * 5            # 5 个 None 占位
"ab" * 3              # "ababab"，字符串也支持
(0,) * 3              # (0, 0, 0)，tuple 也支持
```

**TS 不支持**——TS 里 `Array * number` 是编译错。等价写法：

```typescript
Array(100).fill(0)        // 长度 100 全 0
"ab".repeat(3)            // 字符串重复
```

### 共享引用陷阱（同 [[False]*n]*m）

`[x] * n` 安全的前提是 `x` **不可变**：
- ✅ 安全：`int` `float` `str` `tuple` `bool` `None`
- ❌ 不安全：`list` `dict` `set` 以及任何自定义类对象

```python
[0] * 5             # ✓ int 不可变，5 个 0 安全
[[]] * 5            # ❌ 5 个引用都指向同一个 list
[(0,)] * 5          # ✓ tuple 不可变，安全
```

`[[0]*n] * m` 之所以错，是因为内层 `[0]*n` 是 list（可变），外层 `* m` 把这个 list 整体复制 m 份引用。所以二维全零必用 `[[0]*n for _ in range(m)]`。

---

## ★ 生成器表达式（圆括号代替方括号）

```python
total = sum(x * 2 for x in nums)      # 不创建中间 list，省内存
has_neg = any(x < 0 for x in nums)
all_pos = all(x > 0 for x in nums)
min_len = min(len(s) for s in strs)
```

外层是函数调用时圆括号可省。`sum([...])` 等价但浪费一份 list。

---

## ★ `any()` / `all()` 折叠 OR / AND 循环

**反例**：在循环里对同一个布尔反复赋值——典型 DP 转移场景容易写错。

```python
# ❌ 错：每次循环直接覆盖 dp[i]，最后一次循环决定结果
for w in wordDict:
    if len(w) <= i:
        dp[i] = dp[i - len(w)] and (s[i - len(w):i] == w)
        # 第一个 w 命中可能让 dp[i]=True，但下一个 w 不命中又会把它打回 False
```

正确语义是 **"只要任意一个 word 满足 → dp[i]=True"**——OR 关系。三种写法：

```python
# 方式 A：OR 累加（最小修复）
for w in wordDict:
    if len(w) <= i and s[i - len(w):i] == w:
        dp[i] = dp[i] or dp[i - len(w)]

# 方式 B：早退出（更快）
for w in wordDict:
    if len(w) <= i and dp[i - len(w)] and s[i - len(w):i] == w:
        dp[i] = True
        break

# 方式 C：any() 一行折叠（最 Pythonic）
dp[i] = any(
    dp[i - len(w)] and s[i - len(w):i] == w
    for w in wordDict if len(w) <= i
)
```

`any(iter)` = 任意一个元素为真就返回 True；`all(iter)` = 所有都真才 True。**写出来就不可能写错"循环里反复赋值"的 bug**——结构上禁止。

适用场景：
- "存在某个 x 使 P(x) 成立" → `any(P(x) for x in xs)`
- "所有 x 都满足 P(x)" → `all(P(x) for x in xs)`
- DP 中"任意 / 所有 子状态满足某条件" → 直接 `any/all` 替代手写循环

**TS 对照**：
```typescript
xs.some(x => check(x))     // any
xs.every(x => check(x))    // all
```
TS 也有，但是回调式；Python 的生成器表达式语法更紧凑，且能配 `if` 过滤。

首次出现：#0139 单词拆分

---

## ★ 闭包替代 `self.xxx`：递归状态用嵌套函数 + 局部变量

刷题里 95% 的 DFS / 回溯都该用闭包，**不是把临时状态挂到 Solution 类上**。

### Python 作用域机制（LEGB）

变量查找顺序：**Local → Enclosing → Global → Built-in**。

- **读变量**：自动向外查找
- **写变量**（`x = ...`）：**默认创建 Local**，外层同名变量不受影响

```python
def outer():
    x = 1
    def inner():
        print(x)             # 读 → 找到 outer 的 x = 1
        x = 2                # ❌ 写 → 新建 Local，外层 x 没变
    inner()
    print(x)                 # 还是 1
```

要修改外层变量，必须显式声明：

| 想改的范围 | 声明 |
|---|---|
| 外层函数（闭包）| `nonlocal x` |
| 模块全局 | `global x` |
| 对象属性 | 无需声明，直接 `self.x = ...`（属性机制，绕过 LEGB）|

### 关键二分：修改容器 vs 重新赋值

| 操作 | 例子 | 需要 nonlocal? |
|---|---|---|
| **修改容器内容** | `res.append(x)` / `d[k] = v` / `arr[i] = 0` | ❌ 不需要 |
| **重新绑定变量** | `x = ...` / `x += 1` / `x = max(...)` | ✓ 需要 |

前者只调用对象方法 / 改对象内部，变量本身仍指向同一对象——LEGB 一次读完就完事。后者本质是赋值语句，Python 默认在当前函数新建 Local。

---

### 递归状态的 4 种模式

#### 模式 A：纯递归无状态（首选）

结果靠 return 冒泡，**没有外部变量**。

```python
# 0104 最大深度
def maxDepth(self, root):
    if not root: return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
```

代表题：**0104 / 0226 / 0101 / 0021 / 0108**

#### 模式 B：闭包 + 容器修改（不需 nonlocal）

需要"收集"，用 `append` / `[k]=v` 这类**改容器内容**的操作。

```python
# 0094 中序遍历
def inorderTraversal(self, root):
    res = []
    def dfs(node):
        if not node: return
        dfs(node.left)
        res.append(node.val)         # ✓ 修改 list 内容，不是赋值 res
        dfs(node.right)
    dfs(root)
    return res
```

代表题：**0094 / 0102 / 0046 / 0078**

#### 模式 C：闭包 + 重新赋值（必须 nonlocal）

需要"维护最值/计数"，用 `x = max(...)` 这类**重新赋值变量**。

```python
# 0543 二叉树直径
def diameterOfBinaryTree(self, root):
    res = 0
    def depth(node):
        nonlocal res                 # ★ 必须
        if not node: return 0
        l, r = depth(node.left), depth(node.right)
        res = max(res, l + r)        # 重新赋值
        return max(l, r) + 1
    depth(root)
    return res
```

代表题：**0543 / 0124 / 0337 / 0437**

#### 模式 D：真正的实例状态（用 self）

对象本身**就是要持久存在**——跨方法/跨调用访问同一份数据。

```python
# 0155 最小栈
class MinStack:
    def __init__(self):
        self.stack = []              # 实例属性，跨方法访问
        self.min_stack = []
    def push(self, val):
        self.stack.append(val)
        ...
```

代表题（全是**设计题**）：**0146 LRU / 0155 最小栈 / 0208 Trie / 0295 数据流中位数**

---

### 两个反例（从我自己的题里抽）

#### 反例 1：模式 D 用在算法题里（0094 初版）

```python
class Solution:
    res = []                          # ❌ 类属性
    def inorderTraversal(self, root):
        self.res = []                 # ❌ 每次重置（自己跟自己别扭）
        self.travel(root)             # ❌ 工具函数硬挂类
        return self.res
    def travel(self, root):
        if not root: return
        self.travel(root.left)
        self.res.append(root.val)
        self.travel(root.right)
```

毛病：
- `self.res` **跨调用残留**——LeetCode 复用 `Solution` 实例时不重置就 bug
- `travel` 工具函数被硬挂到 Solution，污染接口
- 满屏 `self.` 影响阅读

应改成模式 B（见上）。

#### 反例 2：半 self 半闭包（0543 初版）

```python
def diameterOfBinaryTree(self, root):
    res = 0                           # 局部变量
    def depth(node):
        ...
        self.res = max(res, l + r)    # ❌ 写 self.res，读 res——两个不同变量
        return ...
    return res                        # 永远是 0
```

灾难合集：既没用 `nonlocal` 更新局部 `res`，又把值写到了根本没读的 `self.res` 上。结果永远返回初始值。应纯走模式 C。

---

### 决策树（背下来）

```
要收集/维护值跨递归层?
├─ 否 → 模式 A（纯递归靠 return）
└─ 是
   ├─ 用 list.append / dict[k]= / arr[i]= ？
   │  └─ 是 → 模式 B（闭包，直接用变量）
   └─ 用 x = max(...) / cnt += 1 ？
      └─ 是 → 模式 C（闭包 + nonlocal）

是否设计题（持久对象 / 跨方法访问）?
└─ 是 → 模式 D（self.xxx）
```

刷题日常 95% 是 A/B/C。**看到自己写 `self.cnt` / `self.res` / `self.max` 这种 helper-state，警觉**——大概率应改闭包。

### 一个绕开 nonlocal 的小技巧（不推荐常用）

把可变状态包成单元素 list 或 dict，全程只**修改**不**赋值**：

```python
res = [0]
def dfs(node, d):
    if not node: return
    res[0] = max(res[0], d)           # 改 list 内容，不重新赋值 → 不需要 nonlocal
```

能跑，但**降可读性**——直接 `nonlocal` 更清晰。

### TS 对照

TS 闭包默认就能写外层（`function inner() { ... }`）；Python 区分"读外层"和"写外层"（后者要 `nonlocal`），这是 TS → Python 切换时最容易栽的坑之一。

首次出现：#0094 中序遍历 / #0543 二叉树直径

---

## 不要写 `True if x else False`

```python
# ❌ 冗余
flag = True if cond else False
flag = True if x == y else False

# ✓ cond / x == y / x in s 这些表达式本身就是 bool，直接用
flag = cond
flag = (x == y)
flag = x in s
```

只有当**真正想把别的类型转成 bool** 时才用三元（其实直接 `bool(x)` 也行）。

```python
flag = True if value else False    # 还是别这么写
flag = bool(value)                 # 也行但很少用
flag = bool(value)                 # 大多数时候不需要——Python 的 if/and/or 会自动处理 truthy/falsy
```

---

## ★ list / iterable → str 用 `"".join()`，**没有 `.to_str()`**

```python
chars = ['a', 'b', 'c']
chars.to_str()              # ❌ AttributeError —— list 没这方法
chars.to_string()           # ❌ 同样不存在
str(chars)                  # ❌ 是 "['a', 'b', 'c']"，不是 "abc"
"".join(chars)              # ✓ "abc"
",".join(chars)             # ✓ "a,b,c"
```

**心法**：`join` 是**字符串方法**，由**分隔符**调用，参数是可迭代物：

```python
sep.join(iterable)          # 用 sep 把 iterable 里的字符串拼起来
```

注意 `iterable` 里每个元素必须是 `str`，整数 / list 等需要先转：

```python
"-".join([1, 2, 3])         # ❌ TypeError
"-".join(map(str, [1, 2, 3]))   # ✓ "1-2-3"
"-".join(str(x) for x in [1, 2, 3])   # ✓ 同上
```

**TS 对照**：TS 是 `[1,2,3].join("-")`——动词归数组。Python 反过来，**动词归分隔符字符串**。

首次出现：#0017 电话号码字母组合

---

## ★ `defaultdict` — 不用手动初始化字典 key

```python
from collections import defaultdict

# 计数：访问不存在的 key 自动返回 0
cnt = defaultdict(int)
cnt['a'] += 1       # 不用先 cnt['a'] = 0
cnt['b'] += 1

# 分组：访问不存在的 key 自动返回空 list
groups = defaultdict(list)
groups['fruit'].append('apple')   # 不用先 groups['fruit'] = []
groups['fruit'].append('banana')

# set 版本
neighbors = defaultdict(set)
neighbors[1].add(2)
```

等价于手写：

```python
# 没有 defaultdict 时
d = {}
if k not in d:
    d[k] = 0
d[k] += 1

# 或者
d = {}
d[k] = d.get(k, 0) + 1
```

---

## 多重解包

```python
a, b = b, a                      # 交换，不需要临时变量
first, *rest = [1, 2, 3, 4]      # first=1, rest=[2,3,4]
*init, last = [1, 2, 3, 4]       # init=[1,2,3], last=4
a, *_, c = [1, 2, 3, 4]          # 只要首尾

# 字典解包
merged = {**d1, **d2}            # 合并 dict（d2 覆盖 d1）
```

---

## `in` 多值匹配

```python
if ch in "()[]{}":               # 字符在串里
    ...
if val in (None, 0, False):      # 多值检查（TS 写 || 链）
    ...
if name in {"a", "b", "c"}:      # set 查 O(1)；元组/列表 O(n)
    ...
```

TS 等价是 `[a, b, c].includes(val)` 或 `val === a || val === b || ...`。

---

## f-string 调试小技巧

```python
n = 42
print(f"{n=}")                   # 输出：n=42
print(f"{nums[i]=}")             # 输出：nums[i]=...
print(f"{i:>4}")                 # 右对齐宽 4
print(f"{x:.2f}")                # 保留 2 位小数
```

`{var=}` 是 Python 3.8+ 的写法，调试时不用打标签：`print(f"{i=} {j=} {res=}")` 一次性看完所有变量。
