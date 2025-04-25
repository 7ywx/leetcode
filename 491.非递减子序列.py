#
# @lc app=leetcode.cn id=491 lang=python3
# @lcpr version=30200
#
# [491] 非递减子序列
#
# https://leetcode.cn/problems/non-decreasing-subsequences/description/
#
# algorithms
# Medium (52.44%)
# Likes:    856
# Dislikes: 0
# Total Accepted:    228K
# Total Submissions: 433.9K
# Testcase Example:  '[4,6,7,7]'
#
# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
#
# 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。
#
#
#
# 示例 1：
#
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
# 示例 2：
#
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
#
#
#

from typing import *
# @lc code=start
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(start, path):
            if len(path) > 1:
                ans.append(path[:])

            uset = set()
            for i in range(start, n):
                if nums[i] in uset:
                    continue
                uset.add(nums[i])
                if not path:
                    backtrack(i+1, path+[nums[i]])
                elif path[-1] <= nums[i]:
                    backtrack(i+1, path+[nums[i]])

        backtrack(0, [])
        return ans

# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [4,6,7,7]\n
# @lcpr case=end

# @lcpr case=start
# [4,4,3,2,1]\n
# @lcpr case=end

#
