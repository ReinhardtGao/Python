import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
'''Scatter'''
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plot1 = plt.scatter(x, y, marker = 'x')
plt.show(plot1)
df = pd.DataFrame({'x': x,'y': y})
plot2 = sns.jointplot(x="x", y="y", data=df, kind='scatter')
plt.show(plot2)
'''Lineplot'''
a = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
b = [5, 3, 6, 20 ,17 ,16, 19, 30, 32, 35]
plot3 = plt.plot(a, b)
plt.show(plot3)
plot4 = sns.lineplot(x="a", y="b", data=pd.DataFrame({'a': a,'b': b}))
plt.show(plot4)
'''Hist(bars)'''
c = np.random.randn(100)
s = pd.Series(c)
plot5 = plt.hist(s)
plt.show(plot5)
plot6 = sns.distplot(s, kde=True)
plt.show(plot6)
'''Bar'''
f = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
g = [5, 4, 8, 12, 7]
plot7 = plt.bar(f, g)
plt.show(plot7)
plot8 = sns.barplot(f, g)
plt.show(plot8)
'''Boxplot'''
data = np.random.normal(size=(10,4))
lbs = ['A', 'B', 'C', 'D']
plot9 = plt.boxplot(data, labels=lbs)
plt.show(plot9)
plot10 = sns.boxplot(data=pd.DataFrame(data, columns=lbs))
plt.show(plot10)
'''Pie'''
nums = [25,37,33,37,6]
lbs1 = ['A','B','C','D','E']
plot11 = plt.pie(x = nums, labels=lbs1)
plt.show(plot11)
'''Heatmap'''
flights = sns.load_dataset("flights")
data1 = flights.pivot('year','month','passengers')
plot12 = sns.heatmap(data1)
plt.show(plot12)
lbs2 = np.array([u" Attack ","KDA",u" Survival ",u" Raid ",u" Growth ",u" DPS "])
stats = [83, 61, 95, 67, 76, 88]
angles = np.linspace(0, 2*np.pi, len(lbs2), endpoint=False)
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, lbs2)
plt.show()
'''JointPlot'''
tips = sns.load_dataset("tips")
print(tips.head(10))
sns.jointplot(x="total_bill",y="tip",data=tips, kind='scatter')
sns.jointplot(x="total_bill",y="tip",data=tips, kind='kde')
sns.jointplot(x="total_bill",y="tip",data=tips, kind='hex')
plt.show()
'''Pairplot'''
iris = sns.load_dataset('iris')
plot15 = sns.pairplot(iris)
plt.show(plot15)
'''Exercise'''
car_crashes = sns.load_dataset('car_crashes')
plotA = sns.pairplot(car_crashes)
plt.show(plotA)
print(car_crashes.head(10))
sns.jointplot(x="total",y="alcohol",data=car_crashes, kind='scatter')
sns.jointplot(x="total",y="alcohol",data=car_crashes, kind='kde')
sns.jointplot(x="total",y="alcohol",data=car_crashes, kind='hex')
plt.show()
