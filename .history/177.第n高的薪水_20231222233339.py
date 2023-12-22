import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    计算第N高的薪水。

    参数：
        employee (pd.DataFrame): 包含员工信息的数据帧，其中包含'salary'列。
        N (int): 指定要查找的第N高的薪水。

    返回：
        pd.DataFrame: 包含第N高薪水的结果数据帧。

    注意：
        - 如果N小于等于0，返回pd.NA。
        - 如果N大于0且小于等于薪水计数字典的长度，则返回第N高的薪水。
        - 如果N大于薪水计数字典的长度，则返回pd.NA。
    """
    # 如果N小于等于0，设置第N高的薪水为pd.NA
    if N <= 0:
        nth_highest_salary = pd.NA
    else:
        # 根据薪水值进行计数，并按升序对计数结果进行排序
        salary_counts = employee['salary'].value_counts().sort_index(ascending=False)
        # 如果计数结果长度大于等于N，则返回第N高的薪水，否则返回pd.NA
        if len(salary_counts) >= N:
            nth_highest_salary = salary_counts.index[N-1]
        else:
            nth_highest_salary = pd.NA
    # 创建一个包含第N高薪水的结果数据帧
    result_df = pd.DataFrame({'getNthHighestSalary('+ str(N) +')': [nth_highest_salary]})
    return result_df

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    返回DataFrame中第N高的工资值

    参数：
    employee: 包含员工信息的DataFrame，其中包含'salary'列
    N: 第N高的工资值的索引

    返回值：
    包含第N高的工资值的DataFrame，如果找不到则返回None
    """
    # 将salary列中的工资值去重并存储在t中
    t = list(set(employee['salary']))
    # 对t进行排序
    t.sort()
    # 如果 N 小于等于 0
    if N <= 0:
        # 返回一个包含一个含有 pd.NA 元素的 DataFrame，列名为 f'getNthHighestSalary({N})'
        return pd.DataFrame([pd.NA], columns=[f'getNthHighestSalary({N})'])
    # 如果t的长度小于N，返回None
    if len(t) < N:
        ans = None
    else:
        # 否则返回去重排序后的第N个值
        ans = t[-N]
    # 返回一个包含单行的DataFrame，该行的列名为[f'getNthHighestSalary({N})']
    return pd.DataFrame([ans], columns=[f'getNthHighestSalary({N})'])

# 创建一个DataFrame
df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})

# 调用函数nth_highest_salary并打印结果
print(nth_highest_salary(df, 2))
