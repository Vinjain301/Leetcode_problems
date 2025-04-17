import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({'immediate_percentage':[round(delivery[delivery.order_date==delivery.customer_pref_delivery_date]['delivery_id'].nunique()/delivery.delivery_id.nunique()*100.00,2)]})
    