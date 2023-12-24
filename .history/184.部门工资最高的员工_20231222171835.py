import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employess_department = employee.merge(department, left_on='departmentId', right_on='id',how='inner')
    max_salary = employess_department.groupby('name_y')['salary'].idxmax()
    # department_highest_salary = employess_department[employess_department.groupby('name_y')['salary'].isin(max_salary)].rename(columns={'name_y': 'Department','name_x': 'Employee','salary': 'Salary'})[['Department','Employee','Salary']]
    department_highest_salary = employess_department[max_salary].rename(columns={'name_y': 'Department','name_x': 'Employee','salary': 'Salary'})[['Department','Employee','Salary']]
    return department_highest_salary

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

department_highest_salary(employee_df, department_df)
