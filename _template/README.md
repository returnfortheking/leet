# 题解模板使用说明

## 新建一道题

```bash
# 假设要刷 #15 三数之和，归在 04_two_pointers
cp _template/solution_template.py 04_two_pointers/0015_three_sum.py
```

文件命名规范：`<4 位题号>_<英文短名>.py`，例如：
- `0001_two_sum.py`
- `0146_lru_cache.py`
- `0023_merge_k_sorted_lists.py`

## 模板要做的修改

1. 顶部 docstring：填题目链接、描述、约束、思路、复杂度
2. 如果题目要求链表 / 二叉树，取消对应 `ListNode` / `TreeNode` 的注释
3. `class Solution` 里的方法名和签名要**完全对齐 LeetCode 题目**（提交时要直接复制类去 LeetCode）
4. `cases` 里写 3-5 个测试用例，至少包含一个边界（空、单元素、最大约束）
5. `test()` 里那行 `s.solve(*args)` 改成实际方法名

## 跑测试

```bash
python 04_two_pointers/0015_three_sum.py
```

输出示例：
```
[PASS] Case 1: args=([-1, 0, 1, 2, -1, -4],)  expected=[[-1, -1, 2], [-1, 0, 1]]  actual=[[-1, -1, 2], [-1, 0, 1]]
[PASS] Case 2: args=([],)  expected=[]  actual=[]
2/2 passed
```

## 复盘流程

每做完一题，**在 docstring 的「复盘要点」里写两句话**：
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？

第二轮复习时只需扫一遍这几行字就能唤起记忆，比重看代码高效得多。
