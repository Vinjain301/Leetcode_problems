import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities=activities.drop_duplicates().sort_values('product')
    activities= pd.merge(activities.groupby('sell_date')['product'].count().rename('num_sold').reset_index(),activities.groupby('sell_date')['product'].unique().rename('products').reset_index(),on='sell_date')
    activities['products'] = [','.join(map(str, l)) for l in activities['products']]
    return activities

    


    