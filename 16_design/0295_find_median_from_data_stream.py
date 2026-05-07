"""
LeetCode 295. Find Median from Data Stream / 数据流的中位数  (Hard)
Link: https://leetcode.cn/problems/find-median-from-data-stream/

题目描述
--------
设计 MedianFinder 类：
- addNum(num): 把整数 num 加入数据流
- findMedian(): 返回当前所有元素的中位数（偶数个时为中间两数平均）

约束
----
- -10^5 <= num <= 10^5
- 调用 findMedian 时至少有一个元素
- 总调用次数 <= 5 * 10^4

提示
----
卡住超过 25 分钟再去看 12_heap_topk/NOTES.md 或 16_design/NOTES.md 的「双堆」模板。
（大顶堆存较小一半 + 小顶堆存较大一半；维护两堆大小差 <= 1）

复杂度（解完后填）
------
addNum: O(?)    findMedian: O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List, Tuple, Any


class MedianFinder:
    def __init__(self):
        # TODO: 初始化数据结构
        pass

    def addNum(self, num: int) -> None:
        # TODO: 在这里写你的解法
        pass

    def findMedian(self) -> float:
        # TODO: 在这里写你的解法
        pass


def run_ops(ops: List[Tuple[str, Any]]) -> List[Any]:
    out: List[Any] = []
    obj = None
    for name, args in ops:
        if name == 'init':
            obj = MedianFinder()
            out.append(None)
        elif name == 'addNum':
            obj.addNum(*args)
            out.append(None)
        else:
            out.append(obj.findMedian())
    return out


def test():
    cases = [
        (
            [('init', ()),
             ('addNum', (1,)),
             ('addNum', (2,)),
             ('findMedian', ()),
             ('addNum', (3,)),
             ('findMedian', ())],
            [None, None, None, 1.5, None, 2.0],
        ),
        (
            [('init', ()),
             ('addNum', (-1,)),
             ('findMedian', ()),
             ('addNum', (-2,)),
             ('findMedian', ()),
             ('addNum', (-3,)),
             ('findMedian', ())],
            [None, None, -1.0, None, -1.5, None, -2.0],
        ),
    ]
    passed = 0
    for i, (ops, expected) in enumerate(cases, 1):
        actual = run_ops(ops)
        ok = len(actual) == len(expected) and all(
            (a == e if (e is None or isinstance(e, type(None))) else
             (a is not None and abs(a - e) < 1e-9) if isinstance(e, float) else a == e)
            for a, e in zip(actual, expected)
        )
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: expected={expected}  actual={actual}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
