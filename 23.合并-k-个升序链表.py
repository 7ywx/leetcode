#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (59.02%)
# Likes:    2766
# Dislikes: 0
# Total Accepted:    760.6K
# Total Submissions: 1.3M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
# 示例 2：
#
# 输入：lists = []
# 输出：[]
#
#
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
#
#
# 提示：
#
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
#
#
#
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
# @lc code=start
# Definition for singly-linked list.
"""
在Python中，__lt__ （less than）是一个特殊方法（也称为魔术方法），它定义了对象之间的“小于”比较行为。
当两个对象通过 < 运算符进行比较时，Python会自动调用这个方法。

__init__(self, ...)：初始化方法，在创建对象时自动调用，用于设置对象的初始状态。

__str__(self) 或 __repr__(self)：

__str__() 返回一个用户友好的字符串表示形式，通常用于打印或显示对象。
__repr__() 返回一个面向开发者且可能包含更多信息的字符串表示形式，目的是能够重新生成该对象。
__call__(self, *args, **kwargs)：允许将实例本身作为函数调用。

__getattr__(self, name)：在试图获取不存在的属性时调用，提供自定义属性查找逻辑。

__setattr__(self, name, value)：在试图设置属性时调用，可以用于实现自定义的属性赋值逻辑。

__delattr__(self, name)：在删除属性时调用，可以进行删除前的验证或其他操作。

__getitem__(self, key) 和 __setitem__(self, key, value)：

__getitem__() 实现了使用索引（如 obj[key]）访问元素的行为。
__setitem__() 允许通过索引赋值（如 obj[key] = value）。
__len__(self)：返回对象长度，使得能使用内置函数 len() 计算对象长度。

__add__(self, other)、__sub__(self, other) 等：定义加法、减法等数学运算符重载，支持自定义类型间的算术运算。

__enter__(self) 和 __exit__(self, exc_type, exc_value, traceback)：用于支持上下文管理协议，使得类实例可以用于 with 语句。
"""
ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 最小堆
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点

        # 如果列表为空，则返回None
        if not lists:
            return None
        # 合并两个链表的函数
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            # 创建一个虚拟节点作为合并后的链表的头节点
            dummy = ListNode()
            # 定义当前节点为虚拟节点
            cur = dummy
            # 当两个链表都不为空时，进行循环合并
            while l1 and l2:
                # 如果l1节点的值小于l2节点的值，则将l1节点添加到合并后的链表中，并将l1指针后移
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                # 否则将l2节点添加到合并后的链表中，并将l2指针后移
                else:
                    cur.next = l2
                    l2 = l2.next
                # 将当前节点指针后移
                cur = cur.next
            # 如果l1链表不为空，则将剩余的节点添加到合并后的链表中
            if l1:
                cur.next = l1
            # 如果l2链表不为空，则将剩余的节点添加到合并后的链表中
            else:
                cur.next = l2
            # 返回合并后的链表的头节点
            return dummy.next
        # 将第一个链表赋值给res
        res = lists[0]
        # 遍历剩余的链表，依次将每个链表与res合并
        for i in range(1, len(lists)):
            res = merge(res, lists[i])
        # 返回合并后的链表
        return res
# @lc code=end
