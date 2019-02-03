# import numpy as np
import pandas as pd

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean = pd.DataFrame.mean(clms)


meanhours = allmean[0]
meansalary = allmean[1]
meantips = allmean[2]

sunday = clms[clms['Day of the Week'].isin(['Sunday'])]

tuesday = clms[clms['Day of the Week'].isin(['Tuesday'])]
print(sunday, tuesday)

# print("I worked for a total of " totalhours " hours, or an average of " meanhours " hours.")
# print("I earntad a total of $" totalsalary " in salary, or an average of $" meansalary " per day.")
# print("I earned a total of $" totaltips " in tips, or an average of " meantips " per day.")
