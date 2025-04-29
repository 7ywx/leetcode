#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (44.49%)
# Likes:    2477
# Dislikes: 0
# Total Accepted:    668K
# Total Submissions: 1.5M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
#
#
# 0 <= j <= nums[i] 
# i + j < n
#
#
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 示例 2:
#
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]
#
#
#
from typing import List
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # 官方题解
        n = len(nums)
        maxPos = 0 # 记录当前能到达的最远位置
        end = 0 # 记录当前位置的边界
        step = 0 # 记录跳跃次数
        for i in range(n - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
        return step

        # # c++改python
        # step = 0
        # start = 0
        # end = 1
        # numsLength = len(nums)
        # while end < numsLength:
        #     maxPos = 0
        #     for i in range(start, end):
        #         maxPos = max(maxPos, i + nums[i])
        #     start = end
        #     end = maxPos + 1
        #     step += 1
        # return step

        jump = {0:0} # 存储每个位置的最小跳跃次数
        maxJump = 0
        for i in range(len(nums)):
            maxJump = max(maxJump, i + nums[i])
            for j in range(i+1, maxJump+1): # 遍历当前位置能到达的所有位置
                if j not in jump or jump[j] > jump[i] + 1: # 如果当前位置能到达的位置没有记录，或者记录的次数比当前位置的次数多
                    jump[j] = jump[i] + 1
        return jump[len(nums)-1]
# @lc code=end
s = Solution()
print(s.jump([2,3,1,1,4]))
print(s.jump([1,2,3]))
