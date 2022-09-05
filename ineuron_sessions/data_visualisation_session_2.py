
# Aug 14 2022 session
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# from chart_studio.plotly import plotly

df = sns.load_dataset('iris')  # seaborn is library having preloaded dataset
# print(df)
# df.plot(kind='area',alpha = 0.1) # alpha gives color density
# plt.show() # to show graph n pycharm

# df.plot.scatter(x='sepal_length', y= 'sepal_width')
# df.plot.scatter(x='sepal_length', y= 'petal_length')

# df.plot.scatter(x='sepal_length', y='petal_length', c='sepal_width', s=100)  # c means colour of the dot, s= size of dot, here size is constant we can make it variable also
# df.plot.scatter(x='sepal_length', y='petal_length', c='sepal_width', s=df['sepal_length']*20)
# df.plot.hexbin(x='sepal_length', y='petal_length',gridsize=10) # instead od dot hexabin will come
# plt.show()

from mpl_toolkits import mplot3d

# x = np.linspace(-1, 6, 30)  # will generate 30 datapoints between -1,6
# y = np.linspace(-1, 6, 30)
# z = x + y
# ax = plt.axes(projection='3d')
# ax.plot3D(x, y, z)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# plt.show()
# df.iloc[5:11].plot(kind='bar',figsize=(5,5)) # figsize is size of bar, graph
# df.iloc[5:11].plot(kind='barh',figsize=(5,5)) # bar in horizontal direction
# df.plot(kind='hist', figsize=(5, 5))  # histogram chart x axis is range and in y axis it will be frequency
# df.hist(figsize=(5, 5), color='g', alpha=0.9)  # alpha gives color density
# plt.show()

# using cufflinks
import cufflinks as cf
import plotly

# plotly.offline.init_notebook_mode()
cf.go_offline()
setattr(plotly.offline, "__PLOTLY_OFFLINE_INITIALIZED", True)
# df.iplot(x='sepal_length',y='sepal_width',size='sepal_length',kind='bubble')
# df.iplot(x='sepal_length',y='sepal_width',z='petal_length',size='sepal_length',kind='bubble')

df1 = sns.load_dataset('tips')
# print(df1)
# df1.plot(x='total_bill', y='tip', kind='scatter')
# plt.show()  # using matplotlib
# df1.iplot(x='total_bill', y='tip', kind='scatter', mode='markers')  # using cufflink
sns.relplot(x='total_bill', y='tip', data=df1, hue='smoker', style='time')  # using seaborne
sns.relplot(x='total_bill', y='tip', data=df1, col='time')
sns.relplot(x='total_bill', y='tip', data=df1, col='day')
sns.relplot(x='sepal_length',y='sepal_length',data=df,col='species')
sns.catplot(x='day',y='total_bill',data=df1)
sns.pairplot(df)
sns.pairplot(df1)
# df.scatter_matrix()# using matplotlib
# sns.jointplot(x=df1.total_bill, y=df1.tip)
# sns.regplot(x=df1.total_bill, y=df1.tip)
sns.set(rc={'figure.figsize': (20, 10)})  # graph size in seaborne
plt.show()# for viewing seaborne graph also u can use plt.show()
#resources
# https://github.com/santosjorge/cufflinks
# plotly - https://plotly.com/python/plotly-express/
# seaborn - https://seaborn.pydata.org/index.html
# matplotlib - https://matplotlib.org/stable/index.html
# https://github.com/sudh9931/graph
