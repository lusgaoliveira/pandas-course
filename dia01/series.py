# %%
import pandas as pd
# %%
idades = [30, 42, 90, 34]
idades
# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total += (media - i)**2
variancia = total / (len(idades) - 1)
variancia

# %%
# Transformação da séries Pandas
series_idades = pd.Series(idades)
series_idades

# %%
series_idades.mean()
# %%
series_idades.var()
series_idades.std()
# %%
series_idades.median()
# %%
series_idades.quantile(0.25)
# %%
series_idades.describe()
# %%
series_idades.shape
# %%
idades[0]
# %%
series_idades[0]
series_idades.index = [40, 10, 30, 20]
# %%
series_idades
# %%
series_idades.iloc[2:4]
# %%
#Posição como lista normal
series_idades.iloc[0:2]
# %%
# Pegar pelo índice - label da série
series_idades.loc[40]
# %%
series_idades.name = "idades"
series_idades
# %%
series_idades = pd.Series(idades, name="idades")
series_idades
# %%
