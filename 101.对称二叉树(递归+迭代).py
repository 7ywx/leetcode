#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (59.78%)
# Likes:    2659
# Dislikes: 0
# Total Accepted:    985.6K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
#
#
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 迭代
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue

            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True

        # 递归
        def isMirror(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2: # 异或
                return False
            if root1.val != root2.val:
                return False
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
        return isMirror(root.left, root.right)
# @lc code=end
def create_binary_tree(values):
    if not values:
        return None

    # 创建根节点
    root = TreeNode(values[0])
    queue = [root]
    front = 0
    index = 1
    while index < len(values):
        node = queue[front]
        front += 1

        # 创建左子节点
        item = values[index]
        index += 1
        if item is not None:
            left_number = item
            node.left = TreeNode(left_number)
            queue.append(node.left)

        # 如果还有元素，则创建右子节点
        if index >= len(values):
            break
        item = values[index]
        index += 1
        if item is not None:
            right_number = item
            node.right = TreeNode(right_number)
            queue.append(node.right)

    return root

# 使用提供的值创建二叉树
values = [1, 2, 2, 3, 4, 4, 3]
root = create_binary_tree(values)
print(Solution().isSymmetric(root))
