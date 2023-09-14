#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install numpy==1.23.1')
get_ipython().system('pip install pandas==1.4.3')
get_ipython().system('pip install matplotlib==3.3.2')
get_ipython().system('pip install seaborn==0.11.0')
get_ipython().system('pip install joblib==1.1.0')
get_ipython().system('pip install nltk==3.7')
get_ipython().system('pip install wordcloud==1.8.2.2')
get_ipython().system('pip install scikit_learn==1.0.2')


# In[2]:


import numpy as np
import pandas as pd
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

import matplotlib.pyplot as plt
import seaborn as sns

import os
import time 
import re

import warnings
warnings.filterwarnings('ignore')


# In[4]:


df = pd.read_excel('news_share_data.xlsx')
print(df.shape)
df.head()


# In[5]:


df.sample(5)


# In[8]:


df['Property Area in Sq. Ft. Cleaned'].quantile(0.95)


# In[9]:


# Treating outliers in the numeric columns
cols_to_treat = ['Property Area in Sq. Ft. Cleaned','Price in lakhs Cleaned']

print("\nDistribution (raw):")
display(df[cols_to_treat].describe())        

# Outlier treatment
def clip_outliers(df,col):
    q_l = df[col].min()
    q_h = df[col].quantile(0.95)
    df[col] = df[col].clip(lower = q_l, upper = q_h)
    return df

for col in cols_to_treat:
    df = clip_outliers(df,col)
    

print("\nDistribution (after outlier treatment):")
display(df[cols_to_treat].describe())  


# In[ ]:




