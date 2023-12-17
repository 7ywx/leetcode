import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # 找到第二高的薪水
    if len(employee['salary'].dropna().sort_values(ascending=False)) >= 2:
        second_highest_salary = employee['salary'].dropna().sort_values(ascending=False).iloc[1]
        result_df = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
        return result_df
    else:
        result_df = pd.DataFrame({'SecondHighestSalary': [np.NaN]})
        return result_df


df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Salary': [50000, 60000, 55000, 65000]})
second
