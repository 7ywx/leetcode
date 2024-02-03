#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode.cn/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (75.09%)
# Likes:    1698
# Dislikes: 0
# Total Accepted:    370.2K
# Total Submissions: 492.7K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
#
#
# 示例 2:
#
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内
#
#
#
#
# 进阶：你可以在 O(1) 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 不被视为 额外空间。）
#
#
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length

        # 初始化最左侧的乘积 #TODO answer = [1] * length 为什么慢？
        answer[0] = 1
        # left
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]

        # 初始化最右侧的乘积
        R = 1
        # right
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


        # 初始化结果列表与辅助变量
        result = [1] * len(nums)
        left_or_right_product = 1

        # 计算左半部分的乘积，并更新结果列表
        for i in range(len(nums) - 1):
            left_or_right_product *= nums[i]
            result[i + 1] = left_or_right_product

        # 计算右半部分的乘积，并更新结果列表
        left_or_right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            left_or_right_product *= nums[i + 1]
            result[i] *= left_or_right_product

        return result

        # n = len(nums)
        # left = [1] * n
        # right = [1] * n
        # for i in range(1, n):
        #     left[i] = left[i - 1] * nums[i - 1]
        # for i in range(n - 2, -1, -1):
        #     right[i] = right[i + 1] * nums[i + 1]
        # answer = [l * r for l, r in zip(left, right)]
        # return answer
# @lc code=end
solution = Solution()
print(solution.productExceptSelf(nums = [1,2,3,4]))
