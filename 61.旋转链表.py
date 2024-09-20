#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode.cn/problems/rotate-list/description/
#
# algorithms
# Medium (41.44%)
# Likes:    1084
# Dislikes: 0
# Total Accepted:    410.3K
# Total Submissions: 989.9K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
#
#
# 示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            i += 1
            cur = cur.next
        tail = cur
        if i < 2:
            return head
        k %= i
        if k == 0:
            return head
        tail.next = head
        cur = dummy
        for _ in range(i - k):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head
# @lc code=end
