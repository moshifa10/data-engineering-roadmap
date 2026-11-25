import pandas as pd
import numpy as np
from datetime import datetime, date


# Extract the csv
def extract_wk1(file_name: str = "week1_pandas_orders.csv") -> pd.DataFrame:
    return pd.read_csv(filepath_or_buffer=file_name)


df  = extract_wk1()

# print(df.head())    
# print(df.tail())    
# rows , cols = df.shape
# print(f"rows : {rows}\ncolumns : {cols}")
print(df.dtypes)

# print(df.isna().any())
# print(df.duplicated().any())

# Data Preparations
df["order_date"] = pd.to_datetime(df["order_date"])

print(df["order_id"].duplicated().any())


trig = False
trigged_rows = []

for idx, row in df.iterrows():

    try:
        int(row["quantity"]) 

    except ValueError:
        trig = True
        trigged_rows.append(idx)

df = df.drop(trigged_rows)
print(trigged_rows)


df["total"] = pd.to_numeric(df["quantity"]) * pd.to_numeric(df["unit_price"])

print(df.head())


df.to_csv("new_created.csv", index=False)


def total_revenue(df: pd.DataFrame) -> int:
    return df["total"].sum()

print(total_revenue(df))


