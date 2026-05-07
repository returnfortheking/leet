# 10 贪心

## 核心思路

贪心 = **每一步都做局部最优选择，且能证明合得起来是全局最优**。

**贪心 vs DP 的区别**：DP 枚举所有选择再求最优；贪心直接挑当前最好的就走人。能贪则贪（O(n)），不能贪退化为 DP（O(n²+)）。

**触发器**：
- 题目允许「任意顺序操作」/「随便挑」
- 出现「最少 / 最多 / 至多」+ 没有明显的子结构依赖
- 区间题（合并 / 安排会议 / 删区间）

**警告**：贪心容易"看似对实则错"。AC 之前必须找一两个小用例验证；遇到"反例能否构造"的疑虑，宁可改 DP。

## 必背套路

### 1) 区间贪心（按右端点排序）

```python
# 无重叠区间 #435
def erase_overlap(intervals):
    intervals.sort(key=lambda x: x[1])    # 按右端点
    end = -float('inf')
    keep = 0
    for l, r in intervals:
        if l >= end:
            keep += 1
            end = r
    return len(intervals) - keep
```

凡是「区间不重叠最多 / 最少删除 / 最少箭射爆」都用这个：**右端点早的先选**，给后面留空间。

### 2) 跳跃游戏（维护可达边界）

```python
# #55
def can_jump(nums):
    far = 0
    for i, x in enumerate(nums):
        if i > far: return False
        far = max(far, i + x)
    return True

# #45 最少跳跃次数
def jump(nums):
    far = end = step = 0
    for i in range(len(nums) - 1):
        far = max(far, i + nums[i])
        if i == end:
            step += 1
            end = far
    return step
```

### 3) 加油站（一次扫描）

```python
# #134
def can_complete_circuit(gas, cost):
    total = tank = start = 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        total += diff
        tank += diff
        if tank < 0:                # 从 start 出发到 i 不行
            start = i + 1           # 跳过中间所有点
            tank = 0
    return start if total >= 0 else -1
```

### 4) 双向扫描（分糖果 #135）

很多"两个约束都要满足"的贪心题：从左扫一遍只满足一边，再从右扫一遍叠加。

```python
def candy(ratings):
    n = len(ratings)
    c = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            c[i] = c[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            c[i] = max(c[i], c[i + 1] + 1)
    return sum(c)
```

### 5) 排序+贪心（重建队列 #406）

```python
def reconstruct_queue(people):
    people.sort(key=lambda p: (-p[0], p[1]))    # 高的在前；同高按 k 升序
    res = []
    for p in people:
        res.insert(p[1], p)
    return res
```

## 贪心证明思路

面试时如果面试官追问"为什么贪心对"：
- **交换论证**：任意一个最优解，把它的某步替换成贪心选择，结果不会更差。
- **数学归纳**：前 i 步贪心保持"最优前缀"，归纳到 i+1。

不会证就别说出来，先写代码 + 给反例验证。

## 高频题

1. #55 跳跃游戏 ★
2. #45 跳跃游戏 II ★
3. #134 加油站
4. #135 分发糖果
5. #435 无重叠区间 ★
6. #452 用最少箭头射爆气球
7. #406 根据身高重建队列 ★
8. #56 合并区间（排序+贪心，也算）
9. #763 划分字母区间
10. #11 盛最多水的容器（贪心移动短板）
