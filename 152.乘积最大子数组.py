#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode.cn/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (43.17%)
# Likes:    2217
# Dislikes: 0
# Total Accepted:    421.5K
# Total Submissions: 976.7K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
#
# 测试用例的答案是一个 32-位 整数。
#
#
#
# 示例 1:
#
#
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#
#
# 示例 2:
#
#
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
#
#
#
from typing import List
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 当前位置的最优解未必是由前一个位置的最优解转移得到的。

        # 初始化最大乘积和最小乘积列表，起始值为列表的第一个元素
        maxF, minF = [nums[0]], [nums[0]]

        for i in range(1, len(nums)):
            num = nums[i]
            index = i
            # 计算当前位置的最大乘积和最小乘积
            maxF.append(max(num, maxF[index-1] * num, minF[index-1] * num))
            minF.append(min(num, minF[index-1] * num, maxF[index-1] * num))
        # 返回最大乘积
        return max(maxF)

        # dp = [nums[0]] + [0] * (len(nums) - 1)
        # tail = []
        # if nums[0] < 0:
        #     tail.append(0)
        # for i in range(1, len(nums)):
        #     if nums[i] > 0:
        #         if dp[i-1] > 0:
        #             dp[i] = dp[i-1] * nums[i]
        #         else:
        #             dp[i] = nums[i]
        #     elif nums[i] < 0:
        #         tail.append(i)
        #         if len(tail) % 2 == 0:
        #             temp = 1
        #             for j in range(tail[0], tail[-1] + 1):
        #                 temp *= nums[j]
        #             if tail[0] > 0 and dp[tail[0] - 1] > 0:
        #                 temp *= dp[tail[0] - 1]
        #             dp[i] = temp
        #         else:
        #             if len(tail) == 1:
        #                 dp[i] = nums[i]
        #             else:
        #                 temp = nums[i]
        #                 for j in range(tail[1], tail[-1]):
        #                     temp *= nums[j]
        #                 if tail[1] > 0 and dp[tail[1]-1] > 0:
        #                     temp *= dp[tail[1]-1]
        #                 dp[i] = temp
        #     else:
        #         tail.clear()
        # return max(dp)

        # dp = nums[:]
        # for i in range(1, len(nums)):
        #     t = nums[i]
        #     for j in range(i-1, -1, -1):
        #         if nums[j] == 0:
        #             break
        #         else:
        #             t *= nums[j]
        #             if t > dp[i]:
        #                 dp[i] = t
        # return max(dp)
# @lc code=end
s = Solution()
print(s.maxProduct([2,3,-2,4]))

# print(s.maxProduct([0,2]))
# print(s.maxProduct([3,-1,4]))
# print(s.maxProduct([-3,-1,-1]))
# print(s.maxProduct([7,-2,-4]))
# print(s.maxProduct([-2,-3,7]))
# print(s.maxProduct([2,-5,-2,-4,3]))
# print(s.maxProduct([-2,0,-1]))
# print(s.maxProduct([1,2,-1,-2,2,1,-2,1]))
# print(s.maxProduct([1,2,-1,-2,2,1,-2,1,4,-5,4]))
