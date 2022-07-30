#!/usr/bin/env python
# coding: utf-8
# In[1]:

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
#seaborn built on top of matplot lib for better graphs
import seaborn as sns
#method to override matpltlib graphs
sns.set()

# In[2]:

data = pd.read_csv("pageviews_sales.csv")

# In[3]:

data

# In[4]:

data.describe()

# Declare variables

# In[5]:

y = data["sales"]
x1= data["pageviews"]

# In[6]:

plt.scatter(x1,y)
#create labels and set font
plt.xlabel("pageviews",fontsize=18)
plt.ylabel("sales",fontsize=18)
#show graph
plt.show()

# In[7]:

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()
results.summary()

# In[9]:

plt.scatter(x1,y)
yhat = 0.0971*x1+-8.9342
fig = plt.plot(x1,yhat, lw=4, c="orange", label="regression line")
#create labels and set font
plt.xlabel("pageviews",fontsize=18)
plt.ylabel("sales",fontsize=18)
#show graph
plt.show()

# In[ ]:
