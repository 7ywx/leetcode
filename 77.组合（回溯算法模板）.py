#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.29%)
# Likes:    1682
# Dislikes: 0
# Total Accepted:    782.3K
# Total Submissions: 1M
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1
# 1
#
#
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtracking(i+1, path)
                path.pop()
        backtracking(1,[])
        return res
# @lc code=end
result = []
def backtrack(选择列表, 路径):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        # 做选择
        路径.add(选择)
        将该选择从选择列表移除
        backtrack(选择列表, 路径) # 核心 递归调用之前【做选择】，调用之后【撤销选择】
        # 撤销选择
        路径.remove(选择)
        将该选择再加入选择列表
'''
作者：缓缓
链接：https://leetcode.cn/problems/combination-sum/solutions/1542788/by-huan-huan-20-k3hb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
