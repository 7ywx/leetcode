import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    salary = employee.sort_values(by='salary', ascending=False,)
    num_rows = salary.shape[0]
    if num_rows < N:
        nth_highest_salary = pd.NA
    else:
        nth_highest_salary = salary['salary'].iloc[N - 1]  # 返回Series时减去1，因为索引是从0开始的
    result_df = pd.DataFrame({'getNthHighestSalary(2) ': [second_highest_salary]})
    return result_df

df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
# 显示DataFrame
print(nth_highest_salary(df, 2))
