#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#
# https://leetcode.cn/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (66.77%)
# Likes:    1908
# Dislikes: 0
# Total Accepted:    977.9K
# Total Submissions: 1.5M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
#
#
# 示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [0, 2000] 内
# -1000 <= Node.val <= 1000
#
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        算法流程：
            1. 特例处理： 当根节点为空，则返回空列表 [] 。
            2. 初始化： 打印结果列表 res = [] ，包含根节点的队列 queue = [root] 。
            3. BFS 循环： 当队列 queue 为空时跳出。
                a. 新建一个临时列表 tmp ，用于存储当前层打印结果。
                b. 当前层打印循环： 循环次数为当前层节点数（即队列 queue 长度）。
                    a. 出队： 队首元素出队，记为 node。
                    b. 打印： 将 node.val 添加至 tmp 尾部。
                    c. 添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue 。
                c. 将当前层结果 tmp 添加入 res 。
            4. 返回值： 返回打印结果列表 res 即可。
        """
        if not root:
            return []
        res = []
        queue = collections.deque() # double-ended queue
        queue.append(root)
        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res

        # if not root:
        #     return []
        # stack = []
        # res = []
        # depth = 1
        # while root or stack:
        #     if not res:
        #         res.append([root.val])
        #     else:
        #         if depth != root_depth[1]:
        #             res.append([])
        #             depth = root_depth[1]
        #         res[-1].append(root.val)
        #     if root.left:
        #         stack.append((root.left, depth + 1))
        #     if root.right:
        #         stack.append((root.right, depth + 1))
        #     if stack:
        #         root_depth = stack.pop(0)
        #         root = root_depth[0]
        #     else:
        #         root = None
        # return res
# @lc code=end
def build_tree(nodes):
    # 如果节点列表为空，则返回空树
    if not nodes:
        return None

    # 创建根节点
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1 # 节点数量

    # 使用队列进行层次遍历构建二叉树
    while queue and i < len(nodes):
        current_node = queue.pop(0)

        # 如果当前节点的值不为空，则创建左子节点
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)

        i += 1

        # 如果当前节点的值不为空，则创建右子节点
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)

        i += 1

    # 返回根节点
    return root

# 用给定的节点列表构建二叉树
nodes_list =  [1,2,3,4,5]
root = build_tree(nodes_list)

solution = Solution()
print(solution.levelOrder(root))
