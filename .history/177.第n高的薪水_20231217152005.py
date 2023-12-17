import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values(by='salary', ascending=False, inplace=True)
	if len()
