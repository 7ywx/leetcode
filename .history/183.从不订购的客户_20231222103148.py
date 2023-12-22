import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customers_orders = customers.merge(orders, left_on='id', right_on='customerId',how='left')
    customers_no_orders = customers_orders[customers_orders['customerId'].isnull()].name.to_frame().rename(columns={'name':'Customers'})
    print(customers_no_orders)
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
