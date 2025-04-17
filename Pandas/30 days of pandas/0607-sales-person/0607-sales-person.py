import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    red=pd.merge(orders,company[company.name=='RED'],on='com_id')
    return sales_person[~sales_person.sales_id.isin(red.sales_id.to_list())][['name']]
    