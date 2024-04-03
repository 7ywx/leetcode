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
        dp = [nums[0]] + [0] * (len(nums) - 1)
        tail = []
        if nums[0] < 0:
            tail.append(0)
        for i in range(1, len(nums)):
            if nums[i] > 0:
                if dp[i-1] > 0:
                    dp[i] = dp[i-1] * nums[i]
                else:
                    dp[i] = nums[i]
            elif nums[i] < 0:
                tail.append(i)
                if len(tail) % 2 == 0:
                    temp = 1
                    for j in range(tail[0], tail[-1] + 1):
                        temp *= nums[j]
                    if tail[0] > 0 and dp[tail[0] - 1] > 0:
                        temp *= dp[tail[0] - 1]
                    dp[i] = temp
                    # temp = 1
                    # for index, t in enumerate(tail):
                    #     if t > 0 and tail[index - 1] + 1 != t:
                    #         temp *= nums[t] * dp[t-1]
                    #     else:
                    #         temp *= nums[t]
                    # dp[i] = temp
                else:
                    if len(tail) == 1:
                        dp[i] = nums[i]
                    else:
                        temp = nums[i]
                        for j in range(tail[1], tail[-1]):
                            temp *= nums[j]
                        if tail[1] > 0 and dp[tail[1]-1] > 0:
                            temp *= dp[tail[1]-1]
                        dp[i] = temp
                    # temp = 1
                    # for t in range(1, len(tail)):
                    #     if tail[t] > 0 and tail[t-1] + 1 != tail[t]:
                    #         temp *= nums[tail[t]] * dp[tail[t]-1]
                    #     else:
                    #         temp *= nums[tail[t]]
                    # dp[i] = temp if len(tail) != 1 else nums[i]
            else:
                tail.clear()
        return max(dp)

        # dp = [nums[0]] + [0] * (len(nums)-1)
        # tail = []
        # if nums[0] < 0:
        #     tail.append(0)
        # for i in range(1, len(nums)):
        #     if nums[i] == 0:
        #         tail.clear()
        #     elif nums[i] < 0:
        #         if not tail:
        #             tail.append(i)
        #             dp[i] = nums[i]
        #         else:
        #             if tail[0] != i-1:
        #                 dp[i] = dp[i-1] * nums[tail.pop()] * nums[i]
        #             else:
        #                 t = tail.pop()
        #                 if dp[t-1] > 0:
        #                     dp[i] = dp[t-1] * nums[t] * nums[i]
        #                 else:
        #                     dp[i] = nums[t] * nums[i]
        #     else:
        #         dp[i] = max(nums[i] * dp[i - 1], nums[i])
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
# print(s.maxProduct([2,3,-2,4]))

# print(s.maxProduct([0,2]))
# print(s.maxProduct([3,-1,4]))
# print(s.maxProduct([-3,-1,-1]))
print(s.maxProduct([7,-2,-4]))
# print(s.maxProduct([-2,-3,7]))
# print(s.maxProduct([2,-5,-2,-4,3]))
# print(s.maxProduct([-2,0,-1]))
# print(s.maxProduct([1,2,-1,-2,2,1,-2,1]))
# print(s.maxProduct([1,2,-1,-2,2,1,-2,1,4,-5,4]))
