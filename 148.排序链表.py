#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode.cn/problems/sort-list/description/
#
# algorithms
# Medium (65.52%)
# Likes:    2244
# Dislikes: 0
# Total Accepted:    470.9K
# Total Submissions: 718.6K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#
#
# 示例 3：
#
#
# 输入：head = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
from typing import Optional, List
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head.next
        sortListHead = ListNode() # dummy head
        sortListHead.next = head
        sortListLast = head
        while current:
            if current.val >= sortListLast.val:
                sortListLast.next = current
                sortListLast = current
                current = current.next
            else: # 当前节点小于sortListLast节点
                # 1.寻找插入位置(pre为插入位置的前一个节点)
                pre = sortListHead
                while pre.next and pre.next.val < current.val:
                    pre = pre.next
                # 2.插入
                currentNext = current.next
                current.next = pre.next
                pre.next = current
                current = currentNext
        return sortListHead.next
# @lc code=end
def printListNode(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()

solution = Solution()

printListNode(solution.sortList(head))
