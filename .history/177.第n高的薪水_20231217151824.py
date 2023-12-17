import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values(by='Salary', ascending=False, inplace=True)
