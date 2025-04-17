import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter, sort, and return the 'name' column as a DataFrame
    return animals.query('weight > 100').sort_values('weight', ascending=False)[['name']]

   
    