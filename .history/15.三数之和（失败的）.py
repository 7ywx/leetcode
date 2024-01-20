#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (37.62%)
# Likes:    6658
# Dislikes: 0
# Total Accepted:    1.6M
# Total Submissions: 4.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
#
# 你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def twoSum(self, self_index, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for index, num in enumerate(nums):
            if index == self_index:
                continue
            if target - num in hashtable: # 在 if a in hashtable: 这样的条件判断中，Python会检查字典（哈希表）hashtable 的键（keys）中是否包含变量 a。也就是说，它不会查找值（values），而是查找键。
                return [nums[self_index], target - num, num] # [hashtable[target - num], index]
            hashtable[num] = index # 将当前元素及其下标存入哈希表
        return []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        hashtable = {}
        for index, num in enumerate(nums):
            if self.twoSum(index, nums, -num) and sorted(self.twoSum(index, nums, -num)) not in result:
                result.append(sorted(self.twoSum(index, nums, -num)))
        # print((result))
        return result
# @lc code=end
solution = Solution()
solution.threeSum([-1,0,1,2,-1,-4])
solution.threeSum([0,1,1])
