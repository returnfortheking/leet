# Python 踩坑清单（持续累积）

> 不是教程，是**真实犯过的错**的索引。每条带"症状 → 根因 → 正确写法"，并标注首次出现的题号方便溯源。

---

## 长度 / 大小

**症状**：`TypeError: 'method-wrapper' object cannot be interpreted as an integer`，或 `range(...)` 不报错但行为诡异。
**根因**：在 Python 里取长度用 **`len(x)`**（顶层函数），不是 `x.length`（TS）也不是 `x.__len__`（不加括号是方法对象）。`__len__` 是 dunder，正常代码里不直接用。
**正确**：

```python
for i in range(len(s)):
    ...
```

首次出现：[#0005](0005_longest_palindrome.md)

---

## 逻辑运算符

**症状**：表达式结果反直觉；或 `TypeError: unsupported operand type(s) for |`。
**根因**：
- TS `&&` `||` → Python `and` `or`
- TS `!x` → Python `not x`
- `&` `|` `^` 在 Python 里是**按位运算**，优先级比 `<` `>` `==` 高。如果两边是 bool 还能"碰巧"工作，但 `a > 0 | b < 0` 会先算 `0 | b`（按位或）再比较，结果错。

**正确**：

```python
if pos - i >= 0 and pos + i < len(s):  # 不是 |
    ...
```

首次出现：[#0005](0005_longest_palindrome.md)

---

## 字符串不可变

**症状**：`AttributeError: 'str' object has no attribute 'append'`（或 'insert'、'pop' 等）。
**根因**：Python 字符串**不可变**，没有 list 的修改方法。`s[i] = c` 也不行。
**正确**：

```python
# 要修改：转 list 修改完再 join
chars = list(s)
chars[i] = 'x'
s = "".join(chars)

# 要累积：用 list + join，比 += 拼字符串高效
parts = []
parts.append("hello")
parts.append("world")
result = " ".join(parts)
```

首次出现：[#0005](0005_longest_palindrome.md)

---

## 类与方法

**症状**：`TypeError: Odd() takes 2 positional arguments but 3 were given`，或调用方法时实例数据被错绑给参数。
**根因**：Python 不像 Java/TS 隐式注入 `this`。**实例方法第一个参数必须显式叫 `self`**。

```python
class Solution:
    def odd(self, s: str, pos: int) -> str:   # ← self 不能省
        ...
    def call_it(self):
        self.odd(s, pos)   # 调用时 self 自动传，不用写
```

首次出现：[#0005](0005_longest_palindrome.md)

---

## 类型转换

**症状**：`SyntaxError: cannot assign to function call`，或表达式不被识别。
**根因**：Python 没有 C/TS 的 `(int)(x)` cast 语法。类型转换是**函数调用**：

```python
i = int("42")      # 字符串/浮点 → int
f = float(3)       # int → float
s = str(123)       # 任意 → 字符串
arr = list("abc")  # 可迭代 → list（结果 ['a','b','c']）
```

字面量根本不需要转换：`i = 0` 就行。

首次出现：[#0005](0005_longest_palindrome.md)

---

## 变量名遮蔽内置

**症状**：写到一半发现 `max(a, b)` 报 `TypeError: 'int' object is not callable`。
**根因**：之前用 `max = 0` 把内置函数 `max` 给覆盖了。
**正确**：避免用以下名字当变量：`max` `min` `sum` `list` `dict` `set` `tuple` `id` `type` `input` `open` `len` `range` `map` `filter` `next` `iter` `format`。常见替代：

| 想用 | 改用 |
|---|---|
| `max` | `best` / `mx` / `cur_max` / `best_len` |
| `list` | `arr` / `nums` / `items` |
| `dict` | `d` / `mp` / `cnt`（计数用 Counter）|
| `set` | `seen` / `s` / `bag` |
| `id` | `idx` / `pid` / `node_id` |
| `str` | `s` / `text` / `word` |
| `chr` | `ch` / `c` / `letter` |

---

## list API

**症状**：`TypeError`，或 list 内容意外。
**根因**：`list.insert(index, value)` 第一个参数是**位置**，第二个是值——容易写反。其它常见 API 速查：

```python
arr.append(x)         # 末尾加
arr.insert(i, x)      # 在 i 位置插入（i 之前的元素前移）
arr.pop()             # 弹末尾，O(1)
arr.pop(0)            # 弹开头，O(n)！要 O(1) 用 collections.deque
arr.remove(x)         # 按值删第一个 x，O(n)；不存在抛 ValueError
del arr[i]            # 按下标删
arr.extend(other)     # 批量 append（== arr += other）
arr.index(x)          # 按值找下标，O(n)
arr.count(x)          # 出现次数
arr.reverse()         # 原地反转，返回 None ★
arr.sort()            # 原地排序，返回 None ★
sorted(arr)           # 返回新列表（不改原 arr）
```

★ **`sort()` 和 `reverse()` 返回 None**——这是 TS 转 Python 头号坑。`a = b.sort()` 后 `a` 是 None。要新列表用 `sorted(b)`。

首次出现：[#0005](0005_longest_palindrome.md)

---

## 半开区间：切片 + range

**症状**：返回的子串/子数组、循环遍历的下标少了或多了一个元素；常见 DP 题最后一个状态没算到、最长子串少 1 字符。
**根因**：Python 里**切片 `s[a:b]` 和 `range(a, b)` 都是 `[a, b)` 半开区间**——含 a，**不含 b**。想把 b 这个值/位置也包进来，stop 永远要 **+1**。

### 切片

```python
s = "abcdef"
s[1:4]      # 'bcd'  —— 含 1, 不含 4。 长度 = 4 - 1 = 3
s[0:0]      # ''     —— 空区间
s[:3]       # 'abc'  == s[0:3]
s[3:]       # 'def'  == s[3:len(s)]
s[:]        # 'abcdef' —— 整段（常用作浅拷贝）
s[::-1]     # 'fedcba' —— 第三个参数是 step
```

### range

```python
range(5)            # 0, 1, 2, 3, 4         （含 0，不含 5）
range(1, 5)         # 1, 2, 3, 4            （含 1，不含 5）
range(1, n)         # 1, 2, ..., n-1        ★ 没有 n！
range(1, n + 1)     # 1, 2, ..., n          ★ 想含 n 必须 +1

# 反向
range(n, 0, -1)     # n, n-1, ..., 1        （含 n，不含 0）
range(n - 1, -1, -1) # n-1, n-2, ..., 0     （倒着遍历下标）
```

**经典翻车**：DP 题外层 `for i in range(1, n)` —— 漏算了 `dp[n]`，最后一个状态。**含端点的循环必须 `range(1, n + 1)`**。
> #0322 零钱兑换内层 `for v in range(1, amount)` 漏算 `dp[amount]`，结果偏小。

### 为什么 Python 这么设计

- 长度直接 `b - a`，不用 ±1
- 空区间自然表示为 `[i, i)`
- 拼接性质：`s[:i] + s[i:] == s` 永远成立
- `len(range(a, b)) == b - a`，跟切片对齐

### 闭区间 ↔ 半开 速查

| 想要 | 写法 |
|---|---|
| 下标 l..r（**闭区间**）的切片 | `s[l : r + 1]` ← +1 |
| 1..n（**含 n**）遍历 | `range(1, n + 1)` ← +1 |
| 0..n-1（默认） | `range(n)` |
| 前 k 个 | `s[:k]` / `range(k)` |
| 倒数 k 个 | `s[-k:]` |
| 倒序 n..1 | `range(n, 0, -1)` |
| 倒序 n-1..0 | `range(n - 1, -1, -1)` |

**TS 自查**：TS 的 `arr.slice(a, b)` / `str.substring(a, b)` 也是半开 `[a, b)`，但 TS 没有 `range`——靠 `for (let i = a; i < b; i++)` 写，长度概念跟 `b - a` 一致。**所以 TS 转 Python 真正的坑是 `range`，而不是切片**——切片你早适应了。

首次出现：[#0005](0005_longest_palindrome.md)、[#0322](0322_coin_change.md)

---

## for / while 循环变量会"漏"到循环外

**症状**：循环跑完后，原本以为"已经没了"的临时变量还有值，被后续代码误用，引发难懂的报错。
**根因**：Python **没有块作用域**。`for x in xs:` 跑完后 `x` 仍指向最后一次迭代的值。这与 TS / Java 的 `for (let x of xs)` 完全不同——TS 那个 `x` 出了循环就 ReferenceError。

```python
strs = ["abc", "def", "ghi"]
for s in strs:
    pass
print(s)              # 'ghi'，不是报错。s 仍然存在！
```

特别危险的组合：循环变量名**和**外层数组名是 `s` / `strs` 这种容易混淆的关系。一旦写错（比如内层用了 `s` 又在外层 for 里 shadow），后续读"看起来对"但行为完全跑偏。

**避免方式**：
- 给循环变量起**和外层不重名**的短名：`for s in strs`、`for w in words` 即可，但**循环外不要再用 `s`** —— 用清晰名字 `min_len`、`first` 之类。
- 不需要遍历值时用 `_`：`for _ in range(n): ...`
- 高级技巧：用列表/生成器表达式或内置函数代替显式循环——根本没"漏出"的变量：

```python
min_len = min(len(s) for s in strs)   # s 是生成器内部局部，外面拿不到
```

首次出现：[#0014](0014_longest_common_prefix.md)

---

## break 只跳出最内层循环

**症状**：双层 for 里写了 break，外层却继续跑下去。
**根因**：Python（和 TS / C 一样）的 `break` 只跳出**最近**一层循环。Python 还**不支持** TS 里那种"标签 + break label"。

**三种正确的双层退出**：

```python
# 方案 A：sentinel return —— 最干净
def f():
    for i in ...:
        for j in ...:
            if bad(i, j):
                return ans

# 方案 B：flag
done = False
for i in ...:
    for j in ...:
        if bad(i, j):
            done = True
            break
    if done:
        break

# 方案 C：for-else（Python 特色）—— 适合"找到/没找到"二分
for i in ...:
    for j in ...:
        if found(i, j):
            break
    else:
        continue   # 内层完整跑完没 break，继续外层
    break          # 内层 break 过，外层也跳
```

实战中 90% 用方案 A：把双层循环包进函数，sentinel return 一了百了。

首次出现：[#0014](0014_longest_common_prefix.md)

---

## 待累积 (新增题时把根因抄到这里)

按主题预留：
- 整数除法 / 负数取模
- `range` 三参数与 step
- 闭包修改外层变量需 `nonlocal`
- 默认参数是可变对象的陷阱（`def f(x=[])`）
- 浅拷贝 vs 深拷贝
- `dict` 遍历顺序 / 修改时不能遍历
- `heapq` 只是小顶堆 / 元组比较
- 递归深度限制
