"""
链表测试通用辅助函数。
- 各题文件自带 ListNode 类（LeetCode 风格独立粘贴）
- 这里集中放 to_list / from_list 等常用工具，需要时 from _helpers import ...
- 多数题为了独立可粘贴提交，会在自己文件里复制一份；这个文件只是参考
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    seen = set()                        # 防环
    while head and id(head) not in seen:
        seen.add(id(head))
        out.append(head.val)
        head = head.next
    return out


def from_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def from_list_with_cycle(values: List[int], pos: int) -> Optional[ListNode]:
    """构造一个尾部指向 values[pos] 的环；pos = -1 表示无环。"""
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]
