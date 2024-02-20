#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#
# https://leetcode.cn/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (66.31%)
# Likes:    1324
# Dislikes: 0
# Total Accepted:    249.7K
# Total Submissions: 376.1K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]'
#
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
#
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random
# 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
#
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random
# --> y 。
#
# 返回复制链表的头节点。
#
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
#
#
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
#
#
#
# 示例 1：
#
#
#
#
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
#
#
# 示例 2：
#
#
#
#
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
#
#
# 示例 3：
#
#
#
#
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
#
#
# 提示：
#
#
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。
#
#
#
#
#
from typing import Optional, List
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        复制一个带有随机指针的链表。

        参数:
            head: 原始链表的头节点。

        返回值:
            复制后链表的头节点。
        """
        original_node_dict = {}  # 创建字典用于存储原始节点及其索引
        node_dict = {}  # 创建字典用于存储复制节点及其索引
        dummy_head = Node(0)  # 创建虚拟头节点以简化代码
        current = dummy_head  # 初始化当前节点为虚拟头节点

        # 根据原始链表创建新链表（此时random指针指向原始链表节点）
        index = 0
        p = head
        while p:
            node_dict[index] = Node(x=p.val, random=p.random)  # 若current.random 不为None，则赋值给random属性
            current.next = node_dict[index]
            index += 1
            current = current.next
            p = p.next

        # 为原始链表节点创建索引字典
        index = 0
        current = head
        while current:
            original_node_dict[current] = index
            current = current.next
            index += 1

        # 更新复制链表中random指针，使其指向新链表中的对应节点
        current = dummy_head.next
        while current:
            current.random = node_dict.get(original_node_dict.get(current.random))
            current = current.next

        # 返回复制后的链表头节点
        return dummy_head.next
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
def print_linked_list(head: Node):
    """
    打印Node链表,random打印指向的值
    """
    while head is not None:
        print(f"Value: {head.val}, Next: {head.next.val if head.next else None}, Random: {head.random.val if head.random != None else None}")
        head = head.next

# 输入数据
head_data = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]

# 调用函数构建链表
linked_list_head = build_linked_list_from_2d_list(head_data)

solution = Solution()
res = solution.copyRandomList(linked_list_head)
print_linked_list(res)
