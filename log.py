# import numpy as np
import pandas as pd

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean = pd.DataFrame.mean(clms)

dotwtotal = clms[clms['Day of the Week'].isin(['Sunday', 'Saturday'])]

meanhours = allmean[0]
meansalary = allmean[1]
meantips = allmean[2]
