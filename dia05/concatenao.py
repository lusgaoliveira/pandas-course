# %%

import pandas as pd
import os

def import_etl(path):

    name = path.split("/")[-1].split(".")[0]

    df = (pd.read_csv(path, sep = ";")
            .rename(columns={"valor":name})
            .set_index(["cod", "nome", "período"]))
    return df

# %%
path = "../data/ipea/"
files = os.listdir(path)

print(files)
# %%

dfs = []
for i in files:
    dfs.append(import_etl(path+i))

# %%
dfs[0]

# %%
df_bia = pd.concat(dfs, axis=1).reset_index()
df_bia.to_csv("../data/bia_consolidado.csv", sep=";", index=False)
# %%

data_01 = {
    "id": [1, 2, 3, 4],
    "nome": ["Teó", "Mat", "Nah", "Mah"],
    "idade": [31, 31, 32, 32],
}

df_01 = pd.DataFrame(data_01)

# %%
data_02 = {
    "id": [5, 6, 7, 8],
    "nome": ["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23, 33, 32, 32],
}

df_02 = pd.DataFrame(data_02)
df_02