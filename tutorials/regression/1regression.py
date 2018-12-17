import pandas as pd
import quandl, math
import numpy as np 

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
print(df.head())