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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# @lc code=end

def build_linked_list_from_2d_list(head_data):
    """
    用一个列表来创建Node链表
    """
    # 创建一个字典用于快速查找节点
    node_dict = {}
    dummy_head = Node(0)  # 创建虚拟头节点
    current = dummy_head

    # 创建只带val的链表
    for index, (val, random_index) in enumerate(head_data):
        node_dict[index] = Node(x=val, random=random_index)
        current.next = node_dict[index]
        current = current.next

    current = dummy_head.next
    # 补充random指针
    while current:
        current.random = node_dict.get(current.random)
        current = current.next

    # 返回真实链表的头节点
    return dummy_head.next
