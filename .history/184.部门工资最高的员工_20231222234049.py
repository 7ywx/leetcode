import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # 将employee表和department表根据departmentId和id进行合并
    e_d = employee.merge(department, left_on='departmentId', right_on='id', how='inner')

    # 给合并后的表添加一个新列max_salary，该列通过groupby函数找到每个name_y（部门）对应的salary的最大值
    e_d['max_salary'] = e_d.groupby('name_y')['salary'].transform('max')

    # 从合并后的表中筛选出salary等于max_salary的行，并重新命名列名
    department_highest_salary = e_d[e_d.salary == e_d.max_salary].rename(columns={'name_y': '部门', 'name_x': '员工', 'salary': '工资'})

    # 只选择部门、员工和工资这三列返回
    department_highest_salary = department_highest_salary[['部门', '员工', '工资']]

    # 返回结果
    return department_highest_salary


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df=employee.merge(department,left_on="departmentId",right_on="id",how="left")
    e_d = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    df.rename(columns={"name_x":"Employee","name_y":"Department","salary":"Salary"},inplace=True)
    max_salary=df.groupby("Department")["Salary"].transform("max")
    df=df[df["Salary"]==max_salary]
    print(df)
    return df[["Department","Employee","Salary"]]

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
