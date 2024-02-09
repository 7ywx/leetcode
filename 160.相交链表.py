#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode.cn/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (64.31%)
# Likes:    2359
# Dislikes: 0
# Total Accepted:    782.5K
# Total Submissions: 1.2M
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3'
#
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
#
# 图示两个链表在节点 c1 开始相交：
#
#
#
# 题目数据 保证 整个链式结构中不存在环。
#
# 注意，函数返回结果后，链表必须 保持其原始结构 。
#
# 自定义评测：
#
# 评测系统 的输入如下（你设计的程序 不适用 此输入）：
#
#
# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
#
#
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被
# 视作正确答案 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# — 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点)
# 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点)
# 在内存中指向相同的位置。
#
#
#
#
# 示例 2：
#
#
#
#
# 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Intersected at '2'
# 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
# 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
# 示例 3：
#
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null 。
#
#
#
#
# 提示：
#
#
# listA 中节点数目为 m
# listB 中节点数目为 n
# 1 <= m, n <= 3 * 10^4
# 1 <= Node.val <= 10^5
# 0 <= skipA <= m
# 0 <= skipB <= n
# 如果 listA 和 listB 没有交点，intersectVal 为 0
# 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
#
#
#
#
# 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
#
#
from typing import List
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        快慢指针通常用于检测链表中是否有环，或者在链表中找到中点。在相交链表的情况下，它也可以用来找到相交点。
        在相交链表问题中，可以将其中一个链表的尾部连接到另一个链表的头部，形成一个环。然后使用快慢指针找到环的起始点，该点即为相交点。
        """
        # 双链表
        if not headA or not headB:
            return None

        # 将链表 A 的尾部连接到链表 B 的头节点
        tailA = headA
        while tailA.next:
            tailA = tailA.next
        tailA.next = headB

        # 使用快慢指针法找到环的起始节点
        slow = headA
        fast = headA

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # 相交
                # 重置其中一个指针到链表头节点，然后一次移动一步
                slow = headA
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # 恢复原始链表，返回相交节点
                tailA.next = None
                return slow

        # 恢复原始链表，未相交
        tailA.next = None
        return None


        # 双指针
        if not headA or not headB:
            return None

        ptrA, ptrB = headA, headB

        while ptrA != ptrB:
            # 如果当前链表指针到达末尾，则重定向到另一个链表的头节点
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA

        return ptrA

        # 哈希集合 #TODO None的情况
        node_s=set()
        cur=headA
        while cur:
            node_s.add(cur)
            cur=cur.next
        for node in node_s:
            print(node.val, end=" ")
        cur=headB
        while cur:
            if cur in node_s:
                return cur
            cur=cur.next

        # 王道解法
        # 如果两个链表为空，则返回空
        if headA == None or headB == None:
            return None

        # 计算链表A和链表B的长度
        lenA, lenB = 0, 0
        A, B = headA, headB
        while A != None:
            lenA += 1
            A = A.next
        while B != None:
            lenB += 1
            B = B.next

        # 将指针A和指针B移动到长度较小的链表的末尾
        if lenA > lenB:
            for i in range(lenA - lenB):
                A = A.next
        else:
            for i in range(lenB - lenA):
                B = B.next

        # 从链表A和链表B的末尾开始遍历，直到找到相交节点或遍历完整个链表
        while A:
            if A == B:
                return A
            A = A.next
            B = B.next

        # 如果没有相交节点，则返回空
        return None
# @lc code=end
node1 = ListNode(8)
node2 = ListNode(4)
node3 = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = node1
headA.next.next.next = node2
headA.next.next.next.next = node3

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = node1
headB.next.next.next.next = node2
headB.next.next.next.next.next = node3

solution = Solution()
print(solution.getIntersectionNode(headA, headB))
