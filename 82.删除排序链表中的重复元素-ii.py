#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (54.62%)
# Likes:    1322
# Dislikes: 0
# Total Accepted:    473.2K
# Total Submissions: 866.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        curPrev = None
        flag = False
        while cur:
            # if cur.next and cur.val == cur.next.val:
            #     flag = True
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                flag = True
            if flag:
                if curPrev:
                    curPrev.next = cur.next
                else:
                    head = cur.next
            else:
                curPrev = cur
            cur = cur.next
            flag = False
        return head
# @lc code=end
