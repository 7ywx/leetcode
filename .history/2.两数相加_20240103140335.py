#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode.cn/problems/add-two-numbers/description/
#
# algorithms
# Medium (43.00%)
# Likes:    10304
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 4.5M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0
# 题目数据保证列表表示的数字不含前导零
#
#
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def getLength(self):
        node = self
        length = 0
        while node!= None:
            length += 1
            node = node.next
        return length
    def _print_(self):
        node = self
        while node!= None:
            print(str(node.val)+'->',end='')
            node = node.next
        print()
from typing import Optional
from typing import List
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode(0)
        l1._print_()
        l2._print_()
        sum._print_()
        lengthl1 = l1.getLength()
        lengthl2 = l2.getLength()
        i,j = 0,0
        while i<lengthl1 or j<lengthl2:
            if i<lengthl1:
                sum.val += l1.val
                i += 1
                l1 = l1.next
            if j<lengthl2:
                sum.val += l2.val
                j += 1
                l2 = l2.next
            unit_digit = sum.val % 10
            tens_digit = sum.val // 10
            sum.val = unit_digit
        sum._print_()


l1 = [2,4,3]
l2 = [5,6,4]

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3
node4.next = node5
node5.next = node6
solution = Solution()
solution.addTwoNumbers(node1,node4)
# @lc code=end
