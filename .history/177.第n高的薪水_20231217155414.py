import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee.sort_values(by='salary', ascending=False,)
    num_rows = salary.shape[0]
    salary_counts = employee['salary'].value_counts().sort_index(ascending=False)
    # 如果至少有两个不同的薪水，那么取第二个（即第二高的）
    if len(salary_counts) >= N:
        second_highest_salary = salary_counts.index[1]
    else:
        second_highest_salary = pd.NA  # 如果只有一个或没有薪水，就用 NA 表示

    if num_rows < N:
        nth_highest_salary = pd.NA
    else:
        nth_highest_salary = salary['salary'].iloc[N - 1]  # 返回Series时减去1，因为索引是从0开始的
    result_df = pd.DataFrame({'getNthHighestSalary('+ str(N) +')': [nth_highest_salary]})
    return result_df

df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
# 显示DataFrame
print(nth_highest_salary(df, 2))
