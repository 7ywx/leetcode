#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode.cn/problems/path-sum-iii/description/
#
# algorithms
# Medium (48.53%)
# Likes:    1811
# Dislikes: 0
# Total Accepted:    276K
# Total Submissions: 569.5K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#
#
# 示例 2：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,1000]
# -10^9  
# -1000  
#
#
#
from typing import Optional, List
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 初始化前缀和计数字典，初始时，前缀和为 0 出现一次
        prefix_sum_count = {0: 1}

        # 标签 定义深度优先搜索函数
        def dfs(node, current_sum):
            # 初始化结果变量，记录满足条件的路径数量
            result = 0

            # 递归终止条件：节点为空
            if not node:
                return 0

            # 计算当前节点的值加到当前路径和上
            current_sum += node.val

            # 判断在当前节点之前的路径上是否存在前缀和 current_sum - targetSum
            # 如果存在，说明存在一条路径满足条件，累加到结果中
            result += prefix_sum_count.get(current_sum - targetSum, 0)

            # 更新当前前缀和的计数
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

            # 递归处理左右子树
            result += dfs(node.left, current_sum)
            result += dfs(node.right, current_sum)

            # 标签 回溯，移除当前节点对前缀和计数的影响
            prefix_sum_count[current_sum] -= 1

            return result

        # 调用深度优先搜索函数，从根节点开始递归
        return dfs(root, 0)

    #     prefix_sum_count = {0: 1}  # 初始化前缀和字典，key为前缀和，value为出现的次数
    #     return self.dfs(root, targetSum, 0, prefix_sum_count)

    # def dfs(self, node, target, current_sum, prefix_sum_count):
    #     if not node:
    #         return 0

    #     current_sum += node.val  # 计算当前节点的前缀和
    #     count = prefix_sum_count.get(current_sum - target, 0)  # 判断是否存在满足条件的前缀和
    #     prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1  # 更新前缀和字典

    #     # 递归处理左右子树
    #     count += self.dfs(node.left, target, current_sum, prefix_sum_count)
    #     count += self.dfs(node.right, target, current_sum, prefix_sum_count)

    #     # 回溯，更新前缀和字典
    #     prefix_sum_count[current_sum] -= 1

    #     return count


    #     if not root:
    #         return 0

    #     # 从当前节点出发的路径和等于给定值的数量
    #     count_from_current = self.count_paths_from_node(root, targetSum)

    #     # 递归处理左右子树
    #     count_left = self.pathSum(root.left, targetSum)
    #     count_right = self.pathSum(root.right, targetSum)

    #     # 总路径数量等于当前节点出发的路径数 + 左子树的路径数 + 右子树的路径数
    #     return count_from_current + count_left + count_right

    # def count_paths_from_node(self, node, targetSum):
    #     if not node:
    #         return 0

    #     # 从当前节点出发的路径和等于给定值的数量
    #     count = 0

    #     # 路径和等于给定值时，计数加一
    #     if node.val == targetSum:
    #         count += 1

    #     # 递归处理左右子树，注意减去当前节点的值
    #     count += self.count_paths_from_node(node.left, targetSum - node.val)
    #     count += self.count_paths_from_node(node.right, targetSum - node.val)

    #     return count

# @lc code=end
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

solution = Solution()
result = solution.pathSum(root, 8)
print(result)

# 用例示例
my_tree = TreeNode(1)
my_tree.left = TreeNode(-2)
my_tree.right = TreeNode(-3)

result = solution.pathSum(my_tree, -1)
print(result)
