# 16 设计题

## 核心思路

设计题要求实现一个支持特定操作的"数据结构"。核心是**用合适的容器组合达到要求的复杂度**。

**触发器**：题面是"实现一个 X 类，要求 add/get/remove 都是 O(1)"。

| 题 | 关键组合 |
|---|---|
| LRU 缓存 #146 | 双向链表 + 哈希；或 Python `OrderedDict` |
| LFU 缓存 #460 | 哈希 + 双向链表（按频次分桶） |
| Trie #208 | 嵌套字典 / 数组 26 |
| O(1) 插入删除随机 #380 | list + 哈希（值 → 下标）|
| 数据流中位数 #295 | 大顶堆 + 小顶堆 |
| 最小栈 #155 | 主栈 + 辅助单调最小栈 |
| 用栈实现队列 #232 | 两个栈：入/出 |

## 必背模板

### 1) LRU 缓存（最常考）

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)            # 访问后挪到末尾（最新）
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)     # 弹出最旧（队头）
```

**面试官如果禁用 OrderedDict**：手写双向链表 + 哈希。

```python
class Node:
    __slots__ = ('k', 'v', 'prev', 'next')
    def __init__(self, k=0, v=0):
        self.k, self.v = k, v
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache: dict[int, Node] = {}
        self.head, self.tail = Node(), Node()      # 哑头/哑尾
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove(node); self._add_to_front(node)
        return node.v

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.v = value
            self._remove(node); self._add_to_front(node)
        else:
            if len(self.cache) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.k]
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)
```

### 2) Trie

```python
class Trie:
    def __init__(self):
        self.root: dict = {}
        self.END = '$'

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            cur = cur.setdefault(ch, {})
        cur[self.END] = True

    def search(self, word: str) -> bool:
        cur = self.root
        for ch in word:
            if ch not in cur: return False
            cur = cur[ch]
        return self.END in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for ch in prefix:
            if ch not in cur: return False
            cur = cur[ch]
        return True
```

### 3) O(1) 时间插入删除随机访问 #380

```python
import random

class RandomizedSet:
    def __init__(self):
        self.arr: list[int] = []
        self.idx: dict[int, int] = {}        # value -> index

    def insert(self, val: int) -> bool:
        if val in self.idx: return False
        self.idx[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx: return False
        i = self.idx[val]
        last = self.arr[-1]
        self.arr[i] = last
        self.idx[last] = i
        self.arr.pop()
        del self.idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
```

技巧：**删除时把最后一个元素换到要删的位置**，避免 list 中间删导致 O(n)。

### 4) 最小栈 #155

```python
class MinStack:
    def __init__(self):
        self.stack: list[tuple[int, int]] = []   # (val, current_min)

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self): self.stack.pop()
    def top(self): return self.stack[-1][0]
    def getMin(self): return self.stack[-1][1]
```

### 5) 用栈实现队列 #232

```python
class MyQueue:
    def __init__(self):
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x): self.in_stack.append(x)

    def pop(self):
        self._move()
        return self.out_stack.pop()

    def peek(self):
        self._move()
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

    def _move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
```

均摊 O(1)：每个元素最多在 in_stack/out_stack 各转移一次。

## 易错点

- **LRU 必须双向链表**：单向不行，因为删一个节点要 O(1) 改前驱的 next，必须知道前驱。
- **Trie 用嵌套 dict** 写起来比 26 数组短得多，面试推荐 dict。
- **#380 删除技巧**：换最后一个，不是真的中间删。
- **OrderedDict 在 Python 里**：`move_to_end` / `popitem(last=False)` 是 LRU 的标准武器。

## 高频题

1. #146 LRU 缓存 ★（必刷必背）
2. #460 LFU 缓存 ★（难，但大厂常考）
3. #208 实现 Trie ★
4. #211 添加与搜索单词
5. #295 数据流中位数 ★（→ 12 堆专题）
6. #380 O(1) 时间插入删除随机
7. #381 含重复 O(1) 时间插入删除随机
8. #155 最小栈
9. #232 用栈实现队列
10. #225 用队列实现栈
11. #707 设计链表
