# 13 并查集 (Union-Find / DSU)

## 核心思路

并查集是处理「**动态连通性**」问题的数据结构：
- 给一堆元素，支持两个操作：
  - `union(a, b)`：把 a 和 b 所在的集合合并
  - `find(x)`：返回 x 所在集合的代表元

**触发器**：
- 「**有多少连通分量**」/ 「a 和 b 是否连通」/ 「合并后是否成环」
- 图问题，但**动态加边**而不是一次性给图（典型场景）
- 等价类问题（等式、字符串等价）

时间复杂度：单次操作近 O(α(n)) ≈ O(1)（含路径压缩 + 按秩合并）。

## 必背模板

```python
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n        # 连通分量数

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]   # 路径压缩（半压缩）
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False     # 已连通，没有合并
        # 按秩合并
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

    def connected(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)
```

## 用法套路

### 1) 计数连通分量

```python
def num_provinces(is_connected):
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j] == 1:
                uf.union(i, j)
    return uf.count
```

### 2) 检测环（无向图）

```python
def find_redundant(edges):
    uf = UnionFind(len(edges) + 1)
    for u, v in edges:
        if not uf.union(u, v):    # 已连通再加边 = 成环
            return [u, v]
    return []
```

### 3) 网格转 1D（行 r 列 c → r*n+c）

```python
def num_islands(grid):
    m, n = len(grid), len(grid[0])
    uf = UnionFind(m * n)
    water = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '0':
                water += 1
                continue
            for dr, dc in ((1, 0), (0, 1)):     # 只看右、下，避免重复
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    uf.union(r * n + c, nr * n + nc)
    return uf.count - water
```

### 4) 等式方程组（#990）

把每个字符映射到一个并查集编号。
- 第一遍：`==` 的两边 union
- 第二遍：`!=` 的两边检查是否已 connected，是 → 矛盾返回 False

## 易错点

- **路径压缩有两种写法**：
  - 半压缩（while 写法）：每步把节点指向祖父
  - 全压缩（递归写法）：所有节点直接指向根。递归在深树上可能爆栈，面试推荐 while 版。
- **count 的维护**：union 成功（之前不连通）才 -1。
- **网格题**：注意只 union 右和下，避免重复 union 把 count 算错（但因为 union 内部去重了，多 union 也无错，只是浪费）。

## 高频题

1. #547 省份数量 ★（模板）
2. #200 岛屿数量（UF 解法 / DFS 解法都会）
3. #684 冗余连接 ★
4. #685 冗余连接 II（有向版，难）
5. #990 等式方程的可满足性 ★
6. #128 最长连续序列（UF 或 set，set 解法更经典）
7. #721 账户合并
8. #399 除法求值（带权 UF）
