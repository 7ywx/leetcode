import pandas as pd
 def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    """
    计算每行薪水中的第N高的薪水。

    参数：
        employee (pd.DataFrame): 包含员工信息的数据帧，其中包含'salary'列。
        N (int): 第N高的薪水。

    返回：
        pd.DataFrame: 包含第N高薪水的结果数据帧。
    """
    if N <= 0:
        nth_highest_salary = pd.NA
    else:
        salary_counts = employee['salary'].value_counts().sort_index(ascending=False)
        if len(salary_counts) >= N:
            nth_highest_salary = salary_counts.index[N-1]
        else:
            nth_highest_salary = pd.NA
    result_df = pd.DataFrame({'getNthHighestSalary('+ str(N) +')': [nth_highest_salary]})
    return result_df

# 创建示例数据帧
df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})

# 调用函数并打印结果
print(nth_highest_salary(df, 2))
