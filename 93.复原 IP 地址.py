#
# @lc app=leetcode.cn id=93 lang=python3
# @lcpr version=30104
#
# [93] 复原 IP 地址
#
# https://leetcode.cn/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (60.95%)
# Likes:    1508
# Dislikes: 0
# Total Accepted:    506.8K
# Total Submissions: 827.2K
# Testcase Example:  '"25525511135"'
#
# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
#
#
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312"
# 和 "192.168@1.1" 是 无效 IP 地址。
#
#
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能
# 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#
#
# 示例 2：
#
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#
#
# 示例 3：
#
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 20
# s 仅由数字组成
#
#
#

from typing import *
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        path = []
        ans = list()
        n = len(s)
        if n > 12:
            return ans

        def isValidIp(ip):
            if ip[0] == "0" and len(ip) != 1:
                return False
            if -1 < int(ip) < 256:
                return True
        
        def backtrack(start, path):
            if len(path) > 4:
                return
            if len(path) == 4 and start == n:
                ans.append(".".join(path[:]))
                return
            for end in range(start+1, n+1):
                if end > start + 3:
                    break
                if isValidIp(s[start:end]):
                    backtrack(end, path + [s[start:end]])
        backtrack(0, [])
        return list(ans)
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    # your test code here
    solution.restoreIpAddresses("12345678910111213141")



#
# @lcpr case=start
# "25525511135"\n
# @lcpr case=end

# @lcpr case=start
# "0000"\n
# @lcpr case=end

# @lcpr case=start
# "101023"\n
# @lcpr case=end

#
