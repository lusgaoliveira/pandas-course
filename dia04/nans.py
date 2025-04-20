# %%
import pandas as pd
import numpy as np

data = {
    "nome": ["Teó", "Nah", "Maria", "Mah", "Jo"],
    "idade": [31, 32, 34, 12, np.nan],
    "renda": [np.nan, 3245, 357, 12432, np.nan],
}
# %%
df = pd.DataFrame(data)
df
# %%
df["idade"].isna().sum()

# %%

df.isna().sum()
# %%

df.isna().mean()

# %% 
df.fillna(
    {
        "idade": df["idade"].mean(),
        "renda": df["renda"].mean()
    }
)
# %%

df.fillna(df.mean())

# %%

df.dropna(subset=["idade", "renda"],how="any")
# %%

df.dropna(axis=1, thresh=2)
# %%
