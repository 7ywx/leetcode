import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    e_d = employee.merge(department, left_on='departmentId', right_on='id',how='inner')
    e_d['max_salary'] = e_d.groupby('name_y')['salary'].transform('max')
    department_highest_salary = e_d[e_d.salary == e_d.max_salary].rename(columns={'name_y': 'Department','name_x': 'Employee','salary': 'Salary'})[['Department','Employee','Salary']]
    return department_highest_salary

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge employee and department dataframes on departmentId and id respectively
    e_d = employee.merge(department, left_on='departmentId', right_on='id', how='inner')

    # Calculate the maximum salary for each department
    e_d['max_salary'] = e_d.groupby('name_y')['salary'].apply(lambda x: x.max())

    # Filter to get the employees with the highest salary in their department
    highest_earners = e_d[e_d['salary'] == e_d['max_salary']].reset_index(drop=True)

    # Rename columns for better understanding
    highest_earners = highest_earners.rename(columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})

    # Select the columns of interest
    result = highest_earners[['Department', 'Employee', 'Salary']]
    print(result)
    return result

# def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
#     df=employee.merge(department,left_on="departmentId",right_on="id",how="left")
#     df.rename(columns={"name_x":"Employee","name_y":"Department","salary":"Salary"},inplace=True)
#     max_salary=df.groupby("Department")["Salary"].transform("max")
#     df=df[df["Salary"]==max_salary]
#     return df[["Department","Employee","Salary"]]

employee_data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 90000, 80000, 60000, 90000],
    'departmentId': [1, 1, 2, 2, 1]
}

# 部门表数据
department_data = {
    'id': [1, 2],
    'name': ['IT', 'Sales']
}

# 创建员工DataFrame
employee_df = pd.DataFrame(employee_data)
# 创建部门DataFrame
department_df = pd.DataFrame(department_data)
department_highest_salary(employee_df, department_df)
