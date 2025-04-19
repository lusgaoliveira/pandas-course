# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%
df.dtypes
# %%
df["Points"].astype(str)
# %%

df["Points_Double"] = df["Points"] * 2

# %%
df[["Points", "Points_Double"]].astype(str)
# %%

df[["UUID", "Name"]].astype(int)
# %%

df["Lista"] = [[1, 2] for _ in df.index]
df
# %%
