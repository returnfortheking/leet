"""
LeetCode 208. Implement Trie (Prefix Tree) / 实现 Trie (前缀树)  (Medium)
Link: https://leetcode.cn/problems/implement-trie-prefix-tree/

题目描述
--------
设计 Trie 类支持：
- insert(word)
- search(word): 返回是否存在 word
- startsWith(prefix): 返回是否存在以 prefix 开头的单词

均要求 O(len) 时间。

约束
----
- 1 <= word.length, prefix.length <= 2000
- 仅小写英文字母
- 调用次数 <= 3 * 10^4

复杂度（解完后填）
------
单次操作 O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class Trie:
    def __init__(self):
        # TODO: 初始化数据结构
        pass

    def insert(self, word: str) -> None:
        # TODO: 在这里写你的解法
        pass

    def search(self, word: str) -> bool:
        # TODO: 在这里写你的解法
        pass

    def startsWith(self, prefix: str) -> bool:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = Trie()
            out.append(None)
        elif name == 'insert':
            obj.insert(*args)
            out.append(None)
        else:
            out.append(getattr(obj, name)(*args))
    return out


def test():
    cases = [
        (
            [('init', ()),
             ('insert', ("apple",)),
             ('search', ("apple",)),
             ('search', ("app",)),
             ('startsWith', ("app",)),
             ('insert', ("app",)),
             ('search', ("app",))],
            [None, None, True, False, True, None, True],
        ),
        (
            [('init', ()),
             ('search', ("a",)),
             ('startsWith', ("",))],
            [None, False, True],
        ),
    ]
    passed = 0
    for i, (ops, expected) in enumerate(cases, 1):
        actual = run_ops(ops)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
