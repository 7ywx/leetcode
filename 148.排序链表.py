#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode.cn/problems/sort-list/description/
#
# algorithms
# Medium (65.52%)
# Likes:    2244
# Dislikes: 0
# Total Accepted:    470.9K
# Total Submissions: 718.6K
# Testcase Example:  '[4,2,1,3]'
#
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#
#
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
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
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
#
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
#
#
from typing import Optional, List
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 自顶向下归并排序
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            """
            找到链表的中点，以中点为分界，将链表拆分成两个子链表。
            寻找链表的中点可以使用快慢指针的做法，
            快指针每次移动 2 步，慢指针每次移动 1 步，
            当快指针到达链表末尾时，慢指针指向的链表节点即为链表的中点。
            :param head: 链表的头节点
            :param tail: 链表的尾节点
            :return: 排序后的链表的头节点
            """
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            """
            合并两个有序链表的函数
            :param head1: 第一个有序链表的头节点
            :param head2: 第二个有序链表的头节点
            :return: 合并后的有序链表的头节点
            """
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        return sortFunc(head, None)

        # 链表->数组->链表
        current = head.next
        sortListHead = ListNode() # dummy head
        sortListHead.next = head
        sortListLast = head
        while current:
            if current.val >= sortListLast.val:
                sortListLast.next = current
                sortListLast = current
                current = current.next
            else: # 当前节点小于sortListLast节点
                # 1.寻找插入位置(pre为插入位置的前一个节点)
                pre = sortListHead
                while pre.next and pre.next.val < current.val:
                    pre = pre.next
                # 2.插入
                currentNext = current.next
                current.next = pre.next
                pre.next = current
                current = currentNext
        return sortListHead.next
# @lc code=end
def printListNode(head: ListNode):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print()

solution = Solution()

printListNode(solution.sortList(head))
