# 14 图论

## 核心思路

图论题在大厂面试出现频率不算最高（除外企外），但**拓扑排序、Dijkstra、并查集** 是必会基本盘。

| 问题 | 算法 | 时间 |
|---|---|---|
| 有向图是否成环 / 课程依赖 | 拓扑排序（Kahn / DFS） | O(V+E) |
| 单源最短路（边权非负） | Dijkstra（堆） | O((V+E) log V) |
| 单源最短路（含负边） | Bellman-Ford / SPFA | O(VE) |
| 有限步数最短路 | Bellman-Ford | O(KE) |
| 最小生成树 | Kruskal（UF）/ Prim（堆） | O(E log E) |
| 连通性 / 最短路（无权） | BFS | O(V+E) |

## 必背模板

### 1) 拓扑排序（Kahn / BFS）

```python
from collections import defaultdict, deque

def topo_sort(num, prerequisites):
    graph = defaultdict(list)
    indeg = [0] * num
    for a, b in prerequisites:        # b -> a
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num) if indeg[i] == 0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num else []   # 长度不够 = 有环
```

### 2) Dijkstra（堆优化）

```python
import heapq

def dijkstra(n, edges, src):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        # graph[v].append((u, w))      # 无向图加这行
    dist = [float('inf')] * n
    dist[src] = 0
    pq = [(0, src)]                     # (current dist, node)
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue        # 过期记录，跳过
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist
```

### 3) Bellman-Ford（K 步内最短路 #787）

```python
def find_cheapest_price(n, flights, src, dst, k):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(k + 1):                  # 最多 K 次中转 = K+1 条边
        new_dist = dist[:]
        for u, v, w in flights:
            if dist[u] + w < new_dist[v]:
                new_dist[v] = dist[u] + w
            # ★ 必须用 dist 不是 new_dist，避免一次循环松弛多次
        dist = new_dist
    return dist[dst] if dist[dst] != float('inf') else -1
```

### 4) Kruskal MST（用上一节的 UnionFind）

```python
def min_cost_connect(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((d, i, j))
    edges.sort()
    uf = UnionFind(n)
    cost = 0
    for w, u, v in edges:
        if uf.union(u, v):
            cost += w
    return cost
```

## 易错点

- **Dijkstra 不能处理负边**。题面有负边一定不能用，要 Bellman-Ford。
- **Dijkstra 弹出过期记录**：`if d > dist[u]: continue` 是优化关键。
- **Bellman-Ford 步数限制**：`new_dist = dist[:]` 这步不能省，否则一轮里多次松弛。
- **拓扑排序判环**：最后看 `len(order) == n`，不是 `q` 是否空。

## 高频题

1. #207 课程表 ★（拓扑判环）
2. #210 课程表 II ★（输出顺序）
3. #743 网络延迟时间 ★（Dijkstra 模板）
4. #787 K 站中转最便宜航班 ★（Bellman-Ford）
5. #1631 最小体力消耗（Dijkstra 变形 / 二分 + BFS）
6. #1584 连接所有点的最小费用 ★（MST）
7. #399 除法求值（带权图 BFS / 带权并查集）
8. #802 找到最终的安全状态（反图拓扑）
