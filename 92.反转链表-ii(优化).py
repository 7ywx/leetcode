#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (56.70%)
# Likes:    1849
# Dislikes: 0
# Total Accepted:    555.7K
# Total Submissions: 979.8K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
#
#
# 提示：
#
#
# 链表中节点数目为 n
# 1
# -500
# 1
#
#
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？
#
#
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index = 1
        cur = head
        lr = {}
        while cur:
            if index > left - 2 and index < right + 2:
                lr[index] = cur
            cur = cur.next
            index += 1

        cur = lr[right]
        i = 1
        while i < right - left + 1:
            cur.next = lr[right - i]
            cur = cur.next
            i += 1
        if left > 1:
            lr[left - 1].next = lr[right]
        if right + 1 in lr:
            cur.next = lr[right + 1]
        else:
            cur.next = None
        return head if left > 1 else lr[right]
# @lc code=end
print(Solution().reverseBetween(ListNode(3, ListNode(5)), 1, 2).next.val)
