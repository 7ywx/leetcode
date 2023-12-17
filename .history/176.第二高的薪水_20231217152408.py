import pandas as pd
import numpy as np
# def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
#     # 找到第二高的薪水
#     if len(employee['salary'].dropna().sort_values(ascending=False)) >= 2:
#         second_highest_salary = employee['salary'].dropna().sort_values(ascending=False).iloc[1]
#         result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
#         return result_df
#     else:
#         result_df = pd.DataFrame({'SecondHighestSalary': [np.NaN]})
#         return result_df

# def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
#     # 使用 numpy 提供的 unique 函数来找到唯一的薪水，并按照降序排列
#     unique_salaries = np.unique(employee['salary'].dropna())
#     # 如果至少有两个不同的薪水，那么取第二个（即第二高的）
#     if len(unique_salaries) >= 2:
#         second_highest_salary = unique_salaries[-2]  # 倒数第二个薪水
#     else:
#         second_highest_salary = np.nan  # 如果只有一个或没有薪水，就用 NaN 表示
#     # 创建包含第二高薪水的 DataFrame
#     result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
#     return result_df
def second_highest_salary(employee: pd.DataFrame) -> pd.Series:
    # 使用 value_counts 来获取薪水的计数并按降序排序
    salary_counts = employee['salary'].value_counts().sort_index(ascending=False)
    # 如果至少有两个不同的薪水，那么取第二个（即第二高的）
    if len(salary_counts) >= 2:
        second_highest_salary = salary_counts.index[1]
    else:
        second_highest_salary = pd.NA  # 如果只有一个或没有薪水，就用 NA 表示
    # 创建包含第二高薪水的 Series
#     result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
#     return result_df

df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'salary': [50000, 60000, 55000, 65000]})
print(second_highest_salary(df))
