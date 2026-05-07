# 0005 最长回文子串 — 复盘

> 题：[0005_longest_palindrome.py](../01_array_string/0005_longest_palindrome.py)
> 日期：2026-04-30
> 套路：中心扩展（详见 [01_array_string/NOTES.md](../01_array_string/NOTES.md)）

## 我的第一版踩了哪些坑

按"致命"→"逻辑"分级。括号里链接到 [pitfalls.md](pitfalls.md) 的主题归类。

### 致命（让代码跑不起来）

1. **`s.__len__` 当成数字用** → `TypeError`。Python 里取长度永远 `len(s)`。`__len__` 不加括号是方法对象。  〔[Python 取长度](pitfalls.md#长度--大小)〕
2. **类内方法忘了 `self`**：`def Odd(s, pos):` 调用 `self.Odd(...)` 时 self 实例会被错误绑给 s 参数。Python 不像 TS / Java 隐式注入 this，必须显式声明 `self`。  〔[OOP/方法定义](pitfalls.md#类与方法)〕
3. **`|` 当逻辑或用**：`pos - i > -1 | pos + i < ...` 里的 `|` 是按位或，且优先级比 `<` `>` 高，整句解析错。Python 的逻辑或是 `or`、与是 `and`，不是 TS 的 `||` `&&`。  〔[逻辑运算符](pitfalls.md#逻辑运算符)〕
4. **while 没递增 `i`** → 死循环（任何语言通病，但加 `i += 1` 即可）。
5. **字符串当 list 用**：`res = s[pos]; res.append(...)` —— 字符串**不可变**，没有 append/insert。要积字符要么用 `list` + `"".join(...)`，要么直接维护下标做切片。  〔[字符串不可变](pitfalls.md#字符串不可变)〕

### 逻辑/风格

6. `i = (int)(0)` → C/TS 风格 cast 不存在。Python 是 `int(0)`（函数）；这里直接 `i = 0` 就够。  〔[类型转换](pitfalls.md#类型转换)〕
7. `max = 0` 覆盖了 Python 内置 `max()` 函数。同名变量不会立即报错，但等你想 `max(a, b)` 时会拿到一个 int 不可调用，调试很费劲。建议永远不要用 `max` `min` `sum` `list` `dict` `set` `id` `type` `input` `open` 这些当变量名。  〔[内置名遮蔽](pitfalls.md#变量名遮蔽内置)〕
8. `res.insert(s[pos + i], 0)` 参数顺序反了。`list.insert(index, value)`，第一个是位置，第二个是值。  〔[list API 参数顺序](pitfalls.md#list-api)〕
9. `Oven` → `Even`（拼写）。
10. 中心扩展的实现思路绕了：**正确套路是只记录 (l, r) 区间，扩展结束后切片 s[l:r+1]**。不要一个一个字符积。

## 这次学到的

- TS 写惯了，最容易"自动"写出来的错都集中在 **取长度（`.length` → `len()`）** 和 **逻辑运算符（`||` → `or`）** 上，把这两条肌肉记忆改过来能省一半 bug。
- Python 字符串和列表的不可变区别要刻进脑子。看到题面里"要修改字符序列"立刻 `s = list(s)`。
- 写实例方法时，**一开始就先打 `def f(self, ...):` 再写参数**——别等调用时才想起来。
- **切片左闭右开**：`s[l : r + 1]` 里的 `+1` 不是 hack——Python 切片 `[a, b)` 不含 b，要把下标 r 这个字符包进来 stop 必须 = r+1。详见 [pitfalls.md § 切片左闭右开](pitfalls.md#切片左闭右开)。

## 修复后的关键片段（中心扩展标准写法）

```python
def expand(l: int, r: int) -> tuple[int, int]:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return l + 1, r - 1
```

整体结构在 [01_array_string/NOTES.md](../01_array_string/NOTES.md) 里有完整模板。
