import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_name = []
    for row in employee.itertuples():
        print(employee.loc[employee.id == row.managerId][salary])
    #     if not pd.isna(row.managerId):
    #         if row.salary > employee.loc[employee.id == row.managerId, 'salary'].astype(int):
    #             employee_name.append(row.name)
    # return pd.DataFrame(employee_name, columns=['Employee'])


data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]
}
data1 = {
    'id': [1, 3, 2],
    'name': ['Mark', 'Jack', 'Alan'],
    'salary': [40000, 30000, 20000],
    'managerId': [3, 2, None]
}
df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print(find_employees(df))
