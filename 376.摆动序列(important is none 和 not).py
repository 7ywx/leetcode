#
# @lc app=leetcode.cn id=376 lang=python3
# @lcpr version=30200
#
# [376] 摆动序列
#
# https://leetcode.cn/problems/wiggle-subsequence/description/
#
# algorithms
# Medium (46.18%)
# Likes:    1229
# Dislikes: 0
# Total Accepted:    288.5K
# Total Submissions: 625.4K
# Testcase Example:  '[1,7,4,9,2,5]'
#
# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列
# 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。
#
#
#
# 例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。
#
# 相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5]
# 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
#
#
# 子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。
#
# 给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,7,4,9,2,5]
# 输出：6
# 解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
#
#
# 示例 2：
#
# 输入：nums = [1,17,5,10,13,15,10,5,16,8]
# 输出：7
# 解释：这个序列包含几个长度为 7 摆动序列。
# 其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
#
#
# 示例 3：
#
# 输入：nums = [1,2,3,4,5,6,7,8,9]
# 输出：2
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#
#
#
#
# 进阶：你能否用 O(n) 时间复杂度完成此题?
#
#

from typing import *
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        计算摆动序列的最大长度。摆动序列是指序列中的元素之间严格交替大于和小于。

        参数:
        nums: List[int] - 一个整数列表，用于计算摆动序列的最大长度。

        返回值:
        int - 摆动序列的最大长度。
        """
        # 初始化序列长度
        n = len(nums)
        # 初始化最大长度为0
        ans = 0

        # 初始化前一个数字为None
        prev = None
        # 初始化标志位为0，用于记录前一个数字和当前数字的大小关系
        flag = 0 # 1:大于, -1:小于
        # 遍历数字列表
        for num in nums:
            # 如果前一个数字为None，即当前是第一个数字
            if prev is None:
                prev = num
                ans += 1
            # 如果当前数字与前一个数字不相等
            elif prev != num:
                # 如果标志位为0，即前一个数字和当前数字的大小关系未确定
                if flag == 0:
                    ans += 1
                    flag = 1 if num > prev else -1
                    prev = num
                else:
                    t = 1 if num > prev else -1
                    # 如果当前数字和前一个数字的大小关系与标志位不同
                    if t != flag:
                        prev = num
                        flag = t
                        ans += 1
                    else:
                        prev = max(prev, num) if flag == 1 else min(prev, num)
        # 返回最大长度
        return ans
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,7,4,9,2,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,17,5,10,13,15,10,5,16,8]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9]\n
# @lcpr case=end

#
