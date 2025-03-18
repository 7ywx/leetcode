#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30103
#
# [18] 四数之和
#
# https://leetcode.cn/problems/4sum/description/
#
# algorithms
# Medium (36.73%)
# Likes:    2039
# Dislikes: 0
# Total Accepted:    680.1K
# Total Submissions: 1.9M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# 示例 2：
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 对数组进行排序，以便后续使用双指针法
        nums.sort()
        # 初始化答案列表，用于存储符合条件的四元组
        ans = []

        # 遍历数组，寻找所有可能的四元组组合
        for i in range(len(nums)):
            # 跳过重复的元素，避免重复计算
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # 在i之后的元素中寻找其他三个数
            for j in range(i+1, len(nums)-1):
                # 跳过重复的元素，避免重复计算
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                # 初始化双指针，分别指向当前i和j之后的开始和结束位置
                left, right = j+1, len(nums)-1
                # 使用双指针法寻找符合条件的两个数
                while left < right:
                    # 计算当前四个数的和
                    sum4 = nums[i] + nums[j] + nums[left] + nums[right]
                    # 根据和与目标值的比较，移动指针
                    if sum4 > target:
                        right -= 1
                    elif sum4 < target:
                        left += 1
                    else:
                        # 找到符合条件的四元组，添加到答案列表中
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        # 跳过所有重复的元素，避免重复计算
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right-1] == nums[right]:
                            right -= 1
                        # 移动指针，继续寻找下一组符合条件的数
                        left += 1
                        right -= 1
        # 返回所有符合条件的四元组
        return ans

# @lc code=end

s = Solution()
s.fourSum([1,0,-1,0,-2,2], 0)
#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#
