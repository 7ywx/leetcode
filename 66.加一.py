from typing import List
#
# @lc app=leetcode.cn id=66 lang=python3
# @lcpr version=20001
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (46.22%)
# Likes:    1433
# Dislikes: 0
# Total Accepted:    784.9K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#
#
# 示例 1：
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#
#
# 示例 2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#
#
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if i == len(digits)-1:
                c, digits[-1] = divmod(digits[-1]+1, 10)
                continue
            if c == 0:
                break
            else:
                c, digits[i] = divmod(digits[i]+c, 10)
        if c != 0:
            digits.insert(0, c)
        return digits
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [4,3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
