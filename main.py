import pandas as pd
import DataPrepare.prepare as dp

# df = loadData()

df = dp.loadData()
# dp.distribution(df)
dp.trends(df)