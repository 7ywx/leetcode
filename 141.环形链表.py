#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# https://leetcode.cn/problems/linked-list-cycle/description/
#
# algorithms
# Easy (52.06%)
# Likes:    2103
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
#
#
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [0, 10^4]
# -10^5 <= Node.val <= 10^5
# pos 为 -1 或者链表中的一个 有效索引 。
#
#
#
#
# 进阶：你能用 O(1)（即，常量）内存解决此问题吗？
#
#
from typing import Optional, List
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 定义一个函数，用于判断链表是否含有环
    def hasCycle(self, head: ListNode) -> bool:
        """
        :param head: 链表的头结点
        :type head: ListNode
        :return: 如果链表含有环则返回True，否则返回False
        :rtype: bool
        """

        # 判断链表是否为空或只有一个节点，这两种情况下都不可能形成环，直接返回False
        if not head or not head.next:
            return False

        # 初始化两个指针，slow指针每次移动一个节点，fast指针每次移动两个节点
        slow = head
        fast = head.next

        # 当慢指针slow与快指针fast未相遇时（即没有形成环），持续移动
        while slow != fast:
            # 如果在fast或fast的下一个节点为空，说明链表已到末尾而未形成环，返回False
            if not fast or not fast.next:
                return False

            # 慢指针slow向前移动一个节点
            slow = slow.next

            # 快指针fast向前移动两个节点
            fast = fast.next.next

        # 若循环结束，说明slow和fast在某个节点相遇（即形成了环），返回True
        return True
# @lc code=end
solution = Solution()

case15 = ListNode(1)
case15.next = ListNode(2)
print(solution.hasCycle(case15))
