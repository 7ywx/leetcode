import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values(by='salary', ascending=False, inplace=True)
    num_rows = employee.shape[0]
	if  < N:
		return pd.NA
	else:
		return employee.iloc[N])

df = pd.DataFrame({'id': [1, 2, 3], 'salary': [100, 200, 300]})

# 显示DataFrame
print(df)
