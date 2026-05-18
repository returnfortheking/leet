# Python 刷题速查（TS 程序员视角）

> 数据结构 CRUD + 标准 API 速查。每条标注：入参 / 返回值 / 原地与否 / 异常。
> 语法糖见 [PYTHON_SHORTCUTS.md](PYTHON_SHORTCUTS.md)，踩过的坑见 [pitfalls.md](pitfalls.md)。

**通用注释约定**：
- `→ 返回值类型` —— 调用的返回值（`None` 表示无返回值）
- `[原地]` —— 修改原对象
- `[抛 X]` —— 异常情况
- 行末 `# == ...` —— 实际示例输出

---

## 1. 容器选型

| 用途 | TS | Python | 创建 / 字面量 |
|---|---|---|---|
| 动态数组 | `Array` | `list` | `[]` / `list()` |
| 哈希表 | `Map` | `dict` | `{}` / `dict()` |
| 集合 | `Set` | `set` | `{1,2}` / `set()` ★ `{}` 是空 dict |
| 双端队列 | 自拼 | `collections.deque` | `deque()` |
| 默认值字典 | `obj[k] ??= []` | `collections.defaultdict` | `defaultdict(list)` |
| 计数 | `Map<T, number>` | `collections.Counter` | `Counter("aabb")` |
| 小顶堆 | 自写 | `heapq`（用 list） | `[]` + heapify |
| 二分插入 | 自写 | `bisect`（用有序 list） | 已排序 list |
| 有序结构 | `TreeMap` 缺 | `sortedcontainers.SortedList` | `SortedList()` |

---

## 2. list（数组）

```python
a = [1, 2, 3]
len(a)                    # → int 长度
a[i]                      # → 元素 [抛 IndexError 越界]
a[-1]                     # → 最后一个；负下标合法
a[l:r]                    # → 新 list 切片 [l, r)；越界自动裁剪不抛
a[::-1]                   # → 新 list 反转副本

# 增
a.append(x)               # → None [原地] 末尾添加
a.insert(i, x)            # → None [原地] 在下标 i 插入，后续右移；i ≥ len 等价 append
a.extend(iterable)        # → None [原地] 批量末尾添加；== a += list(iterable)

# 删
a.pop()                   # → 弹出的末尾元素 [原地] O(1) [抛 IndexError 空]
a.pop(0)                  # → 弹出的头部元素 [原地] O(n) ★ 高频 pop(0) 改用 deque
a.pop(i)                  # → 弹出的 a[i] [原地]
a.remove(x)               # → None [原地] 按值删第一个 [抛 ValueError 不存在]
del a[i]                  # → 按下标删，无返回
a.clear()                 # → None [原地] 清空

# 查
a.index(x)                # → 首个 x 的下标 [抛 ValueError 不存在]
a.count(x)                # → x 出现次数 int
x in a                    # → bool O(n)

# 排序 / 反转
a.sort(key=None, reverse=False)   # → None [原地] ★ 注意返回 None！
a.reverse()                       # → None [原地] ★ 同上
sorted(a, key=None, reverse=False)   # → 新 list（不改原）
list(reversed(a))                    # → 新 list；reversed 返回迭代器，要 list()

# 自定义排序（key 传函数 / lambda）
sorted(arr, key=lambda x: -x)              # 按负值 → 降序（等价 reverse=True）
sorted(arr, key=str.lower)                  # 字符串不区分大小写
sorted(pairs, key=lambda p: (p[0], -p[1])) # 多关键字：先 p[0] 升，再 p[1] 降
sorted(words, key=len)                      # 按长度

# 极少需要：自定义比较函数（key 表达不出来时）
from functools import cmp_to_key
sorted(arr, key=cmp_to_key(lambda a, b: a - b))    # 返回 <0/0/>0
```

### 拷贝（一维 + 二维）★

```python
# 一维（元素是 int / str / bool 这种不可变值）
b = a[:]                    # ✓ 浅拷贝
b = a.copy()                # ✓ 同上
b = list(a)                 # ✓ 同上

# ⚠ 二维：一维方法只复制外层！内层 row 还是同一引用
grid2 = grid[:]
grid2[0][0] = 99            # ❌ grid[0][0] 也被改了

# 二维独立拷贝（每行独立）
grid2 = [row[:] for row in grid]            # ✓ 最 Pythonic
grid2 = [list(row) for row in grid]         # ✓ 同上

# 嵌套更深（list of dict of list 等）才需要 deepcopy
import copy
grid2 = copy.deepcopy(grid)                 # ✓ 万能但慢，刷题极少需要
```

**速查表**：

| 写法 | 外层 | 内层 |
|---|---|---|
| `b = a` | ❌ 同对象 | ❌ 共享 |
| `a[:]` / `a.copy()` / `list(a)` | ✓ 新 list | ❌ 共享（内层 list 仍然原对象） |
| **`[row[:] for row in a]`** | ✓ 新 list | ✓ 行独立 |
| **`copy.deepcopy(a)`** | ✓ 新 list | ✓ 任意深度独立 |

**坑：**
- `a.sort()` / `a.reverse()` **返回 None**——`b = a.sort()` 后 b 是 None。要新 list 用 `sorted(a)`
- 二维初始化 `[[0]*n]*m` 是 m 个**相同引用**；要独立行用 `[[0]*n for _ in range(m)]`
- 二维**拷贝** `grid[:]` 同样是浅，要行独立用 `[row[:] for row in grid]`
- `a.pop(0)` 是 O(n)——BFS 必用 `deque`

---

## 3. dict（哈希表）

```python
d = {}
d = {"a": 1, "b": 2}
len(d)                          # → int 键数

# 增 / 改
d[k] = v                        # → 无返回；不存在则创建
d.update(other)                 # → None [原地] 合并 other 字典（覆盖同 key）
d.setdefault(k, default)        # → 已有的 d[k] 或 default；不存在则同时设 d[k]=default

# 查 / 包含判断（Python 没 .has() / .contains()，全靠 in）
k in d                          # → bool O(1)  ★ key 存在判断
k not in d                      # → bool O(1)
v in d.values()                 # → bool O(n)  按值查
(k, v) in d.items()             # → bool O(n)  按 (k,v) 对查

d[k]                            # → 值 [抛 KeyError 不存在]
d.get(k)                        # → 值 / None（缺省，不抛）
d.get(k, default)               # → 值 / default（不抛）

# 删
del d[k]                        # → 无返回 [抛 KeyError]
d.pop(k)                        # → 删除并返回值 [抛 KeyError]
d.pop(k, default)               # → 删除并返回值 / default（不抛）
d.popitem()                     # → (k, v) tuple，弹最后插入项 (Py3.7+) [抛 KeyError 空]
d.clear()                       # → None [原地] 清空

# 遍历
for k in d: ...                 # 默认遍历 key
for k, v in d.items(): ...      # → 视图（实时反映 d）
for v in d.values(): ...        # → 值视图
list(d.keys())                  # → key 的 list
```

**坑：**
- 默认遍历 `for x in d` 是遍历 **key**，不是 value
- `d.keys()` 是视图，遍历期间改 d 会报错——要拷贝就 `list(d.keys())`

### Counter（频次统计）

```python
from collections import Counter
cnt = Counter("aabbc")          # → Counter({'a': 2, 'b': 2, 'c': 1})
cnt = Counter([1, 1, 2])        # → Counter({1: 2, 2: 1})

cnt[k]                          # → 出现次数；不存在返回 0（不抛 KeyError！）
cnt.most_common(k)              # → 前 k 个 [(elem, count), ...]，降序
cnt.most_common()               # → 全部，降序

cnt.update(other_iter)          # → None [原地] 累加（不是覆盖）
cnt.subtract(other)             # → None [原地] 减法，允许负数

# 算术（返回新 Counter）
c1 + c2                         # → 新 Counter，对应 key 加；丢负值/零
c1 - c2                         # → 新 Counter，对应 key 减；★ 只保留正值！
c1 & c2                         # → min（交集）
c1 | c2                         # → max（并集）
sum(cnt.values())               # → 总数
```

**坑：** `c1 - c2` 只保留正值——要带负值用普通 dict 或 `c1.subtract(c2)`。

### defaultdict（自动初始化）

```python
from collections import defaultdict
groups = defaultdict(list)              # 工厂函数：缺 key 时调它生成默认值
groups[k].append(x)                     # 不用先判断 k 是否存在

cnt = defaultdict(int)                  # int() == 0
cnt[k] += 1                             # 默认 0 起步

neighbors = defaultdict(set)
neighbors[u].add(v)
```

---

## 4. set（集合）

```python
s = {1, 2, 3}                   # 字面量
s = set()                       # ★ 空 set 必须用 set()；{} 是空 dict
s = set([1, 2, 2])              # → {1, 2} 去重
s = set("abc")                  # → {'a', 'b', 'c'}
len(s)                          # → int

# 增
s.add(x)                        # → None [原地] 加单个（已存在不报错）
s.update(iterable)              # → None [原地] 批量加；== s |= set(iter)

# 删
s.remove(x)                     # → None [原地] [抛 KeyError 不存在] ★
s.discard(x)                    # → None [原地] 不存在静默忽略（更常用）
s.pop()                         # → 任意一个元素 [原地] [抛 KeyError 空]；★ 无序
s.clear()                       # → None [原地]

# 查
x in s                          # → bool O(1)

# 集合运算（不修改 a/b，返回新 set）
a | b                           # → 新 set 并集（union）
a & b                           # → 新 set 交集（intersection）
a - b                           # → 新 set 差集（a 有 b 没）
a ^ b                           # → 新 set 对称差（任一独有）

# 关系判断
a <= b                          # → bool a ⊆ b
a < b                           # → bool a 真子集 b
a.isdisjoint(b)                 # → bool 无交集

# 推导
{x * 2 for x in nums}           # → set 推导（花括号 + 无冒号 = set 而非 dict）

# 不可变版（可作 dict key / set 元素）
frozenset([1, 2, 3])            # → frozenset({1, 2, 3})
```

**坑：**
- `{}` 是空 dict，**空 set 必须 `set()`**
- `s.remove(x)` 元素不存在抛 `KeyError`——要安全删用 `s.discard(x)`
- set 元素必须 hashable：list / dict / set **不能**放进 set；要装就用 tuple / frozenset
- set **无序**，别假设遍历顺序

---

## 5. deque（双端队列）

```python
from collections import deque

q = deque()                     # 空 deque
q = deque([1, 2, 3])            # 初始化
q = deque(maxlen=5)             # 限长，满了从另一端挤掉

len(q)                          # → int
q[0]                            # → 头部元素，不弹（peek）
q[-1]                           # → 尾部元素，不弹

# 两端读写（全 O(1)）
q.append(x)                     # → None [原地] 右端入
q.appendleft(x)                 # → None [原地] 左端入
q.pop()                         # → 右端元素 [原地] [抛 IndexError 空]
q.popleft()                     # → 左端元素 [原地] [抛 IndexError 空] ★ BFS 用这个

# 其它
q.extend(iter)                  # → None [原地] 批量右端入
q.extendleft(iter)              # → None [原地] 批量左端入（顺序倒过来）
q.rotate(n)                     # → None [原地] 循环右移 n（负数左移）
q.reverse()                     # → None [原地]
q.clear()                       # → None [原地]
```

**用途**：BFS 队列、滑动窗口最大值（单调队列）、LRU 缓存。**别用 `list.pop(0)`，O(n) 退化**。

---

## 6. heapq（最小堆）

⚠ `heapq` **只有小顶堆**。要大顶堆 → 存负数 / 重写比较。

```python
import heapq

h = []                                  # 普通 list 当堆
heapq.heapify(arr)                      # → None [原地] O(n) 把现有 list 整成堆

# 增 / 删 / 看
heapq.heappush(h, x)                    # → None [原地] O(log n) 推入
heapq.heappop(h)                        # → 最小元素 [原地] O(log n) [抛 IndexError 空]
h[0]                                    # → 最小元素，不弹（peek）O(1)

# 复合操作（比单独 push+pop 更快）
heapq.heappushpop(h, x)                 # → 推入 x 然后弹最小；x 比堆顶小则等价不动
heapq.heapreplace(h, x)                 # → 弹最小然后推入 x；★ 堆必须非空

# TopK（一次性查询，不需要维护堆）
heapq.nlargest(k, iter, key=None)       # → 新 list，K 大降序
heapq.nsmallest(k, iter, key=None)      # → 新 list，K 小升序

# 多路归并
heapq.merge(*iters, key=None, reverse=False)  # → 迭代器，懒合并多个有序序列
```

**模式**：
- **大顶堆** → 存 `-x`，弹时 `-` 还原
- **元组比较** → 按字典序：`heappush(h, (priority, item))` 按 priority 排
- **TopK 第 k 大** → 维护**大小为 k 的小顶堆**，堆顶就是答案

---

## 7. bisect（二分插入 / 查找）

要求**数组已升序排列**。

```python
import bisect

arr = [1, 3, 5, 7, 9]

# 查找插入位置（arr 不变）
bisect.bisect_left(arr, x)              # → int 最左插入位（== 第一个 ≥ x 的下标）
bisect.bisect_right(arr, x)             # → int 最右插入位（== 第一个 > x 的下标）
bisect.bisect(arr, x)                   # → == bisect_right

# 边界
bisect.bisect_left([1,3,5,7,9], 5)      # == 2 （已存在 5，插它前面）
bisect.bisect_right([1,3,5,7,9], 5)     # == 3 （已存在 5，插它后面）
bisect.bisect_left([1,3,5,7,9], 4)      # == 2 （不存在，插应有位置）
bisect.bisect_left([1,3,5,7,9], 0)      # == 0 （比所有小）
bisect.bisect_left([1,3,5,7,9], 100)    # == 5 （比所有大，== len）

# 插入并保持有序 [原地，O(n) 因为元素要移动]
bisect.insort_left(arr, x)              # → None
bisect.insort_right(arr, x)             # → None ★ 重复值插在已有后

# Py3.10+ 才有 key 参数：bisect_left(arr, x, key=lambda a: a.val)
```

### 高频模式

```python
# 判断 x 是否存在
i = bisect.bisect_left(arr, x)
exists = i < len(arr) and arr[i] == x

# 计数 ≤ x 的元素
count = bisect.bisect_right(arr, x)

# 计数闭区间 [lo, hi] 的元素
count = bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)

# LIS O(n log n)
tails = []
for x in nums:
    i = bisect.bisect_left(tails, x)
    if i == len(tails): tails.append(x)
    else: tails[i] = x
# len(tails) == 最长严格递增子序列长度
```

**坑：** arr 没排序 → 结果错乱不报错；`insort` O(n) 高频插入用 `SortedList`。

---

## 8. 字符串

字符串**不可变**——所有"修改"都返回新字符串。

```python
s = "Hello"
len(s)                          # → int
s[0]                            # → 'H'（单字符也是 str）
s[1:4]                          # → "ell" 切片

# 大小写 / 空白（返回新 str）
s.lower() / .upper()            # → 新 str
s.title() / .capitalize()       # → 新 str
s.swapcase()                    # → 大小写互换
s.strip()                       # → 新 str（两端空白）
s.strip("xyz")                  # → 新 str（两端任意 x/y/z）
s.lstrip() / .rstrip()          # → 新 str（只剥一侧）

# 查找
s.find(sub)                     # → 首次出现下标，**不存在返回 -1**（不抛）
s.rfind(sub)                    # → 末次出现下标 / -1
s.index(sub)                    # → 同 find，但不存在 [抛 ValueError]
s.count(sub)                    # → 出现次数 int（不重叠）
sub in s                        # → bool

# 判断（返回 bool）
s.startswith(prefix)            # / 元组 tuple of prefixes 也行
s.endswith(suffix)
s.isdigit()                     # 全部数字
s.isalpha()                     # 全部字母
s.isalnum()                     # 字母或数字
s.isspace()                     # 全空白
s.isupper() / .islower()

# 替换 / 切分 / 拼接
s.replace(old, new)             # → 新 str，全替换
s.replace(old, new, count=1)    # → 新 str，最多替 count 次
s.split()                       # → list[str]，默认按空白切
s.split(",")                    # → list[str]，按 , 切
s.split(",", maxsplit=2)        # → 最多切 maxsplit+1 段
sep.join(iterable)              # → 新 str，用 sep 拼接（必须全 str）

# 编码
ord('a')                        # → 97 (字符 → ASCII/Unicode int)
chr(97)                         # → 'a' (int → 字符)
```

### 字符串 ↔ 其他类型 ★（0049 核心）

```python
# str ↔ 字符 list
list("abc")                     # → ['a', 'b', 'c']
"".join(['a', 'b', 'c'])        # → "abc"
"-".join(['a', 'b', 'c'])       # → "a-b-c"

# str ↔ 词 list
"hello world".split()           # → ['hello', 'world']  默认按任何空白切
"a,b,,c".split(",")             # → ['a', 'b', '', 'c']  保留空段
"a,b,c".split(",", maxsplit=1)  # → ['a', 'b,c']         限切次数
" ".join(['hello', 'world'])    # → "hello world"

# str ↔ int / float
int("42")                       # → 42      [抛 ValueError 格式错]
str(42)                         # → "42"
float("3.14")                   # → 3.14
int("ff", 16)                   # → 255     按 16 进制解析
int("101", 2)                   # → 5       按 2 进制解析
bin(5)                          # → "0b101"
hex(255)                        # → "0xff"

# StringBuilder 等价（避免 O(n²) 累加）
parts = []
parts.append("x")
result = "".join(parts)         # → 新 str

# 修改某下标 → list 中转
chars = list(s)
chars[0] = 'h'
s = "".join(chars)
```

### 字符串排序 ★ 0049 招牌坑

```python
sorted("cba")                   # → ['a', 'b', 'c']  ⚠ 返回字符 list，不是 str！
"".join(sorted("cba"))          # → "abc"            想要排序字符串必须 join 回
tuple(sorted("cba"))            # → ('a', 'b', 'c')  hashable，可作 dict key

# ❌ str 没有 .sort()
"cba".sort()                    # AttributeError：str 不可变

# 异位词判同（0049 核心）
"".join(sorted(s1)) == "".join(sorted(s2))      # 字面 key
tuple(sorted(s1)) == tuple(sorted(s2))          # tuple key（省 join 一步，可直接当 dict key）
```

**坑：** `s[i] = c` 直接报 TypeError——str 不可变；累加字符串用 list + join。`s.sort()` 不存在，用 `"".join(sorted(s))`。

---

## 9. 数学 / 位运算

```python
# 整除 / 取模
a // b                          # → 整除（向下取整！-3 // 2 == -2）
a % b                           # → 取模（结果与除数同号）
divmod(a, b)                    # → (商, 余数) 元组

# 函数
abs(x)                          # → 绝对值
min(a, b, c)                    # → 多参数最小
min(iterable)                   # → 可迭代物最小 [抛 ValueError 空]
min(iter, key=lambda x: ..., default=None)   # 可加 key 和 default
max(...)                        # → 同 min
sum(iter)                       # → 求和
sum(iter, start=0)              # → 带起始值
round(x)                        # → 四舍五入到整数 ★ 银行家舍入！round(0.5)==0, round(1.5)==2
round(x, n)                     # → 保留 n 位小数
pow(a, b)                       # → a**b（同 ** 运算符）
pow(a, b, mod)                  # → (a**b) % mod 高效快速幂

# 无穷
float('inf'), float('-inf')     # → 浮点正/负无穷
import math
math.inf, -math.inf             # 同上
math.nan                        # → NaN

# math 库常用
math.gcd(a, b, *)               # → 最大公约数（Py3.9+ 可多参数）
math.lcm(a, b, *)               # → 最小公倍数（Py3.9+）
math.sqrt(x)                    # → 平方根 (float)
math.isqrt(x)                   # → 整数平方根 (int，向下取整)
math.floor(x) / math.ceil(x)    # → 向下/上取整 int
math.log(x, base=e)             # → 自然对数（可指定底）
math.log2(x) / math.log10(x)

# 位运算
x & y                           # 与
x | y                           # 或
x ^ y                           # 异或
~x                              # 按位取反（结果是 -(x+1)）
x << k                          # 左移 k 位（== x * 2**k）
x >> k                          # 右移 k 位（== x // 2**k）

bin(x)                          # → str '0b...'
oct(x) / hex(x)                 # → '0o...' / '0x...'
int('0b101', 2)                 # → 5 反向：字符串按指定进制转 int
x.bit_count()                   # → 1 的个数 (Py3.10+；老版 bin(x).count('1'))
x.bit_length()                  # → 表示 x 需要的位数
```

**坑：** Python `//` 是**向下取整**（不是向零截断）—— `-3 // 2 == -2` 而非 `-1`。要向零截断用 `int(a / b)`。

---

## 10. 类型 / 容器互转大全

刷题里 80% 的"我不会写"卡壳就是"我不知道这个怎么转那个"。一张表搞定。

### 数字 ↔ 字符串

```python
int("42")               # → 42       [抛 ValueError]
int("ff", 16)           # → 255      指定进制解析
int("101", 2)           # → 5
str(42)                 # → "42"
float("3.14")           # → 3.14
bin(5)                  # → "0b101"  转 2 进制字符串
oct(8)                  # → "0o10"
hex(255)                # → "0xff"
```

### 单字符 ↔ ASCII / Unicode

```python
ord('a')                # → 97       字符 → int
chr(97)                 # → 'a'      int → 字符
ord('a') - ord('a')     # → 0        小写字母转下标常用
```

### 字符串 ↔ list

```python
list("abc")             # → ['a', 'b', 'c']    str → 字符 list
"".join(['a','b','c'])  # → "abc"              字符 list → str
"-".join(['1','2','3']) # → "1-2-3"            带分隔符
"hi".split()            # → ['hi']             默认按空白
"a,b".split(",")        # → ['a', 'b']

# 数字 list 拼接字符串：要先转 str
"-".join(map(str, [1,2,3]))           # → "1-2-3"
"-".join(str(x) for x in [1,2,3])     # → 同上，生成器版
```

### list ↔ tuple / set / dict

```python
tuple([1, 2, 3])        # → (1, 2, 3)
set([1, 2, 2, 3])       # → {1, 2, 3}      去重
list((1, 2, 3))         # → [1, 2, 3]
list({1, 2, 3})         # → [1, 2, 3]      ⚠ 顺序不保证（set 无序）
list("abc")             # → ['a','b','c']  str 也是 iterable

# dict 解构成 list
list(d.keys())          # → 键 list
list(d.values())        # → 值 list
list(d.items())         # → [(k, v), ...]  键值对 list

# (k, v) 对 → dict
dict([("a", 1), ("b", 2)])      # → {"a": 1, "b": 2}
dict(zip(keys, values))         # → 两个 list 配对建 dict
```

### 字符串排序（异位词 0049 核心）

```python
sorted("cba")           # → ['a','b','c']   ⚠ 字符 list，不是 str
"".join(sorted(s))      # → "abc"           排序后字符串
tuple(sorted(s))        # → ('a','b','c')   排序后 tuple（可作 dict key）

# 异位词判同（哪个都行）
"".join(sorted(s1)) == "".join(sorted(s2))
tuple(sorted(s1)) == tuple(sorted(s2))
```

### Hashable 类型一览（什么能当 dict key / set 元素）★

`sorted(s)` 返回的是 **list**——而 **list 不能当 dict key**！必须先转 `tuple` 或 `str`。

| 类型 | 能 hash？ | 为啥 |
|---|---|---|
| `int` `float` `bool` `None` | ✓ | 不可变 |
| `str` | ✓ | 不可变 |
| `tuple`（元素全 hashable）| ✓ | 不可变 |
| `frozenset` | ✓ | 不可变 |
| **`list`** | **❌** | 可变 → TypeError: unhashable type |
| **`dict`** | **❌** | 可变 |
| **`set`** | **❌** | 可变 |

```python
# 想用"排序后的字符序列"当 dict key 的两种合法路子
d[tuple(sorted(s))] = ...      # tuple，省一次 join
d["".join(sorted(s))] = ...    # str，print 时更可读

# ❌ 不能直接：
d[sorted(s)] = ...             # TypeError: unhashable type: 'list'
```

**心法**：**"我想用 X 作 dict key / set 元素"** → 先检查 X 是不是 hashable。
- 是 → 直接用
- 否（list / dict / set） → 转 tuple / frozenset / json 字符串

### 数值转换汇总

```python
abs(-5)                 # → 5
round(3.5)              # → 4    ⚠ Py 3 银行家舍入：round(0.5)==0, round(1.5)==2
round(3.14, 1)          # → 3.1
int(3.7)                # → 3    截尾（向 0），不是四舍五入
math.floor(3.7)         # → 3    向下
math.ceil(3.2)          # → 4    向上
math.trunc(-3.7)        # → -3   截尾（向 0）
divmod(17, 5)           # → (3, 2)   (商, 余)
```

### 二维 / 嵌套结构

```python
# 二维 list 拷贝（详见 §2）
grid2 = [row[:] for row in grid]

# 二维 list 行列转置
list(zip(*grid))                       # → [(row0col0, row1col0, ...), ...]
                                       #    每列变 tuple
[list(col) for col in zip(*grid)]      # → 同上但内层是 list

# 字典反查（值 → 键）
{v: k for k, v in d.items()}           # ⚠ 值有重复时会丢
```

### 速查决策表

| 想要 | 写法 |
|---|---|
| 字符串排序后还是字符串 | `"".join(sorted(s))` |
| 字符串排序后当 dict key | `tuple(sorted(s))` |
| 数字 list 拼成字符串 | `"-".join(map(str, nums))` |
| 字符串拆成字符 list | `list(s)` |
| list 去重保序 | `list(dict.fromkeys(arr))` |
| list 去重不保序 | `list(set(arr))` |
| 二维独立拷贝 | `[row[:] for row in grid]` |
| 两 list 配对建 dict | `dict(zip(keys, values))` |
| dict 翻转 | `{v: k for k, v in d.items()}` |
| 二维转置 | `list(zip(*grid))` |

---

## 11. 闭包与作用域

```python
def outer():
    cnt = 0
    nums = []
    def inner():
        nonlocal cnt            # ★ 修改外层变量必须 nonlocal
        cnt += 1                # 重新赋值 → 需要 nonlocal
        nums.append(cnt)        # 修改容器内容 → 不需要 nonlocal
    inner()
    return cnt, nums
```

**详细机制 / 4 种模式 / 决策树**：见 [PYTHON_SHORTCUTS.md § 闭包替代 self.xxx](PYTHON_SHORTCUTS.md)。

---

## 12. 类型注解（LeetCode 标准签名）

```python
from typing import List, Optional, Tuple, Dict, Set

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
    def buildTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ...
```

`Optional[X]` == `X | None`（Py3.10+）；LeetCode 仍用 `Optional` 风格。

---

## 13. 链表 / 树节点模板（LeetCode 风格）

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

模板里已经预置，直接用。

---

## 14. 常用速记（一行流）

```python
# 枚举：拿下标和值
for i, x in enumerate(arr): ...
for i, x in enumerate(arr, start=1): ...        # start 改起始下标

# 并行遍历
for a, b in zip(arr1, arr2): ...                # 短的为准
for a, b in zip(arr1, arr2, strict=True): ...   # Py3.10+ 长度不等抛错

# 任意 / 全部
any(x > 0 for x in arr)                         # → bool 有正
all(x > 0 for x in arr)                         # → bool 全正

# 列表推导
[x*2 for x in arr if x > 0]                     # → 新 list 过滤+变换

# 解包
a, b = b, a                                     # 交换
first, *rest = [1,2,3,4]                        # first=1, rest=[2,3,4]
a, *_, c = [1,2,3,4]                            # 只要首尾

# 字典反查
{v: k for k, v in d.items()}
```

更多 Pythonic 写法见 [PYTHON_SHORTCUTS.md](PYTHON_SHORTCUTS.md)。

---

## 15. 递归限制

```python
import sys
sys.setrecursionlimit(10**6)            # 默认约 1000 层，链表/深树要加
```

---

## 16. 调试技巧

```python
print(f"{i=} {res=}")                   # → "i=3 res=42"，Py3.8+ 自带标签
from pprint import pprint
pprint(grid)                            # → 格式化打印嵌套结构
import json; print(json.dumps(obj, indent=2, ensure_ascii=False))   # JSON 风格
```

LeetCode 本地模板自带 `test()` 跑用例 + PASS/FAIL 输出，直接 `python xxxx.py` 验证。
