# 07 DFS / BFS

## 核心思路

DFS 和 BFS 都是图/网格/树的**遍历**算法。题面给你一个图状结构，让你"找到 X / 数清 X / 走到 X"，几乎都能套这两个之一。

| 选哪个 | 触发器 |
|---|---|
| BFS | 「**最短**路径 / 最少步数 / 最少层」+ 边权全为 1 |
| DFS | 「**所有可能** / 计数 / 染色 / 拓扑后序」 |
| 都行 | 简单连通性、计数岛屿（DFS 写起来短） |

**网格题**最常考。把每个格子看成节点，相邻 4/8 格为边。

## 必背模板

### 1) 网格 DFS（岛屿数量）

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid: return 0
    m, n = len(grid), len(grid[0])

    def dfs(r: int, c: int) -> None:
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '0'                        # 标记访问
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc)

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
    return count
```

### 2) 网格 BFS（多源 / 最短）

```python
from collections import deque

def shortest(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    q = deque()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == SOURCE:
                q.append((r, c, 0))             # (r, c, dist)
    visited = {(r, c) for r, c, _ in q}
    while q:
        r, c, d = q.popleft()
        if grid[r][c] == TARGET:
            return d
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                visited.add((nr, nc))
                q.append((nr, nc, d + 1))
    return -1
```

### 3) BFS 按层（同时知道层号）

```python
def bfs_levels(start):
    q = deque([start])
    visited = {start}
    step = 0
    while q:
        for _ in range(len(q)):       # 处理整层
            node = q.popleft()
            if is_target(node):
                return step
            for nxt in neighbors(node):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
        step += 1
    return -1
```

### 4) 双向 BFS（搜索空间巨大时）

从起点和终点同时往中间扩展，相遇即停。能把 O(b^d) 降到 O(b^(d/2))。

```python
def double_bfs(start, end, neighbors):
    if start == end: return 0
    front, back = {start}, {end}
    visited = {start, end}
    step = 0
    while front and back:
        step += 1
        if len(front) > len(back):
            front, back = back, front
        nxt_front = set()
        for node in front:
            for nb in neighbors(node):
                if nb in back: return step
                if nb not in visited:
                    visited.add(nb)
                    nxt_front.add(nb)
        front = nxt_front
    return -1
```

## 易错点

- **必须 `deque`**，不能用 list 当队列。
- **入队时立刻标记 visited**，不要"出队再标"，否则会重复入队。
- **方向数组**：`((1,0),(-1,0),(0,1),(0,-1))` 写成元组比 list 略快。
- **递归爆栈**：网格 1000×1000 可能 DFS 爆栈，要么 BFS，要么 `sys.setrecursionlimit`。

## 高频题

1. #200 岛屿数量 ★（DFS 模板题）
2. #695 岛屿的最大面积
3. #463 岛屿的周长
4. #130 被围绕的区域
5. #994 腐烂的橘子 ★（多源 BFS）
6. #127 单词接龙 ★（BFS / 双向 BFS）
7. #752 打开转盘锁（BFS 状态空间）
8. #111 二叉树最小深度（BFS 找到第一个叶子）
9. #79 单词搜索（DFS + 回溯）
10. #417 太平洋大西洋水流问题（反向 DFS）
