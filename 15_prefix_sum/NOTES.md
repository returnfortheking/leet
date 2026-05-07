# 15 前缀和 / 差分

## 核心思路

**前缀和**：把"区间求和"从 O(n) 降到 O(1)。
**差分**：把"区间增减"从 O(n) 降到 O(1)。

它们是对偶操作：差分数组的前缀和 = 原数组。

**触发器**：
- 「**子数组和等于 K** / 能被 K 整除」→ 前缀和 + 哈希
- 「**多次区间加减某值**，最后查询某点」→ 差分
- 「频繁查询区间和」→ 一维 / 二维前缀和

## 必背模板

### 1) 一维前缀和

```python
# 区间 [l, r] 的和
prefix = [0] * (n + 1)
for i, x in enumerate(nums):
    prefix[i + 1] = prefix[i] + x
# 查询：sum[l..r] = prefix[r + 1] - prefix[l]
```

### 2) 二维前缀和

```python
# 矩阵区域和（左上 (r1,c1)，右下 (r2,c2)）
m, n = len(mat), len(mat[0])
ps = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m):
    for j in range(n):
        ps[i + 1][j + 1] = ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + mat[i][j]
# 查询
def query(r1, c1, r2, c2):
    return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]
```

### 3) 前缀和 + 哈希（核心套路）

**子数组和等于 K (#560)**：

```python
def subarray_sum(nums, k):
    cnt = {0: 1}     # 前缀和 -> 出现次数；初始有一个空前缀和 0
    s = ans = 0
    for x in nums:
        s += x
        ans += cnt.get(s - k, 0)        # 之前出现过的某个前缀和与当前前缀和差 k → 一段子数组和 = k
        cnt[s] = cnt.get(s, 0) + 1
    return ans
```

**模板心法**：把"子数组 sum == K"翻译成"两个前缀和差 == K"。
- 推广到「能被 K 整除」(#974)：键存 `s % k`，注意负数取模
- 推广到「奇偶性 / 0-1 数量相等」(#525)：把 0 当作 -1，求"前缀和相等"

### 4) 差分数组

```python
# 多次区间加：[l, r] 区间 += val
diff = [0] * (n + 1)
for l, r, val in operations:
    diff[l] += val
    diff[r + 1] -= val
# 还原
result = [0] * n
result[0] = diff[0]
for i in range(1, n):
    result[i] = result[i - 1] + diff[i]
```

应用：#1109 航班预订统计、#1094 拼车。

### 5) 树上前缀和（#437）

二叉树从根到当前节点的前缀和 + 哈希计数：

```python
def path_sum(root, target):
    cnt = {0: 1}                # 路径前缀和 -> 次数
    ans = 0
    def dfs(node, cur):
        nonlocal ans
        if not node: return
        cur += node.val
        ans += cnt.get(cur - target, 0)
        cnt[cur] = cnt.get(cur, 0) + 1
        dfs(node.left, cur)
        dfs(node.right, cur)
        cnt[cur] -= 1            # ★ 回溯：离开此节点时撤销
    dfs(root, 0)
    return ans
```

## 易错点

- **前缀和数组下标偏移 1**：`prefix[i+1]` 对应 `nums[0..i]` 的和；省得处理 `i = 0` 边界。
- **哈希要预置 `{0: 1}`**：表示空前缀。漏了这一项，从下标 0 开始的子数组就漏算。
- **二维前缀和容斥**：加左上、减重叠（左 + 上 - 左上）。
- **差分末尾 -=**：`diff[r+1] -= val` 而不是 `diff[r] -= val`。

## 高频题

1. #303 区域和检索 - 一维（模板）
2. #304 二维区域和（二维模板）
3. #560 和为 K 的子数组 ★（前缀和+哈希经典）
4. #974 和可被 K 整除的子数组 ★
5. #525 连续数组（0/1 → -1/+1）
6. #523 连续的子数组和
7. #1109 航班预订统计 ★（差分）
8. #1094 拼车（差分）
9. #437 路径总和 III ★（树上前缀和）
10. #238 除自身以外数组的乘积（前缀积/后缀积）
