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
        def getLength(node):
            length = 0
            while node!= None:
                length += 1
                node = node.next
            return length
        sum = ListNode(0)  # 创建一个空的ListNode节点作为sum
        p1 = sum  # 将p1指向sum节点
        # lengthl1 = l1.getLength()  # 获取l1链表的长度
        # lengthl2 = l2.getLength()  # 获取l2链表的长度
        while l1 or l2:
        # while l1.next != None or l2.next != None:  # 循环直到i和j都遍历完l1和l2链表或者i和j都大于l1和l2链表的长度
            sumVal=0  # sumVal：保存sum节点的值，初始化sumVal为0
            if l1:  # 如果i小于l1链表的长度，则将l1节点的值加到sumVal上，并将i加1，更新l1节点为l1.next节点
                sumVal += l1.val
                l1 = l1.next
            if l2:  # 如果j小于l2链表的长度，则将l2节点的值加到sumVal上，并将j加1，更新l2节点为l2.next节点
                sumVal += l2.val
                l2 = l2.next
            p1.val += sumVal  # 将p1节点的值加上sumVal
                            unit_digit = p1.val % 10  # 重新计算p1节点的个位数
            tens_digit = p1.val // 10  # 重新计算p1节点的十位数
            if p1.val >= 10 or tens_digit!= 0:  # 如果p1节点的值（在加上sumVal时）大于等于10

                p1.val = unit_digit  # 将p1节点的值设为个位数
                p1.next = ListNode(tens_digit)  # 创建一个新的ListNode节点，值为十位数，并将其作为p1节点的下一个节点
            if l1 or l2:  # 如果后面还有计算或者p1节点的十位数不为0（p1节点需要进位）
                p1.next = ListNode(tens_digit)  # 创建一个新的ListNode节点，值为十位数，并将其作为p1节点的下一个节点
                p1 = p1.next  # 将p1节点指向下一个节点
        sum._print_()
        return sum  # 返回sum节点作为结果
        # while i<lengthl1 or j<lengthl2:  # 循环直到i和j都遍历完l1和l2链表或者i和j都大于l1和l2链表的长度
        #     sumVal=0  # sumVal：保存sum节点的值，初始化sumVal为0
        #     if i<lengthl1:  # 如果i小于l1链表的长度，则将l1节点的值加到sumVal上，并将i加1，更新l1节点为l1.next节点
        #         sumVal += l1.val
        #         i += 1
        #         l1 = l1.next
        #     if j<lengthl2:  # 如果j小于l2链表的长度，则将l2节点的值加到sumVal上，并将j加1，更新l2节点为l2.next节点
        #         sumVal += l2.val
        #         j += 1
        #         l2 = l2.next
        #     p1.val += sumVal  # 将p1节点的值加上sumVal
        #     unit_digit = p1.val % 10  # 重新计算p1节点的个位数
        #     tens_digit = p1.val // 10  # 重新计算p1节点的十位数
        #     if p1.val >= 10 or tens_digit!= 0:  # 如果p1节点的值（在加上sumVal时）大于等于10
        #         p1.val = unit_digit  # 将p1节点的值设为个位数
        #         p1.next = ListNode(tens_digit)  # 创建一个新的ListNode节点，值为十位数，并将其作为p1节点的下一个节点
        #     if i<lengthl1 or j<lengthl2:  # 如果后面还有计算或者p1节点的十位数不为0（p1节点需要进位）
        #         p1.next = ListNode(tens_digit)  # 创建一个新的ListNode节点，值为十位数，并将其作为p1节点的下一个节点
        #         p1 = p1.next  # 将p1节点指向下一个节点
        # sum._print_()
        # return sum  # 返回sum节点作为结果
# @lc code=end
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

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)
l1.next.next.next = ListNode(9)
l1.next.next.next.next = ListNode(9)
l1.next.next.next.next.next = ListNode(9)
l1.next.next.next.next.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)

solution = Solution()
solution.addTwoNumbers(node1,node4)
solution.addTwoNumbers(l1,l2)
