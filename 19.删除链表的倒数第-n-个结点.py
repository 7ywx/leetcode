#

# @lc app=leetcode.cn id=19 lang=python3
#

# [19] 删除链表的倒数第 N 个结点
#

# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#

# algorithms

# Medium (46.97%)

# Likes:    2807

# Dislikes: 0

# Total Accepted:    1.3M

# Total Submissions: 2.8M

# Testcase Example:  '[1,2,3,4,5]\n2'
#

# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#
#

# 示例 1：
#
#

# 输入：head = [1,2,3,4,5], n = 2

# 输出：[1,2,3,5]
#
#

# 示例 2：
#
#

# 输入：head = [1], n = 1

# 输出：[]
#
#

# 示例 3：
#
#

# 输入：head = [1,2], n = 1

# 输出：[1]
#
#
#
#

# 提示：
#
#

# 链表中结点的数目为 sz

# 1 <= sz <= 30

# 0 <= Node.val <= 100

# 1 <= n <= sz
#
#
#
#

# 进阶：你能尝试使用一趟扫描实现吗？
#
#


# @lc code=start

# Definition for singly-linked list.

# class ListNode:

#     def __init__(self, val=0, next=None):

#         self.val = val

#         self.next = next

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建一个虚拟节点，并将其下一个指针设置为链表的头部
        dummy_head = ListNode(0, head)

        # 创建两个指针，慢指针和快指针，并将它们指向虚拟节点
        slow = fast = dummy_head

        # 快指针比慢指针快 n+1 步
        for i in range(n+1):
            fast = fast.next

        # 移动两个指针，直到快速指针到达链表的末尾
        while fast:
            slow = slow.next
            fast = fast.next

        # 通过更新第 (n-1) 个节点的 next 指针删除第 n 个节点
        slow.next = slow.next.next

        return dummy_head.next


        # 创建一个空列表node_list，用于存储链表节点
        node_list = []

        # 将链表节点加入node_list
        cur = head
        while cur:
            node_list.append(cur)
            cur = cur.next

        # 获取链表的长度
        i = len(node_list)

        # 如果要删除的节点数为第一个节点: 直接返回head.next
        if n == i:
            return head.next
        # 否则: 因为不算头节点, 所以必有i-n-1(要删除的节点的前一个节点)
        else:
            node_list[i-n-1].next = node_list[i-n-1].next.next # (i-n-1: 要删除的节点的前一个节点的索引, i-n: 要删除的节点的索引, i-n+1: 要删除的节点的下一个节点的索引, 因为可能不存在于node_list中, 故而用node_list[i-n-1].next.next)
            return head

# @lc code=end
