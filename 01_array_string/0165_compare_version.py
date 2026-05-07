"""
LeetCode 165. Compare Version Numbers / 比较版本号  (Medium)
Link: https://leetcode.cn/problems/compare-version-numbers/

题目描述
--------
给定两个版本号字符串 version1 和 version2（点号分隔的修订号序列）。
按从左到右逐段比较修订号大小：
  - version1 < version2 返回 -1
  - version1 > version2 返回 1
  - 相等返回 0
比较时忽略前导零；缺失的修订号当作 0。

约束
----
- 1 <= version*.length <= 500
- 仅包含数字和点号
- 修订号无前导零（除非整段是 "0"）

提示
----
卡住超过 25 分钟再去看 01_array_string/NOTES.md。
（思路：split('.') 后逐段 int 比较）

复杂度（解完后填）
------
时间：O(?)    空间：O(?)

复盘要点（解完后填）
--------
- 卡在哪一步？
- 触发器：什么样的题面应该让我立刻想到这个套路？
"""

from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # TODO: 在这里写你的解法
        pass


def test():
    sol = Solution()
    cases = [
        (("1.01", "1.001"), 0),
        (("1.0", "1.0.0"), 0),
        (("0.1", "1.1"), -1),
        (("1.0.1", "1"), 1),
        (("7.5.2.4", "7.5.3"), -1),
        (("1.01.1", "1.1.1"), 0),
        (("1", "1.0.0.0"), 0),
    ]
    passed = 0
    for i, (args, expected) in enumerate(cases, 1):
        actual = sol.compareVersion(*args)
        ok = actual == expected
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] Case {i}: args={args!r}  expected={expected!r}  actual={actual!r}")
        if ok:
            passed += 1
    print(f"\n{passed}/{len(cases)} passed")
    assert passed == len(cases)


if __name__ == "__main__":
    test()
