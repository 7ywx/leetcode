import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 使用merge函数将customers和orders进行合并，根据id和customerId进行匹配，使用'left'参数表示保留所有来自customers的数据
    customers_orders = customers.merge(orders, left_on='id', right_on='customerId',how='left')
    # 通过筛选出customerId为空的数据，得到没有下过订单的客户
    customers_no_orders = customers_orders[customers_orders['customerId'].isnull()].name.to_frame().rename(columns={'name':'Customers'})
    # 返回没有下过订单的客户数据
    return customers_no_orders


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 从 customers 数据框中选取除了在 orders 数据框中的 customerId 以外的所有数据
    df = customers[~customers["id"].isin(orders["customerId"])]
    print(df[["name"]])
    # 选取 df 数据框中的 "name" 列，并将其重命名为 "Customers"
    df = df[["name"]].rename(columns={"name":"Customers"})
    # 返回重命名后的数据框
    return df

# def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
#     # 从 customers 数据框中选取除了在 orders 数据框中的 customerId 以外的所有数据
#     return customers[~customers["id"].isin(orders["customerId"])][["name"]].rename(columns={"name":"Customers"})




# Customers table
customers = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
}
df_customers = pd.DataFrame(customers)

# Orders table
orders = {
    'id': [1, 2],
    'customerId': [3, 1]
}
df_orders = pd.DataFrame(orders)
print(df_customers)
print(df_orders)
find_customers(df_customers, df_orders)
