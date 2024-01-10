/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
class Solution
{
public:
    // vector<int> twoSum(vector<int> &nums, int target)
    // {
    //     vector<int> two;
    //     for (int i = 0; i < nums.size(); i++)
    //     {
    //         for (int j = i + 1; j < nums.size(); j++)
    //         {
    //             if (nums[i] + nums[j] == target)
    //             {
    //                 return {i, j};
    //             }
    //         }
    //     }
    //     return {};
    // }
    vector<int> twoSum(vector<int> &nums, int target)
    {
        // 哈希表，用于存储目标值与元素下标的对应关系
        unordered_map<int, int> hashtable;

        // 遍历数组
        for (int i = 0; i < nums.size(); ++i)
        {
            // 在哈希表中查找目标值与当前元素的差值
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end())
            {
                // 如果找到匹配的差值，则返回对应的两个元素下标
                return {it->second, i};
            }
            // 将当前元素及其下标存入哈希表
            hashtable[nums[i]] = i;
        }

        // 如果未找到匹配的差值，则返回空向量
        return {};
    }
};
int main()
{
    Solution s;
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    vector<int> two = s.twoSum(nums, target);
    for (int i = 0; i < two.size(); i++)
    {
        cout << two[i] << " ";
    }
    cout << endl;
}
// @lc code=end
