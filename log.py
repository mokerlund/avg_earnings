import pandas as pd

filename = 'work_log.csv'
df = pd.read_csv(filename, delimiter=',')

# Overall of Averages and Totals

clms = df.loc[:, ['Day of the Week', 'Hours', 'Salary', 'Tips']]
allmean = pd.DataFrame.mean(clms)
alltotals = pd.DataFrame.sum(clms)

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
meansunday = pd.DataFrame.mean(sunday)
allsunday = pd.DataFrame.sum(sunday)
#this!!msunhours, msunsalary, msumtips, but leave those as comments, just use [1]etc.
print(meansunday[1])

# print('I worked an average of ' + meansunday[0] + ' hours on Sundays. I also made an average of $' + meansunday[1] + ' in addition to $' + meansunday[3] + ' in tips.')
weekday = clms[clms['Day of the Week'].isin(['Monday', 'Tuesday', 'Wednesday',  'Thursday', 'Friday'])]
meanweekday = pd.DataFrame.mean(weekday)
# allhours = 
# allprofit= allweekday[]

# print('I worked an average of ' + meanweekday)
