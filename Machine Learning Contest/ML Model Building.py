#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install numpy==1.23.1')
get_ipython().system('pip install pandas==1.4.3')
get_ipython().system('pip install matplotlib==3.3.2')
get_ipython().system('pip install seaborn==0.11.0')
get_ipython().system('pip install scikit_learn==1.0.2')
get_ipython().system('pip install scipy==1.9.0')


# In[ ]:


import numpy as np
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

import matplotlib.pyplot as plt
import seaborn as sns

import os
import time 
import re

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn import metrics

from scipy import stats

import warnings
warnings.filterwarnings('ignore')


# In[ ]:


df = pd.read__excel('news_share_data.xlsx')
print(df.shape)
df.head()


# In[ ]:


# Selecting only numerical features
cols_to_drop = ['City','State','Country','Sub-Area Cleaned','TownShip Name/ Society Name Cleaned',
                'Description Cleaned','Company Name Cleaned']

features = df.drop(cols_to_drop,axis=1).columns.tolist()
print("Final number of features: "+str(len(features)))


# In[ ]:




