import pytest
import pandas as pd

df_raw = pd.read_csv("D:/form/data/databricks_pj/tests/testdata.csv")

def pivot_and_clean(pdf, fillna):
    pdf["value"] = pd.to_numeric(pdf["value"])
    pdf = pdf.pivot_table(
        values="value", columns="indicator", index="date"
    )
    pdf = pdf.fillna(fillna)  # fillna después del pivot
    return pdf

pivoted = pivot_and_clean(df_raw,0)

value = pivoted.iloc[0]["Daily ICU occupancy"] 
print(value ==0)

