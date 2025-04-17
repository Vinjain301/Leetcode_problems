import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(views[views.author_id==views.viewer_id]['author_id'].drop_duplicates().rename('id').sort_values())

    