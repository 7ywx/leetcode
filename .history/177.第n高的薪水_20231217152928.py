import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values(by='salary', ascending=False, inplace=True)
	if employee.shape[0] < N:
		return pd.NA
	else:
		return employee.iloc[N])
