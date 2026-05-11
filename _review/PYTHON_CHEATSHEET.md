# Python 刷题速查（TS 程序员视角）

> 数据结构 CRUD + 标准操作速查。语法糖类的简写见 [PYTHON_SHORTCUTS.md](PYTHON_SHORTCUTS.md)；踩过的坑见 [pitfalls.md](pitfalls.md)。

---

## 1. 容器与导入

| 用途 | TS / JS | Python |
|---|---|---|
| 动态数组 | `number[]` / `Array` | `list`（直接用 `[]`） |
| 哈希表 | `Map` / `Record` | `dict`（`{}`） |
| 集合 | `Set` | `set`（`set()` 或 `{1,2}`，注意 `{}` 是空 dict） |
| 双端队列 | 自己拼数组（O(n) shift） | `from collections import deque` |
| 默认值字典 | `obj[k] ??= []` | `from collections import defaultdict` |
| 计数 | `Map<T, number>` | `from collections import Counter` |
| 堆（小顶堆） | 自己写 | `import heapq` |
| 有序结构 | `TreeMap` 缺 | `from sortedcontainers import SortedList` |
| 二分插入 | 自己写 | `import bisect` |

**坑：** `{}` 是空 dict 不是空 set；空 set 必须 `set()`。

---

## 2. 数组 / 列表

```python
a = [1, 2, 3]
a.append(4)        # push
a.pop()            # pop（O(1)）
a.pop(0)           # shift（O(n)，少用！要 O(1) 用 deque）
a[-1]              # 最后一个，TS 里要 a[a.length-1]
a[1:3]             # 切片：[a[1], a[2]]
a[::-1]            # 反转（生成新列表）
a.reverse()        # 原地反转
sorted(a)          # 返回新列表
a.sort()           # 原地排序
sorted(a, key=lambda x: -x)  # 自定义排序
sorted(pairs, key=lambda p: (p[0], -p[1]))  # 多关键字
```

**坑：**
- `a.sort()` **返回 None**，不是排好的列表。TS 里 `a.sort()` 返回 a，Python 不会。
- 二维列表初始化别写 `[[0]*n]*m`，那是 m 个相同引用。要 `[[0]*n for _ in range(m)]`。
- 浅拷贝：`a[:]` 或 `a.copy()`；深拷贝：`copy.deepcopy(a)`。

---

## 3. 字典 / 哈希表

```python
d = {}
d[k] = v
d.get(k, default)       # 不存在返回 default，不抛异常
d.setdefault(k, [])     # 不存在则设默认
k in d                  # 检查 key
for k, v in d.items(): ...
for k in d: ...         # 默认遍历 key

from collections import defaultdict, Counter
cnt = Counter("aabbc")  # {'a':2, 'b':2, 'c':1}
cnt.most_common(2)      # [('a',2), ('b',2)]

groups = defaultdict(list)
groups[k].append(x)     # 自动初始化空列表
```

**坑：** `Counter` 减法 `c1 - c2` 只保留正值；如果要带负值用普通 dict。

---

## 4. 集合 set

```python
# 创建
s = {1, 2, 3}              # 字面量
s = set()                  # 空 set（不能写 {}，那是空 dict）
s = set([1, 2, 2, 3])      # 去重：{1, 2, 3}
s = set("abc")             # {'a', 'b', 'c'}

# 增
s.add(x)                   # 加单个，已存在不报错
s.update([1, 2, 3])        # 批量加（参数可以是任意可迭代）

# 删
s.remove(x)                # 删；不存在抛 KeyError ★
s.discard(x)               # 删；不存在静默忽略（更常用）
s.pop()                    # 随机弹一个（无序，空 set 抛 KeyError）
s.clear()                  # 清空

# 查
x in s                     # O(1)，比 list `in` 快几个数量级
len(s)

# 集合运算（高频）
a | b                      # 并集（union）
a & b                      # 交集（intersection）
a - b                      # 差集（a 有 b 没有）
a ^ b                      # 对称差（任一独有，去掉公共部分）
a <= b                     # a 是 b 的子集（issubset）
a < b                      # a 是 b 的真子集
a.isdisjoint(b)            # 是否无交集

# 推导
{x * 2 for x in nums}      # set 推导（花括号 + 表达式，跟 dict 区别在没有冒号）
{c for c in s if c.isalpha()}

# 不可变版
frozenset([1, 2, 3])       # 可作为 dict key 或另一个 set 的元素
```

**坑：**
- `{}` 是空 dict，**空 set 必须 `set()`**
- `s.remove(x)` 元素不存在抛 `KeyError`，要安全删用 `s.discard(x)`
- set 元素必须 hashable —— list/dict/set 不能放进 set；要装就 tuple / frozenset
- set **无序**，别假设遍历顺序（即使插入顺序看似稳定）

---

## 5. 双端队列

```python
from collections import deque
q = deque()
q.append(x)        # 右进
q.appendleft(x)    # 左进
q.pop()            # 右出
q.popleft()        # 左出（BFS 队列、滑窗最常用）
q[0], q[-1]        # 两端窥探
```

BFS 必用 `deque` 而不是 `list`，否则 `list.pop(0)` 让你的 BFS 退化成 O(n²)。

---

## 6. 堆（最小堆）

```python
import heapq
h = []
heapq.heappush(h, x)
top = heapq.heappop(h)        # 最小元素
heapq.heappushpop(h, x)        # 推入再弹出最小
heapq.heapify(arr)             # 原地建堆 O(n)
heapq.nlargest(k, arr)         # TopK 大
heapq.nsmallest(k, arr)        # TopK 小
```

**坑：**
- `heapq` **只有小顶堆**。要大顶堆，存负数：`heapq.heappush(h, -x)`。
- 元素是 tuple 时按字典序比较：`heapq.heappush(h, (priority, item))`。
- TopK 第 k 大：维护大小为 k 的小顶堆，堆顶就是第 k 大。

---

## 7. 字符串

```python
s = "abc"
s[::-1]                # 反转
"".join(["a", "b"])    # 拼接（不要用 s += ch，O(n²)）
s.split(",")
s.lower()
ord('a'), chr(97)      # ASCII 转换
s.isdigit(), s.isalpha()
"-".join(map(str, [1,2,3]))   # 1-2-3

# StringBuilder 的等价：
parts = []
parts.append("x")
result = "".join(parts)
```

**坑：** 字符串不可变；`s[i] = c` 不行。要改成 `list(s)` → 改 → `"".join(...)`。

---

## 8. 数学与位运算

```python
a // b           # 整除（向下取整，注意负数也是向下！-3 // 2 == -2）
a % b            # 取模（结果与除数同号）
divmod(a, b)     # (商, 余数)
abs(x)
min(a, b, c, *iterable)
max(...)
float('inf'), float('-inf')

# 位运算
x & y; x | y; x ^ y; ~x; x << k; x >> k
bin(x)           # '0b1011'
x.bit_count()    # 1 的个数（Py3.10+；老版用 bin(x).count('1')）
```

**坑：** Python `//` 向下取整对负数会让你算出意外结果。需要"向零截断"用 `int(a/b)` 或 `math.trunc`。

---

## 9. 函数与作用域

```python
def outer():
    cnt = 0
    def inner():
        nonlocal cnt    # ★ 修改外层变量必须 nonlocal
        cnt += 1
    inner()
    return cnt
```

**坑：** TS 里闭包改外层变量直接写就行；Python 必须 `nonlocal`（修改全局用 `global`）。仅"读"不需要。这是回溯/DFS 题最常踩的坑。

---

## 10. 类型注解（让模板更专业）

```python
from typing import List, Optional, Tuple, Dict, Set

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

LeetCode 的题目签名是这种风格。Py3.9+ 也能直接用 `list[int]`，但 LeetCode 官方仍是 `List[int]`。

---

## 11. 链表 / 树节点（LeetCode 标准定义）

```python
# 链表
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

# 二叉树
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

模板里已经预置好，可直接用。

---

## 12. 常用速记

```python
# 枚举
for i, x in enumerate(arr): ...

# zip
for a, b in zip(arr1, arr2): ...

# 任意 / 全部
any(x > 0 for x in arr)
all(x > 0 for x in arr)

# 列表推导（比 map/filter 更 Pythonic）
[x*2 for x in arr if x > 0]

# 解包
a, b = b, a            # 交换
first, *rest = [1,2,3] # first=1, rest=[2,3]

# 二维遍历
for i in range(m):
    for j in range(n):
        ...
```

更多语法糖见 [PYTHON_SHORTCUTS.md](PYTHON_SHORTCUTS.md)。

---

## 13. bisect 二分插入 / 查找

```python
import bisect

arr = [1, 3, 5, 7, 9]

# 查找插入位置
bisect.bisect_left(arr, 5)     # 2  最左插入位置（已存在 5 时在它之前）
bisect.bisect_right(arr, 5)    # 3  最右插入位置（== bisect.bisect()）
bisect.bisect_left(arr, 4)     # 2  不存在则返回应插入处
bisect.bisect_left(arr, 0)     # 0  小于全部
bisect.bisect_left(arr, 100)   # 5  大于全部（== len(arr)）

# 插入并保持有序（O(n)：二分 O(log n) + 移动元素 O(n)）
bisect.insort_left(arr, 4)     # arr → [1, 3, 4, 5, 7, 9]
bisect.insort_right(arr, 5)    # 重复值插在已有 5 之后
```

### 高频用法

```python
# 1. 二分查找：判断 x 是否存在
i = bisect.bisect_left(arr, x)
exists = i < len(arr) and arr[i] == x

# 2. 计数 ≤ x 的元素个数
count = bisect.bisect_right(arr, x)

# 3. 计数闭区间 [lo, hi] 内的元素个数
count = bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

# 4. LIS O(n log n)：在 tails 上 bisect_left
tails = []
for x in nums:
    i = bisect.bisect_left(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
# len(tails) 就是最长严格递增子序列长度
```

**坑：**
- `bisect` 要求数组**已排序**，否则结果错乱（不报错，只是答案错）
- `insort` 是 O(n)（要移动元素）；高频插入用 `sortedcontainers.SortedList`
- `key` 参数 Python 3.10+ 才支持；老版本只能预处理或排序元组

---

## 14. 递归限制

```python
import sys
sys.setrecursionlimit(10**6)  # DFS 题深递归时加这一行
```

LeetCode 默认大约 1000 层，链表题或深树会爆栈。

---

## 15. 调试技巧

- 直接 `print(...)` 输出中间值，比 IDE 调试器快。
- 复杂结构：`from pprint import pprint; pprint(grid)`。
- 模板里的 `test()` 函数对每个用例打印 `Case i: expected=... got=...` 后再 assert。
