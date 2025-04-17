import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return courses.groupby('class')['student'].count().rename('count').reset_index().query('count >= 5')[['class']]
    