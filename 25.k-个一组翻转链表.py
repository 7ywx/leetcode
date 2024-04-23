#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#
# https://leetcode.cn/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (67.80%)
# Likes:    2284
# Dislikes: 0
# Total Accepted:    554K
# Total Submissions: 817K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
#
#
# 示例 2：
#
#
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
#
#
# 提示：
#
#
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
#
#
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
#
#
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或只有一个节点，则直接返回头节点
        if head == tail:
            return head
        else:
            # reverse_last: reverse链表倒数第二个节点
            reverse_last = head.next
            # 递归反转链表, reverse: 反转链表的头部节点
            reverse = self.reverseList(head.next, tail)

            # 将反转后的链表尾部节点的next指针指向头节点,并将头节点的next指针指向None
            reverse_last.next = head
            head.next = None

            # 返回反转后的头节点
            return reverse
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while True:
            count = 0
            cur_head = cur
            cur_last = cur.next
            while cur.next and count < k:
                cur = cur.next
                count += 1
            if count < k:
                break
            else:
                if cur_head == dummy:
                    cur_next = cur.next
                    reverse = self.reverseList(cur_head.next, cur)
                    head.next = cur_next
                    cur = head
                    dummy.next = reverse
                else:
                    cur_next = cur.next
                    reverse = self.reverseList(cur_head.next, cur)
                    cur_head.next = reverse
                    cur_last.next = cur_next
                    cur = cur_last
            # print(f'cur = {cur.val}')
            # printListNode(dummy.next)
        return dummy.next
# @lc code=end
