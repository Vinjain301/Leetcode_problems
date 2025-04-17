import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(customers[~customers.id.isin(orders['customerId'])]['name'].rename('Customers'))
    