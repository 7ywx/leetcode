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

        node_list = []
        cur = head

        while cur:

            node_list.append(cur)

            cur = cur.next

        i = len(node_list)

        if n == i:

            return head.next
        else:

            node_list[i-n-1].next = node_list[i-n-1].next.next

            return head


        # i = 0

        # node_dict = {}

        # while head:

        #     node_dict[i] = head

        #     head = head.next

        #     i += 1

        # if n == i:
        #     return node_dict[0].next
        # else:

        #     node_dict[i-n-1].next = node_dict[i-n-1].next.next

        #     return node_dict[0]

# @lc code=end
