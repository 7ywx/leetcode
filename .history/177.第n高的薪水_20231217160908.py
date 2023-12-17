import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N < 0:
        nth_highest_salary = pd.NA
    else:
        salary_counts = employee['salary'].value_counts().sort_index(ascending=False)
        # 如果至少有两个不同的薪水，那么取第二个（即第二高的）
        if len(salary_counts) >= N:
            nth_highest_salary = salary_counts.index[N-1]
        else:
            nth_highest_salary = pd.NA
        result_df = pd.DataFrame({'getNthHighestSalary('+ str(N) +')': [nth_highest_salary]})
        return result_df

df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
# 显示DataFrame
print(nth_highest_salary(df, 2))
