# 0014 最长公共前缀 — 复盘

> 题：[0014_longest_common_prefix.py](../01_array_string/0014_longest_common_prefix.py)
> 日期：2026-04-30
> 套路：纵向扫描（详见 [01_array_string/NOTES.md](../01_array_string/NOTES.md)）

## 我这版踩了哪些坑

### 致命

1. **循环变量 `str` 漏出来污染了后续代码** —— 主 bug 来源。
   ```python
   for str in strs:           # 这个 str 在循环结束后仍 = strs 的最后一个字符串
       ...
   ...
   chr = str[0][i]            # 此时 str 不是数组而是单字符串；str[0][1] 就越界
   ```
   错误：`IndexError: string index out of range`。
   〔[for / while 循环变量会"漏"到循环外](pitfalls.md#for--while-循环变量会漏到循环外)〕

2. **inner break 没有跳出 outer**：双层 for 中，内层不匹配时只 break 内层，外层 i 还会继续递增。改用 **sentinel return**（找到第一个不匹配就直接 return）最干净。
   〔[break 只跳出最内层循环](pitfalls.md#break-只跳出最内层循环)〕

### 风格 / 习惯

3. **`str`、`chr` 都覆盖了 Python 内置**（`str()` 类型转换、`chr()` 整数转字符）。这次没立即出错只是因为没用到这两个内置。下回写题：永远用 `s`、`ch`、`text`、`word` 这种命名，避开内置名。
   〔[变量名遮蔽内置](pitfalls.md#变量名遮蔽内置)〕

4. **手写 `min_len = 10000; for s in strs: if len(s) < min_len: ...`** 太啰嗦。一行内置就能搞定：
   ```python
   min_len = min(len(s) for s in strs)
   ```
   生成器表达式在 Python 比手写循环更 Pythonic，而且**变量 `s` 局限于生成器作用域，不会泄漏到外层**——一举两得。

5. 末尾 `pass` 在 `return` 之后是死代码，可删。

6. 返回切片用了 `str[0][:j]`，但 j 是字符串下标（外层 strs 的索引），用错了变量。**列号 `i` 才是要切的位置**。

## 这次学到的

- TS 的 `for (let x of xs)` 是块作用域，循环变量出循环就消失。**Python 不是**——循环跑完 `x` 还在，且等于最后一次迭代值。改肌肉记忆：循环变量起短名（`s` / `i` / `_`），但**循环外不要再读这个变量名**。
- 双层 for 想"任一不满足就整体停"，**优先想 sentinel return**，比 flag 干净 3 倍。
- 看到题面里有"求最小长度"、"取每个元素的某属性后聚合"这种动词，立刻条件反射 `min(... for ... in ...)` 之类的内置 + 生成器，比 for 循环短而且没循环变量泄漏问题。

## 修复后的关键片段（纵向扫描）

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        ch = strs[0][i]
        for s in strs:
            if s[i] != ch:
                return strs[0][:i]
    return strs[0][:min_len]
```
