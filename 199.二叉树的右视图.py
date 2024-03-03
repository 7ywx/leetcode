#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode.cn/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (66.65%)
# Likes:    1036
# Dislikes: 0
# Total Accepted:    374.5K
# Total Submissions: 561.7K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
#
#
# 示例 2:
#
#
# 输入: [1,null,3]
# 输出: [1,3]
#
#
# 示例 3:
#
#
# 输入: []
# 输出: []
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,100]
# -100  
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 标签  BFS 层序遍历
        """
        算法流程：
            1. 特例处理： 当根节点为空，则返回空列表 [] 。
            2. 初始化： 结果列表 res = [] ，包含根节点的队列 queue = [root] 。
            3. BFS 循环： 当队列 queue 为空时跳出。
                a. 当前层打印循环： 循环次数为当前层节点数（即队列 queue 长度）。
                    a. 出队： 队首元素出队，记为 node。
                    b. 打印： 如果为右边界，则将 node.val 添加至 res 尾部。
                    c. 添加子节点： 若 node 的左（右）子节点不为空，则将左（右）子节点加入队列 queue 。
            4. 返回值： 返回打印结果列表 res 即可。
        """
        if not root:
            return []
        res = []
        queue = collections.deque() # double-ended queue
        queue.append(root)
        while queue:
            num = len(queue)
            for i in range(num):
                node = queue.popleft()
                if i == num - 1: # 右边界
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
# @lc code=end
