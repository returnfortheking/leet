# 12 堆 / TopK

## 核心思路

**触发器**：题面出现「**前 K 大 / 前 K 小 / 第 K 大**」、「**数据流求中位数**」、「**合并 K 个有序结构**」、「**调度 / 任务排序按优先级**」。

Python 的 `heapq` 只有**小顶堆**，要大顶堆就**存负数**。

| 解法 | 时间 | 适用 |
|---|---|---|
| 排序 | O(n log n) | n 不大或要全排 |
| **大小为 K 的堆** | O(n log K) | TopK，n 大 K 小（最常用）|
| 快速选择（quickselect） | O(n) 期望 | 第 K 大，不需要返回顺序 |

## 必背模板

### 1) 大小为 K 的堆找第 K 大

```python
import heapq

def find_kth_largest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, x)
        if len(h) > k:
            heapq.heappop(h)        # 弹出当前最小
    return h[0]                     # 堆顶 = 第 K 大
```

记忆：要"第 K 大"，维护"大小为 K 的**小顶堆**"，堆顶就是答案。  
要"第 K 小"，维护"大小为 K 的**大顶堆**"。

### 2) 前 K 高频元素 #347

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    cnt = Counter(nums)
    return heapq.nlargest(k, cnt.keys(), key=lambda x: cnt[x])
    # 也可以：return [v for v, _ in cnt.most_common(k)]
```

### 3) 合并 K 个有序链表 #23

```python
import heapq

def merge_k_lists(lists):
    h = []
    for i, head in enumerate(lists):
        if head:
            heapq.heappush(h, (head.val, i, head))   # (val, idx, node)，idx 防 val 相等时比 node 报错
    dummy = ListNode()
    tail = dummy
    while h:
        _, i, node = heapq.heappop(h)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(h, (node.next.val, i, node.next))
    return dummy.next
```

**坑**：tuple 比较到 `node` 时 Python 会调用 `<`，节点没定义比较器会报错。所以加一个 idx 占位。

### 4) 数据流中位数（双堆 #295）

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.lo = []     # 大顶堆（存负数），存较小的一半
        self.hi = []     # 小顶堆，存较大的一半

    def addNum(self, num):
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))   # 把 lo 最大值丢给 hi
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

不变量：`len(lo) >= len(hi)` 且 `len(lo) - len(hi) <= 1`。

### 5) 快速选择（quickselect）

```python
import random

def quick_select(nums, k):       # 返回第 k 大
    def partition(l, r, pivot_idx):
        pivot = nums[pivot_idx]
        nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
        store = l
        for i in range(l, r):
            if nums[i] > pivot:                # 大的放左 → 找第 k 大
                nums[store], nums[i] = nums[i], nums[store]
                store += 1
        nums[store], nums[r] = nums[r], nums[store]
        return store

    l, r = 0, len(nums) - 1
    target = k - 1
    while l <= r:
        p = partition(l, r, random.randint(l, r))
        if p == target: return nums[p]
        if p < target: l = p + 1
        else: r = p - 1
    return -1
```

## 易错点

- **Python heapq 是小顶堆**。要大顶堆存 `-x`。
- **元组比较**到非可比对象会抛错，加 idx 占位。
- **`heapq.heappushpop`** 比 push 后 pop 快 50%（少一次 sift）。
- **TopK 的小顶堆容量 = K**：超过 K 才弹出。

## 高频题

1. #215 数组中第 K 大 ★（堆 / 快选两种解法都要会）
2. #347 前 K 高频元素 ★
3. #692 前 K 高频单词
4. #295 数据流的中位数 ★
5. #23 合并 K 个有序链表 ★
6. #378 有序矩阵中第 K 小
7. #973 最接近原点的 K 个点
8. #767 重构字符串（堆调度）
9. #1046 最后一块石头的重量
