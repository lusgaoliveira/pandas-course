# %%
import pandas as pd

data_users = {
    "id": [1, 2, 3, 4],
    "nome": ["Teó", "Mat", "Nah", "Mah"],
    "idade": [31, 31, 32, 32],
}

df_user = pd.DataFrame(data_users)
df_user
# %%

data_transacoes = {
    "id_user": [1, 1, 1, 2, 3, 3],
    "v1": [432, 532, 123, 6, 4, 87],
    "qt_produtos": [2, 1, 3, 6, 10, 2],
}

df_transcao = pd.DataFrame(data_transacoes)
df_transcao
# %%

df_transcao.merge(
    df_user, how="left", 
    left_on="id_user", right_on="id"
)
# %%
