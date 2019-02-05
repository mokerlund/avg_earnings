import pandas as pd
import numpy as np

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

# Overall of Averages and Totals

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean = pd.DataFrame.mean(clms)
# To do: totalhours/sal/tips = pd.DF.sun(allmean[0])
npclms = np.array(clms[:, 1:])

meanhours = str(allmean[0])
meansalary = str(allmean[1])
meantips = str(allmean[2])
totalhours = str(np.sum(npclms[:, 1]))
totalsalary = str(np.sum(npclms[:, 2]))
totaltips = str(np.sum(npclms[:, 3]))
# print(str(np.sum(npclms[:, 0:3])))
print(npclms)
# print("I worked for a total of " + totalhours + " hours, or an average of " + meanhours + " hours.")
# print("I earntad a total of $" + totalsalary + " in salary, or an average of $" + meansalary + " per day.")
# print("I earned a total of $" + totaltips + " in tips, or an average of $" + meantips + " per day.")
# Averages and Totals by Days of the week

sunday = clms[clms['Day of the Week'].isin(['Sunday'])]
allsunday = pd.DataFrame.mean(sunday)

weekday = clms[clms['Day of the Week'].isin(['Monday', 'Tuesday', 'Wednesday',  'Thursday', 'Friday'])]
allweekday = pd.DataFrame.mean(weekday)

