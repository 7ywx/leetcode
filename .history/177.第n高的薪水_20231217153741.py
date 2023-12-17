import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values(by='salary', ascending=False, inplace=True)
    num_rows = employee.shape[0]
    if num_rows < N:
        return   # 返回空的DataFrame或者抛出异常，根据你的需求来定
    else:
        return employee.iloc[N - 1].to_frame()  # 返回Series时减去1，因为索引是从0开始的

df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})
# 显示DataFrame
print(nth_highest_salary(df, 2))
