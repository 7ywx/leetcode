#
# @lc app=leetcode.cn id=332 lang=python3
# @lcpr version=30200
#
# [332] 重新安排行程
#
# https://leetcode.cn/problems/reconstruct-itinerary/description/
#
# algorithms
# Hard (44.25%)
# Likes:    965
# Dislikes: 0
# Total Accepted:    124.8K
# Total Submissions: 283.7K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给你一份航线列表 tickets ，其中 tickets[i] = [fromi, toi]
# 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。
#
# 所有这些机票都属于一个从 JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK
# 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
#
#
# 例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前。
#
#
# 假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。
#
#
#
# 示例 1：
#
# 输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# 输出：["JFK","MUC","LHR","SFO","SJC"]
#
#
# 示例 2：
#
# 输入：tickets =
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。
#
#
#
#
# 提示：
#
#
# 1 <= tickets.length <= 300
# tickets[i].length == 2
# fromi.length == 3
# toi.length == 3
# fromi 和 toi 由大写英文字母组成
# fromi != toi
#
#
#

from typing import *
from collections import defaultdict
# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # graph = defaultdict(list)
        # for src, dst in tickets:
        #     graph[src].append(dst)
        # for key in graph:
        #     graph[key].sort(reverse=True)  # 按字典序逆序存储以便后续弹出最小值

        # 创建一个集合来存储所有出现过的机场
        airports = set()
        for src, dst in tickets:
            airports.add(src)
            airports.add(dst)

        # 将机场映射到索引
        airport_to_index = {airport: idx for idx, airport in enumerate(sorted(airports))}
        num_airports = len(airport_to_index)

        # 初始化邻接矩阵
        graph = [[0] * num_airports for _ in range(num_airports)]

        # 填充邻接矩阵
        for src, dst in tickets:
            graph[airport_to_index[src]][airport_to_index[dst]] += 1

        for row in graph:
            print(row)
        print(airport_to_index)

        ans = []
        def dfs(src="JFK", path=["JFK"]):
            nonlocal ans
            if len(path) == len(tickets) + 1:
                if not ans:
                    ans = path[:]
                elif ''.join(path) < ''.join(ans):
                    ans = path[:]

                print(ans)
                return

            for dst_idx in range(num_airports):
                if graph[airport_to_index[src]][dst_idx] > 0:
                    graph[airport_to_index[src]][dst_idx] -= 1
                    dfs(list(airport_to_index.keys())[dst_idx], path + [list(airport_to_index.keys())[dst_idx]])
                    graph[airport_to_index[src]][dst_idx] += 1

        dfs()
        print(True if "ATL" < "SFO" else False)
        print(f"ans = {ans}")
        return ans
# @lc code=end
if __name__ == '__main__':
    solution = Solution()
    solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
    # your test code here



#
# @lcpr case=start
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]\n
# @lcpr case=end

# @lcpr case=start
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]\n
# @lcpr case=end

#
