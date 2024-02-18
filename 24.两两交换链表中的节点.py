#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode.cn/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (71.86%)
# Likes:    2147
# Dislikes: 0
# Total Accepted:    777.8K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
#
#
# 示例 2：
#
#
# 输入：head = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：head = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果头结点为空或者头结点的下一个节点为空，则直接返回头结点
        if not head or not head.next:
            return head
        else:
            # 定义两个指针node1和node2，分别指向头结点和头结点的下一个节点
            node1 = head
            node2 = head.next

            # 将头结点指向下一个节点
            head = node2
            # 将node1的下一个节点指向调用swapPairs函数后的结果
            node1.next = self.swapPairs(node2.next)
            # 将node2的下一个节点指向node1
            node2.next = node1
        return head
# @lc code=end
