# %%
import pandas as pd

data = {
    "Nome": ["Teó", "Nah", "Maria", "Nah", "Lara", "Teó"],
    "Idade": [32, 33, 2, 33, 31, 32],
    "updated_at": [1, 2, 3, 1, 2, 3]
}

# %%
df = pd.DataFrame(data)

# %%
df = (df.sort_values(by="updated_at", ascending=False)
        .drop_duplicates(subset=["Nome", "Idade"]))
df
# %%
