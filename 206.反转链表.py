#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode.cn/problems/reverse-linked-list/description/
#
# algorithms
# Easy (73.86%)
# Likes:    3498
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 2.4M
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
#
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5]
# 输出：[5,4,3,2,1]
#
#
# 示例 2：
#
#
# 输入：head = [1,2]
# 输出：[2,1]
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
# 链表中节点的数目范围是 [0, 5000]
# -5000
#
#
#
#
# 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
#
#
#
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代
        cur, pre = head, None
        while cur:
            tmp = cur.next # 暂存后继节点 cur.next
            cur.next = pre # 修改 next 引用指向
            pre = cur      # pre 暂存 cur
            cur = tmp      # cur 访问下一节点
        return pre

        # 递归
        # 如果链表为空或只有一个节点，则直接返回头节点
        if not head or not head.next:
            return head
        else:
            # reverse_last: reverse链表尾部节点
            reverse_last = head.next
            # 递归反转链表, reverse: 反转链表的头部节点
            reverse = self.reverseList(head.next)

            # 将反转后的链表尾部节点的next指针指向头节点,并将头节点的next指针指向None
            reverse_last.next = head
            head.next = None

            # 返回反转后的头节点
            return reverse
# @lc code=end
def printListNode(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()

example1 = ListNode(1)
example1.next = ListNode(2)
example1.next.next = ListNode(3)
example1.next.next.next = ListNode(4)
example1.next.next.next.next = ListNode(5)
printListNode(Solution().reverseList(example1))

example2 = ListNode(1)
example2.next = ListNode(2)
# printListNode(Solution().reverseList(example2))

#example3 = ListNode()
# printListNode(Solution().reverseList(None))
