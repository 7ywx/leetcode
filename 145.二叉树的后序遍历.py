#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Easy (76.57%)
# Likes:    1163
# Dislikes: 0
# Total Accepted:    739.4K
# Total Submissions: 965.7K
# Testcase Example:  '[1,null,2,3]'
#
# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [0, 100] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：递归算法很简单，你可以通过迭代算法完成吗？
#
#
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 栈
        # if not root:
        #     return []
        # stack = []
        # res = []
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root = root.left
        #     root = stack.pop()
        #     res.append(root.val)
        #     root = root.left

        # #标签迭代
        # if not root:
        #     return []
        # stack = [root]
        # res = []
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # print(res)
        # return res[::-1]

        # # 递归
        # if not root:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
# @lc code=end
#标签 构建二叉树
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current_node = queue.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)

        i += 1

    return root

# 用给定的节点列表构建二叉树
nodes_list = [1, 2, 3, 4, 5]
root = build_tree(nodes_list)

# 给定的前序遍历数组
preorder_traversal = [1, 2, 3, 4, 5]

# 构建二叉树
root = build_tree(preorder_traversal)

solution = Solution()
print(solution.postorderTraversal(root))
