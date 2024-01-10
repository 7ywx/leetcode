import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    return  employee.merge(department, left_on='departmentId', right_on='id',how='inner').groupby('name_y').nlargest().reset_index()

# Create the DataFrame for Employee table
employee_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
})

# Create the DataFrame for Department table
department_df = pd.DataFrame({
    'id': [1, 2],
    'name': ['IT', 'Sales']
})

print(department_highest_salary(employee_df, department_df))
