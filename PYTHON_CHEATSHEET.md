# Python 刷题速查（TS 程序员视角）

> 你在 TS 里的等价物 → Python 怎么写 + 最容易踩的坑。

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

## 4. 双端队列

```python
from collections import deque
q = deque()
q.append(x)        # 右进
q.appendleft(x)    # 左进
q.pop()            # 右出
q.popleft()        # 左出（这个是 BFS 队列、滑窗最常用的）
q[0], q[-1]        # 两端窥探
```

BFS 必用 `deque` 而不是 `list`，否则 `list.pop(0)` 让你的 BFS 退化成 O(n²)。

---

## 5. 堆（最小堆）

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

## 6. 字符串

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

## 7. 数学与位运算

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

## 8. 函数与作用域

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

## 9. 类型注解（让模板更专业）

```python
from typing import List, Optional, Tuple, Dict, Set

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

LeetCode 的题目签名是这种风格。Py3.9+ 也能直接用 `list[int]`，但 LeetCode 官方仍是 `List[int]`。

---

## 10. 链表 / 树节点（LeetCode 标准定义）

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

## 11. 常用速记

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

---

## 12. 递归限制

```python
import sys
sys.setrecursionlimit(10**6)  # DFS 题深递归时加这一行
```

LeetCode 默认大约 1000 层，链表题或深树会爆栈。

---

## 13. 调试技巧

- 直接 `print(...)` 输出中间值，比 IDE 调试器快。
- 复杂结构：`from pprint import pprint; pprint(grid)`。
- 模板里的 `test()` 函数对每个用例打印 `Case i: expected=... got=...` 后再 assert。
