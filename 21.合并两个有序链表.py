#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.24%)
# Likes:    3437
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
#
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
# 示例 2：
#
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 两个链表的节点数目范围是 [0, 50]
# -100
# l1 和 l2 均按 非递减顺序 排列
#
#
#
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # # 双指针
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # res = ListNode()
        # head = res
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         res.next = list1
        #         list1 = list1.next
        #         res = res.next
        #     else: # list1.val >= list2.val
        #         res.next = list2
        #         list2 = list2.next
        #         res = res.next
        # if list1:
        #     res.next = list1
        # else:
        #     res.next = list2
        # return head.next
        # # 递归
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        # if list1.val < list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2
# @lc code=end
def printListNode(node: ListNode):
    while node:
        print(node.val, end='->')
        node = node.next
    print('None')
solution = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
printListNode(solution.mergeTwoLists(list1, list2))
