"""
LeetCode 211. Design Add and Search Words Data Structure / 添加与搜索单词  (Medium)
Link: https://leetcode.cn/problems/design-add-and-search-words-data-structure/

题目描述
--------
设计 WordDictionary 类：
- addWord(word): 添加 word
- search(word): 返回字典中是否存在 word；word 中可以含 '.'，'.' 表示任意一个字母

约束
----
- 1 <= word.length <= 25
- search 中 '.' 数量 <= 3
- 调用 addWord 总次数 <= 10^4
- 仅小写字母与 '.'

提示
----
卡住超过 25 分钟再去看 16_design/NOTES.md。
（思路：Trie + DFS：遇到 '.' 时枚举所有子节点）

复杂度（解完后填）
------
addWord: O(?)    search: O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class WordDictionary:
    def __init__(self):
        # TODO: 初始化数据结构
        pass

    def addWord(self, word: str) -> None:
        # TODO: 在这里写你的解法
        pass

    def search(self, word: str) -> bool:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = WordDictionary()
            out.append(None)
        elif name == 'addWord':
            obj.addWord(*args)
            out.append(None)
        else:
            out.append(getattr(obj, name)(*args))
    return out


def test():
    cases = [
        (
            [('init', ()),
             ('addWord', ("bad",)),
             ('addWord', ("dad",)),
             ('addWord', ("mad",)),
             ('search', ("pad",)),
             ('search', ("bad",)),
             ('search', (".ad",)),
             ('search', ("b..",))],
            [None, None, None, None, False, True, True, True],
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
