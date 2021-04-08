# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read the dataset as a Pandas dataframe in memory
# Note: here, we only read the first 100K rows. Other sampling options are available
dataset_heart = dataiku.Dataset("heart")
df = dataset_heart.get_dataframe(limit=100000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_new = df.iloc[0:1, :]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_new2 = df.iloc[1:2, :]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
py_recipe_output = dataiku.Dataset("new_df")
py_recipe_output.write_with_schema(df_new)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
py_recipe_output = dataiku.Dataset("new_df2")
py_recipe_output.write_with_schema(df_new2)
