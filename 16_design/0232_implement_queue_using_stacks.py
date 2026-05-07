"""
LeetCode 232. Implement Queue using Stacks / 用栈实现队列  (Easy)
Link: https://leetcode.cn/problems/implement-queue-using-stacks/

题目描述
--------
仅使用两个栈实现先入先出 (FIFO) 队列：
- push(x): 入队
- pop(): 出队并返回元素
- peek(): 返回队头元素
- empty(): 是否为空

均摊 O(1) 实现。

约束
----
- 1 <= x <= 9
- 调用次数 <= 100
- 调用 pop / peek 前队列非空

提示
----
卡住超过 25 分钟再去看 16_design/NOTES.md 的「用栈实现队列」模板。

复杂度（解完后填）
------
push: O(?)    pop: O(?) 均摊    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class MyQueue:
    def __init__(self):
        # TODO: 初始化两个栈
        pass

    def push(self, x: int) -> None:
        # TODO: 在这里写你的解法
        pass

    def pop(self) -> int:
        # TODO: 在这里写你的解法
        pass

    def peek(self) -> int:
        # TODO: 在这里写你的解法
        pass

    def empty(self) -> bool:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = MyQueue()
            out.append(None)
        elif name == 'push':
            obj.push(*args)
            out.append(None)
        else:
            out.append(getattr(obj, name)(*args))
    return out


def test():
    cases = [
        (
            [('init', ()),
             ('push', (1,)),
             ('push', (2,)),
             ('peek', ()),
             ('pop', ()),
             ('empty', ())],
            [None, None, None, 1, 1, False],
        ),
        (
            [('init', ()),
             ('empty', ())],
            [None, True],
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
