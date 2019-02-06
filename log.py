import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

# Overall of Averages and Totals

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean2 = pd.DataFrame.mean(clms)
alltotals = pd.DataFrame.sum(clms)
allmean = allmean2.round(2)

meanhours = str(allmean[0])
meansalary = str(allmean[1])
meantips = str(allmean[2])
totalhours = str(alltotals[1])
totalsalary = str(alltotals[2])
totaltips = str(alltotals[3])

print("I worked for a total of " + totalhours + " hours, or an average of " + meanhours + " hours.")
print("I earntad a total of $" + totalsalary + " in salary, or an average of $" + meansalary + " per day.")
print("I earned a total of $" + totaltips + " in tips, or an average of $" + meantips + " per day.")

# Averages and Totals by Days of the week

sunday = clms[clms['Day of the Week'].isin(['Sunday'])]
meansunday2 = pd.DataFrame.mean(sunday)
meansunday = meansunday2.round(2)
msunhours = str(meansunday[0])
msunsalary = str(meansunday[1])
msuntips = str(meansunday[2])

print('I worked an average of ' + msunhours + ' hours on Sundays. I also made an average of $' + msunsalary + ' in addition to $' + msuntips + ' in tips.')

saturday = clms[clms['Day of the Week'].isin(['Saturday'])]
meansaturday2 = pd.DataFrame.mean(saturday)
meansaturday = meansaturday2.round(2)
msathours = str(meansaturday[0])
msatsalary = str(meansaturday[1])
msattips = str(meansaturday[2])

print('I worked an average of ' + msathours + ' hours on Saturdays. I also made an average of $' + msatsalary + ' in addition to $' + msattips + ' in tips.')
weekday = clms[clms['Day of the Week'].isin(['Monday', 'Tuesday', 'Wednesday',  'Thursday', 'Friday'])]

meanweekday2 = pd.DataFrame.mean(weekday)
meanweekday = meanweekday2.round(2)
mwkhours = str(meanweekday[0])
mwksalary = str(meanweekday[1])
mwktips = str(meanweekday[2])
print('I worked an average of ' + mwkhours + ' hours on weekdays. I also made an average of $' + mwksalary + ' in addition to $' + mwktips + ' in tips.')

# Matplotlib implementation
n_groups = 2
overall = [allmean[1], allmean[2]]
sunday = [meansunday[1], meansunday[2]]
saturday = [meansaturday[1], meansaturday[2]]
weekday = [meanweekday[1], meanweekday[2]]

fig, ax = plt.subplots()
index = np.arrange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, overall, bar_width, alpha=opacity, color='b', label='Overall')

rects2 = plt.bar(index, saturday, bar_width, alpha=opacity, color='r', label='Saturday')

rects3 = plt.bar(index, sunday, bar_width, alpha=opacity, color='g', label='Sunday')

rects4 = plt.bar(index, weekday, bar_width, alpha=opacity, color='y', label='Weekday')
