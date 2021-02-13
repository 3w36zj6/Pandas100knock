# %% init
import pandas as pd
df = pd.read_csv("./input/titanic3.csv")

# %% 1
df.head(5)

# %% 2
df.tail(5)

# %% 3
df.shape

# %% 4
df2 = pd.read_csv("./input/data1.csv")
df2.head(5)

# %% 5
df.sort_values(by="fare").head()

# %% 6
df_copy = df.copy()
df_copy.head()

# %% 7
df.dtypes
df["cabin"].dtype

# %% 8
df["pclass"].dtype
df["pclass"].astype(str)

# %% 9
len(df)

# %% 10
df.info()

# %% 11
df["sex"].unique()
df["cabin"].unique()

# %% 12
df.columns.tolist()

# %% 13
df.index.values

# %%
