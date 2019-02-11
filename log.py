import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcdefaults()

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

# Overall of Averages and Totals, [0]=HOURS, [1]=SALARY, [2]=TIPS

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean2 = pd.DataFrame.mean(clms)
alltotals = pd.DataFrame.sum(clms)
allmean = allmean2.round(2)


# Averages and Totals by Days of the week

sunday = clms[clms['Day of the Week'].isin(['Sunday'])]
meansunday2 = pd.DataFrame.mean(sunday)
meansunday = meansunday2.round(2)
sunhourly = (meansunday[1] + meansunday[2]) / meansunday[0]

saturday = clms[clms['Day of the Week'].isin(['Saturday'])]
meansaturday2 = pd.DataFrame.mean(saturday)
meansaturday = meansaturday2.round(2)
sathourly = (meansaturday[1] + meansaturday[2]) / meansaturday[0]
weekday = clms[clms['Day of the Week'].isin(['Monday', 'Tuesday', 'Wednesday',  'Thursday', 'Friday'])]

meanweekday2 = pd.DataFrame.mean(weekday)
meanweekday = meanweekday2.round(2)
weekhourly = (meanweekday[1] + meanweekday[2]) / meanweekday[0]

# Matplotlib implementation
n_groups = 3
overall = [allmean[1], allmean[2], (allmean[1] + allmean[2])]
sunday = [meansunday[1], meansunday[2], (meansunday[1] + meansunday[2])]
saturday = [meansaturday[1], meansaturday[2], (meansaturday[1] + meansaturday[2])]
weekday = [meanweekday[1], meanweekday[2], (meanweekday[1] + meanweekday[2])]

fig, ax = plt.subplots(figsize=(8, 6.5))
index = np.arange(n_groups)
bar_width = 0.15
opacity = 0.69

p1 = plt.bar(index, overall, bar_width, alpha=opacity, color='b', label='Overall')

p2 = plt.bar(index + bar_width, saturday, bar_width, alpha=opacity, color='y', label='Saturday')

p3 = plt.bar(index + bar_width*2, sunday, bar_width, alpha=opacity, color='g', label='Sunday')

p4 = plt.bar(index + bar_width*3, weekday, bar_width, alpha=opacity, color='r', label='Weekday')
plt.title('Money Earned Comparison')
plt.xticks(index + bar_width*1.5, ('Wage ($10/hr)', 'Tips', 'Total'))
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160], ['$0', '$10', '$20', '$30', '$40', '$50', '$60', '$70', '$80', '$90', '$100', '$110', '$120', '$130', '$140', '$150', '$160'])
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Overall', 'Saturday', 'Sunday', 'Weekday'), loc='best')


def autolabel(ps):
    for p in ps:
        height = p.get_height()
        ax.text(p.get_x() + p.get_width()/2., 1*height, '$' + str('%d' % int(height)), ha='center', va='bottom')


autolabel(p1)
autolabel(p2)
autolabel(p3)
autolabel(p4)
plt.grid()
plt.tight_layout()
plt.show()


# Projections for 3 months

days = 3*4
hourly = (sunhourly + sathourly + weekhourly) / 3

totalsunday = (sunday[0] + sunday[1]) * 4
totalweekday = (weekday[0] + weekday[1]) * 4
