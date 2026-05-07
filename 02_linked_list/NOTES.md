# 02 链表

## 核心思路

链表题难在**指针操作**，但套路只有几个：

| 题面特征 | 套路 |
|---|---|
| 反转 / 部分反转 / K 个一组反转 | 三指针迭代反转 |
| 找中点 / 判环 / 倒数第 K | 快慢指针 |
| 合并 / 删除 | 虚拟头结点 dummy |
| 复杂结构（带 random、深拷贝） | 哈希表 / 原地穿插 |

**铁律**：链表题永远先想要不要 dummy（虚拟头结点）。如果**头结点可能变**或**统一删除逻辑**，dummy 必加。

## 必背模板

### 1) 反转链表（迭代）

```python
def reverse(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next      # 1. 暂存下一个
        cur.next = prev     # 2. 反指
        prev = cur          # 3. prev 前进
        cur = nxt           # 4. cur 前进
    return prev
```

### 2) 快慢指针找中点

```python
def middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow  # 偶数节点时返回靠右的中点
```

### 3) Floyd 判环（环形入口）

```python
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:               # 相遇
            slow = head
            while slow is not fast:    # 双指针同速找入口
                slow, fast = slow.next, fast.next
            return slow
    return None
```

### 4) 虚拟头结点合并

```python
def merge(l1, l2):
    dummy = ListNode()
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

### 5) K 个一组反转（高频中的高频）

```python
def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next     # 不足 k，保持原样
        group_next = kth.next
        # 反转 [group_prev.next, kth]
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        # 把反转好的段接回
        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
```

## 易错点（TS → Python）

- **`is` vs `==`**：判断节点是不是同一个对象用 `is`，比 TS 的 `===` 更直接。
- **None 检查**：`while node` 等价于 `while node is not None`。
- **多重赋值 `a, b = b, a.next`**：右侧整体先求值，**很方便**做 `prev/cur` 同时推进。
- 忘加 `dummy.next` 是最经典的 bug：返回的不是答案。

## 高频题

1. #206 反转链表 ★（必背）
2. #92 反转链表 II ★（部分反转）
3. #25 K 个一组翻转 ★（大厂面试反复出现）
4. #21 合并两个有序链表
5. #23 合并 K 个有序链表（→ 堆 / 分治）
6. #141 环形链表
7. #142 环形链表 II（Floyd）
8. #160 相交链表（双指针走两遍）
9. #19 删除倒数第 N 个节点（dummy + 快慢）
10. #2 两数相加（高位低位翻转）
11. #138 复制带随机指针的链表 ★（哈希 / 穿插）
12. #148 排序链表（归并）
