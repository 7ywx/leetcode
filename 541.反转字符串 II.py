#
# @lc app=leetcode.cn id=541 lang=python3
# @lcpr version=30103
#
# [541] 反转字符串 II
#
# https://leetcode.cn/problems/reverse-string-ii/description/
#
# algorithms
# Easy (58.13%)
# Likes:    665
# Dislikes: 0
# Total Accepted:    356.5K
# Total Submissions: 613.2K
# Testcase Example:  '"abcdefg"\n2'
#
# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。
#
#
# 如果剩余字符少于 k 个，则将剩余字符全部反转。
# 如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
#
#
#
#
# 示例 1：
#
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#
#
# 示例 2：
#
# 输入：s = "abcd", k = 2
# 输出："bacd"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅由小写英文组成
# 1 <= k <= 10^4
#
#
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 将输入的字符串转换为列表，以便进行就地修改
        s = list(s)
        # 计算字符串的长度
        n = len(s)
        # 计算可以进行完整反转的次数
        times = n//(2*k)

        # 对于每个完整的反转周期
        for i in range(times):
            # 反转当前周期内的子字符串
            s[i*2*k : (i*2+1)*k] = s[i*2*k : (i*2+1)*k][::-1]

        # 处理剩余的部分，如果剩余长度大于k
        if n % (2*k) > k:
            # 只反转剩余部分的前k个字符
            s[times*2*k : (times*2+1)*k] = s[times*2*k : (times*2+1)*k][::-1]
        else:
            # 如果剩余长度不大于k，反转所有剩余的字符
            s[times*2*k :] = s[times*2*k : ][::-1]

        # 最后，将修改后的字符列表重新连接成字符串并返回
        return "".join(s)

# @lc code=end
s = Solution()
s.reverseStr("abcdefg", 2)


#
# @lcpr case=start
# "abcdefg"\n2\n
# @lcpr case=end

# @lcpr case=start
# "abcd"\n2\n
# @lcpr case=end

#
